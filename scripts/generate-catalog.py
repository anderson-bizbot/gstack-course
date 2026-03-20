#!/usr/bin/env python3
"""
Generate per-skill lesson files, skills-catalog.md, and skill-index.json
from the gstack repo. Each lesson teaches a business person how to use
that skill through the Claude Code prompt chain.
"""

import json
import os
import re
import sys
import yaml
from pathlib import Path
from datetime import datetime, timezone


# Shared sections that appear in every skill (boilerplate to strip)
BOILERPLATE_HEADERS = [
    'Preamble (run first)',
    'AskUserQuestion Format',
    'Completeness Principle',
    'Boil the Lake',
    'Contributor Mode',
    'Completion Status Protocol',
    'Telemetry (run last)',
]

# Markers that indicate start of boilerplate
BOILERPLATE_MARKERS = [
    '## Preamble (run first)',
    '## AskUserQuestion Format',
    '## Completeness Principle — Boil the Lake',
    '## Contributor Mode',
    '## Completion Status Protocol',
    '## Telemetry (run last)',
    '<!-- AUTO-GENERATED from SKILL.md.tmpl',
]


def extract_frontmatter(content: str) -> dict:
    match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return {}
    try:
        return yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        return {}


def strip_boilerplate(content: str) -> str:
    """Remove shared boilerplate sections, keep skill-specific workflow."""
    # Remove frontmatter
    content = re.sub(r'^---\s*\n.*?\n---\s*\n', '', content, flags=re.DOTALL)
    # Remove HTML comments
    content = re.sub(r'<!--.*?-->\s*\n?', '', content, flags=re.DOTALL)

    lines = content.split('\n')
    result = []
    skip = False

    for i, line in enumerate(lines):
        # Check if this line starts a boilerplate section
        is_boilerplate_start = False
        for marker in BOILERPLATE_MARKERS:
            if line.strip().startswith(marker.strip()):
                is_boilerplate_start = True
                break

        if is_boilerplate_start:
            skip = True
            continue

        # Stop skipping when we hit a new ## heading that isn't boilerplate
        if skip and re.match(r'^##\s+', line):
            is_still_boilerplate = False
            for marker in BOILERPLATE_MARKERS:
                if line.strip().startswith(marker.strip()):
                    is_still_boilerplate = True
                    break
            if not is_still_boilerplate:
                skip = False

        if not skip:
            result.append(line)

    return '\n'.join(result).strip()


def extract_phases(unique_content: str) -> list[dict]:
    """Extract named phases/sections from the unique content."""
    phases = []
    current = None

    for line in unique_content.split('\n'):
        heading_match = re.match(r'^(#{1,3})\s+(.+)$', line)
        if heading_match:
            if current:
                phases.append(current)
            level = len(heading_match.group(1))
            current = {
                'title': heading_match.group(2).strip(),
                'level': level,
                'content_lines': []
            }
        elif current:
            current['content_lines'].append(line)

    if current:
        phases.append(current)

    return phases


def classify_phase(name: str, description: str) -> str:
    name_lower = name.lower()
    if any(k in name_lower for k in ['office-hours', 'plan-ceo', 'plan-eng', 'plan-design', 'design-consultation']):
        return 'Think'
    if any(k in name_lower for k in ['review', 'investigate']) and 'design-review' not in name_lower:
        return 'Review'
    if 'design-review' in name_lower:
        return 'Review'
    if any(k in name_lower for k in ['qa', 'browse', 'cookie', 'browser']):
        return 'Test'
    if any(k in name_lower for k in ['ship', 'document', 'retro', 'release']):
        return 'Ship'
    if any(k in name_lower for k in ['careful', 'freeze', 'guard', 'unfreeze']):
        return 'Safety'
    if any(k in name_lower for k in ['upgrade', 'update']):
        return 'Meta'
    return 'Other'


def slash_name(skill_name: str) -> str:
    if skill_name.startswith('gstack-'):
        return '/' + skill_name[7:]
    if skill_name == 'gstack':
        return '/gstack'
    return '/' + skill_name


def generate_lesson(skill: dict, unique_content: str, phases: list) -> str:
    """Generate a lesson file for a single skill."""
    lines = []
    slash = skill['slash']
    name = skill['name']
    desc = skill['description']
    sprint_phase = skill['phase']

    lines.append(f'# Lesson: `{slash}`')
    lines.append('')
    lines.append(f'> Sprint phase: **{sprint_phase}** | Size: {skill["size_bytes"]:,} bytes')
    lines.append(f'> Source: `garrytan/gstack/.agents/skills/{skill["dir_name"]}/SKILL.md`')
    lines.append('')

    # --- What is this? (plain English, no jargon) ---
    lines.append('## What Is This?')
    lines.append('')
    # Use first line of description
    desc_lines = desc.strip().split('\n')
    for dl in desc_lines[:3]:
        if dl.strip():
            lines.append(dl.strip())
    lines.append('')

    # --- When do you use it? ---
    lines.append('## When Do You Use It?')
    lines.append('')
    # Extract "Use when" from description
    use_when = []
    for dl in desc_lines:
        if 'use when' in dl.lower() or 'proactively suggest' in dl.lower():
            use_when.append(dl.strip())
    if use_when:
        for uw in use_when:
            lines.append(f'- {uw}')
    else:
        lines.append(f'- When the {sprint_phase.lower()} phase of your sprint calls for it')
    lines.append('')

    # --- What do you say to Claude? ---
    lines.append('## What Do You Say to Claude?')
    lines.append('')
    lines.append(f'Type `{slash}` in Claude Code. That\'s it. The skill takes over from there.')
    lines.append('')
    # Extract trigger phrases from description
    triggers = re.findall(r'"([^"]+)"', desc)
    if triggers:
        lines.append('**Trigger phrases that also work:**')
        for t in triggers[:8]:
            lines.append(f'- "{t}"')
        lines.append('')

    # --- What will Claude ask you? ---
    lines.append('## What Will Claude Ask You?')
    lines.append('')
    # Extract questions/AskUserQuestion patterns from unique content
    questions = []
    for phase in phases:
        content = '\n'.join(phase['content_lines'])
        # Find quoted questions
        q_matches = re.findall(r'"([^"]{20,})\?"', content)
        questions.extend([q + '?' for q in q_matches[:3]])
        # Find "Ask:" patterns
        ask_matches = re.findall(r'Ask:\s*"([^"]+)"', content)
        questions.extend(ask_matches[:3])

    if questions:
        lines.append('Claude will walk you through a structured conversation. Key questions include:')
        lines.append('')
        for q in questions[:6]:
            lines.append(f'- *"{q}"*')
        lines.append('')
    else:
        lines.append('Claude handles this automatically — you provide the context, it runs the workflow.')
        lines.append('')

    # --- What do you get out of it? ---
    lines.append('## What Do You Get?')
    lines.append('')
    # Look for output mentions in phases
    outputs = []
    for phase in phases:
        title = phase['title'].lower()
        if any(k in title for k in ['output', 'design doc', 'result', 'handoff', 'report']):
            outputs.append(phase['title'])

    if outputs:
        for o in outputs:
            lines.append(f'- **{o}**')
        lines.append('')
    else:
        lines.append(f'The skill produces structured output relevant to the {sprint_phase.lower()} phase.')
        lines.append('')

    # --- The Workflow (simplified) ---
    lines.append('## The Workflow (Step by Step)')
    lines.append('')
    phase_count = 0
    for phase in phases:
        if phase['level'] <= 2:
            phase_count += 1
            content_preview = '\n'.join(phase['content_lines'][:3]).strip()
            # Get first meaningful sentence
            first_sentence = ''
            for cl in phase['content_lines']:
                cl = cl.strip()
                if cl and not cl.startswith('```') and not cl.startswith('|') and not cl.startswith('-'):
                    first_sentence = cl[:150]
                    break
            lines.append(f'{phase_count}. **{phase["title"]}**')
            if first_sentence:
                lines.append(f'   {first_sentence}')
            lines.append('')

    if phase_count == 0:
        lines.append('This skill runs as a single automated step.')
        lines.append('')

    # --- Where it fits ---
    lines.append('## Where It Fits in the Sprint')
    lines.append('')
    lines.append('```')
    sprint = '/office-hours → /plan-ceo-review → /plan-eng-review → [build] → /review → /qa → /ship → /retro'
    # Highlight current skill
    highlighted = sprint.replace(slash, f'>>>{slash}<<<')
    lines.append(highlighted)
    lines.append('```')
    lines.append('')

    # --- What comes next? ---
    lines.append('## What Comes Next?')
    lines.append('')
    next_skills = {
        'Think': ['/plan-ceo-review', '/plan-eng-review', '/plan-design-review'],
        'Review': ['/qa', '/ship'],
        'Test': ['/ship', '/review'],
        'Ship': ['/document-release', '/retro'],
        'Safety': ['(continue your current workflow with safety enabled)'],
        'Meta': ['(continue with your current sprint)'],
    }
    for ns in next_skills.get(sprint_phase, ['See workflow patterns']):
        lines.append(f'- `{ns}`')
    lines.append('')

    # --- Pro Tips ---
    lines.append('## Pro Tips')
    lines.append('')
    # Extract anti-patterns or tips from unique content
    tips_found = False
    for phase in phases:
        content = '\n'.join(phase['content_lines'])
        if 'red flag' in content.lower():
            lines.append('- Watch for red flags Claude identifies — they\'re based on YC pattern matching')
            tips_found = True
            break
    if not tips_found:
        lines.append(f'- Run this skill before moving to the next sprint phase')
        lines.append(f'- The output feeds automatically into downstream skills')
    lines.append('')

    return '\n'.join(lines)


def generate(gstack_path: str, output_dir: str):
    skills_dir = Path(gstack_path) / '.agents' / 'skills'

    if not skills_dir.exists():
        print(f"ERROR: {skills_dir} not found", file=sys.stderr)
        sys.exit(1)

    output_path = Path(output_dir)
    lessons_dir = output_path / 'lessons'
    lessons_dir.mkdir(parents=True, exist_ok=True)

    skills = []

    for skill_dir in sorted(skills_dir.iterdir()):
        if not skill_dir.is_dir():
            continue

        skill_md = skill_dir / 'SKILL.md'
        if not skill_md.exists():
            continue

        content = skill_md.read_text(encoding='utf-8')
        frontmatter = extract_frontmatter(content)

        name = frontmatter.get('name', skill_dir.name)
        description = frontmatter.get('description', '')
        if not isinstance(description, str):
            description = str(description)

        desc_oneline = description.strip().split('\n')[0].strip()[:200]
        size_bytes = len(content.encode('utf-8'))
        phase = classify_phase(skill_dir.name, description)

        # Extract unique content (strip boilerplate)
        unique_content = strip_boilerplate(content)
        phases = extract_phases(unique_content)

        skill_data = {
            'dir_name': skill_dir.name,
            'name': name,
            'slash': slash_name(skill_dir.name),
            'description': description.strip(),
            'description_oneline': desc_oneline,
            'phase': phase,
            'size_bytes': size_bytes,
            'unique_size_bytes': len(unique_content.encode('utf-8')),
            'section_count': len(phases),
            'sections': [p['title'] for p in phases],
            'has_scripts': (skill_dir / 'scripts').exists(),
            'has_references': (skill_dir / 'references').exists(),
            'has_assets': (skill_dir / 'assets').exists(),
        }
        skills.append(skill_data)

        # Generate per-skill lesson
        lesson = generate_lesson(skill_data, unique_content, phases)
        lesson_file = lessons_dir / f'{skill_dir.name}.md'
        lesson_file.write_text(lesson, encoding='utf-8')

    # Build index JSON
    index = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'gstack_source': 'https://github.com/garrytan/gstack',
        'skill_count': len(skills),
        'skills': skills,
    }

    with open(output_path / 'skill-index.json', 'w') as f:
        json.dump(index, f, indent=2)

    # Build markdown catalog (now just a directory pointing to lessons)
    phases_order = ['Think', 'Review', 'Test', 'Ship', 'Safety', 'Meta', 'Other']
    by_phase = {}
    for s in skills:
        by_phase.setdefault(s['phase'], []).append(s)

    cat_lines = [
        '# gstack Skills Catalog',
        '',
        f'> Auto-generated from [garrytan/gstack](https://github.com/garrytan/gstack)',
        f'> {len(skills)} skills | Generated: {datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")}',
        '',
        '## How to Use This Course',
        '',
        'Each skill has a **lesson file** in `references/lessons/` that teaches you:',
        '- What the skill does (plain English)',
        '- When to use it',
        '- What you say to Claude to trigger it',
        '- What Claude will ask you',
        '- What you get out of it',
        '- Where it fits in the sprint workflow',
        '',
        'Read the lesson for any skill you want to learn. Start with `/office-hours`.',
        '',
        '## Quick Reference',
        '',
        '| Phase | Skill | What You Say | One-Liner |',
        '|-------|-------|-------------|-----------|',
    ]

    for phase in phases_order:
        for s in by_phase.get(phase, []):
            cat_lines.append(
                f"| {phase} | [`{s['slash']}`](lessons/{s['dir_name']}.md) "
                f"| Type `{s['slash']}` | {s['description_oneline'][:60]} |"
            )

    cat_lines.append('')
    cat_lines.append('## The Sprint (Read in This Order)')
    cat_lines.append('')
    cat_lines.append('gstack is a process. Skills chain together:')
    cat_lines.append('')
    cat_lines.append('```')
    cat_lines.append('Think:  /office-hours → /plan-ceo-review → /plan-eng-review')
    cat_lines.append('                        /plan-design-review → /design-consultation')
    cat_lines.append('Build:  [you + Claude write code]')
    cat_lines.append('Review: /review → /investigate → /design-review')
    cat_lines.append('Test:   /qa → /qa-only → /browse')
    cat_lines.append('Ship:   /ship → /document-release → /retro')
    cat_lines.append('Safety: /careful → /freeze → /guard → /unfreeze')
    cat_lines.append('```')
    cat_lines.append('')
    cat_lines.append('## Lessons by Phase')
    cat_lines.append('')

    for phase in phases_order:
        phase_skills = by_phase.get(phase, [])
        if not phase_skills:
            continue
        cat_lines.append(f'### {phase}')
        cat_lines.append('')
        for s in phase_skills:
            cat_lines.append(f'- [`{s["slash"]}`](lessons/{s["dir_name"]}.md) — {s["description_oneline"][:80]}')
        cat_lines.append('')

    with open(output_path / 'skills-catalog.md', 'w') as f:
        f.write('\n'.join(cat_lines))

    print(f"Generated: {len(skills)} skills")
    print(f"  → {output_path / 'skill-index.json'}")
    print(f"  → {output_path / 'skills-catalog.md'}")
    print(f"  → {lessons_dir}/ ({len(skills)} lesson files)")


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <gstack-repo-path> <output-dir>")
        sys.exit(1)

    generate(sys.argv[1], sys.argv[2])
