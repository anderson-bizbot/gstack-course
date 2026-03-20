#!/usr/bin/env python3
"""
Generate per-skill lesson files, skills-catalog.md, and skill-index.json
from gstack's SKILL.md.tmpl source templates (not the generated SKILL.md).

Templates are the source of truth — they contain only the unique workflow
without injected boilerplate (preamble, telemetry, AskUserQuestion format, etc.)
"""

import json
import os
import re
import sys
import yaml
from pathlib import Path
from datetime import datetime, timezone


# Template placeholders to strip
TEMPLATE_PLACEHOLDERS = [
    '{{PREAMBLE}}',
    '{{BROWSE_SETUP}}',
    '{{TELEMETRY}}',
    '{{COMPLETION_STATUS}}',
    '{{CONTRIBUTOR_MODE}}',
    '{{COMPLETENESS}}',
    '{{ASK_USER_QUESTION}}',
]


def extract_frontmatter(content: str) -> dict:
    match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return {}
    try:
        return yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        return {}


def strip_template_placeholders(content: str) -> str:
    """Remove frontmatter and {{PLACEHOLDER}} lines from template."""
    # Remove frontmatter
    content = re.sub(r'^---\s*\n.*?\n---\s*\n', '', content, flags=re.DOTALL)
    # Remove placeholder lines
    lines = []
    for line in content.split('\n'):
        stripped = line.strip()
        if any(stripped == p for p in TEMPLATE_PLACEHOLDERS):
            continue
        lines.append(line)
    return '\n'.join(lines).strip()


def extract_phases(content: str) -> list[dict]:
    """Extract named phases/sections from the unique content."""
    phases = []
    current = None

    for line in content.split('\n'):
        heading_match = re.match(r'^(#{1,3})\s+(.+)$', line)
        if heading_match:
            if current:
                current['content'] = '\n'.join(current['content_lines']).strip()
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
        current['content'] = '\n'.join(current['content_lines']).strip()
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


def slash_name(dir_name: str) -> str:
    """Convert template dir name to slash command."""
    if dir_name == 'gstack' or dir_name == '.':
        return '/gstack'
    return '/' + dir_name


def find_templates(gstack_path: Path) -> list[tuple[str, Path]]:
    """Find all SKILL.md.tmpl files and their logical names."""
    templates = []
    for tmpl in sorted(gstack_path.rglob('SKILL.md.tmpl')):
        # Skip the root template (it's the main gstack skill, handle separately)
        rel = tmpl.relative_to(gstack_path)
        dir_name = str(rel.parent)
        if dir_name == '.':
            dir_name = 'gstack'
        templates.append((dir_name, tmpl))
    return templates


def extract_questions(content: str) -> list[str]:
    """Extract questions Claude will ask the user."""
    questions = []
    # Pattern: **Ask:** "question?"
    for m in re.finditer(r'\*\*Ask:\*\*\s*["\u201c]([^"\u201d]+\?)', content):
        questions.append(m.group(1))
    # Pattern: "question?" in quoted blocks
    for m in re.finditer(r'["\u201c]([A-Z][^"\u201d]{20,}\?)\s*["\u201d]', content):
        q = m.group(1)
        if q not in questions:
            questions.append(q)
    # Pattern: > question text?
    for m in re.finditer(r'^>\s*(.{20,}\?)\s*$', content, re.MULTILINE):
        q = m.group(1).strip()
        if q not in questions and not q.startswith('http'):
            questions.append(q)
    return questions[:8]


def extract_outputs(phases: list) -> list[str]:
    """Identify what the skill produces."""
    outputs = []
    output_keywords = ['write', 'save', 'create', 'produce', 'generate', 'output', 'design doc', 'PR', 'commit']
    for phase in phases:
        title_lower = phase['title'].lower()
        content = phase.get('content', '')
        if any(k in title_lower for k in ['output', 'design doc', 'result', 'handoff', 'report', 'ship']):
            outputs.append(phase['title'])
        # Check for "Write to" patterns
        for m in re.finditer(r'Write to\s+`([^`]+)`', content):
            outputs.append(f"File: `{m.group(1)}`")
    return outputs[:5]


def generate_lesson(skill: dict, unique_content: str, phases: list) -> str:
    """Generate a lesson file for a single skill."""
    lines = []
    slash = skill['slash']
    desc = skill['description']
    sprint_phase = skill['phase']
    version = skill.get('version', '')

    lines.append(f'# Lesson: `{slash}`')
    lines.append('')
    ver_str = f' | Version: {version}' if version else ''
    lines.append(f'> Sprint phase: **{sprint_phase}** | Template: {skill["template_lines"]} lines{ver_str}')
    lines.append(f'> Source: `garrytan/gstack/{skill["dir_name"]}/SKILL.md.tmpl`')
    lines.append('')

    # --- What is this? ---
    lines.append('## What Is This?')
    lines.append('')
    desc_lines = desc.strip().split('\n')
    # Get substantive lines (not trigger/suggest lines)
    for dl in desc_lines:
        dl = dl.strip()
        if dl and not dl.lower().startswith('use when') and not dl.lower().startswith('proactively'):
            lines.append(dl)
    lines.append('')

    # --- When do you use it? ---
    lines.append('## When Do You Use It?')
    lines.append('')
    for dl in desc_lines:
        dl = dl.strip()
        if 'use when' in dl.lower() or 'proactively suggest' in dl.lower() or 'use before' in dl.lower():
            lines.append(f'- {dl}')
    if not any('use when' in dl.lower() or 'proactively' in dl.lower() for dl in desc_lines):
        lines.append(f'- During the **{sprint_phase}** phase of your sprint')
    lines.append('')

    # --- What do you say? ---
    lines.append('## What Do You Say to Claude?')
    lines.append('')
    lines.append(f'Type `{slash}` in Claude Code. The skill activates and guides you.')
    lines.append('')
    triggers = re.findall(r'"([^"]{3,})"', desc)
    if triggers:
        lines.append('**Natural language triggers:**')
        for t in triggers[:6]:
            lines.append(f'- "{t}"')
        lines.append('')

    # --- What will Claude ask? ---
    questions = extract_questions(unique_content)
    lines.append('## What Will Claude Ask You?')
    lines.append('')
    if questions:
        lines.append('Claude walks you through a structured conversation:')
        lines.append('')
        for q in questions:
            lines.append(f'- *"{q}"*')
        lines.append('')
    else:
        lines.append('This skill runs mostly automatically — you provide initial context and Claude handles the rest.')
        lines.append('')

    # --- What do you get? ---
    outputs = extract_outputs(phases)
    lines.append('## What Do You Get?')
    lines.append('')
    if outputs:
        for o in outputs:
            lines.append(f'- {o}')
    else:
        lines.append(f'Structured output for the **{sprint_phase}** phase of your sprint.')
    lines.append('')

    # --- The workflow ---
    lines.append('## The Workflow')
    lines.append('')
    step_num = 0
    for phase in phases:
        if phase['level'] <= 2:
            step_num += 1
            # Get first meaningful sentence from content
            first_sentence = ''
            for cl in phase.get('content', '').split('\n'):
                cl = cl.strip()
                if cl and not cl.startswith('```') and not cl.startswith('|') and not cl.startswith('-') and not cl.startswith('#') and len(cl) > 15:
                    first_sentence = cl[:200]
                    if len(cl) > 200:
                        first_sentence += '...'
                    break
            lines.append(f'**Step {step_num}: {phase["title"]}**')
            if first_sentence:
                lines.append(f'> {first_sentence}')
            lines.append('')
    if step_num == 0:
        lines.append('This skill runs as a single automated workflow.')
        lines.append('')

    # --- Sprint position ---
    lines.append('## Where It Fits')
    lines.append('')
    lines.append('```')
    lines.append(f'Think → Plan → Build → Review → Test → Ship')
    lines.append(f'                    ↑')
    lines.append(f'        You are here: {sprint_phase.upper()} phase')
    lines.append('```')
    lines.append('')

    # --- What comes next ---
    next_map = {
        'Think': ['After thinking, plan: `/plan-ceo-review` → `/plan-eng-review`', 'Then build, review, test, ship.'],
        'Review': ['After review, test: `/qa` or `/qa-only`', 'Then ship: `/ship`'],
        'Test': ['After testing, ship: `/ship`', 'If bugs found, fix and re-test.'],
        'Ship': ['After shipping, document: `/document-release`', 'End of week: `/retro`'],
        'Safety': ['Continue your current workflow with safety enabled.', 'Use `/unfreeze` when done.'],
        'Meta': ['Continue with your current sprint.'],
    }
    lines.append('## What Comes Next?')
    lines.append('')
    for n in next_map.get(sprint_phase, ['Continue with the next sprint phase.']):
        lines.append(f'- {n}')
    lines.append('')

    return '\n'.join(lines)


def generate(gstack_path: str, output_dir: str):
    gstack = Path(gstack_path)
    templates = find_templates(gstack)

    if not templates:
        print(f"ERROR: No SKILL.md.tmpl files found in {gstack_path}", file=sys.stderr)
        sys.exit(1)

    output_path = Path(output_dir)
    lessons_dir = output_path / 'lessons'
    lessons_dir.mkdir(parents=True, exist_ok=True)

    skills = []

    for dir_name, tmpl_path in templates:
        content = tmpl_path.read_text(encoding='utf-8')
        frontmatter = extract_frontmatter(content)

        name = frontmatter.get('name', dir_name)
        description = frontmatter.get('description', '')
        version = frontmatter.get('version', '')
        if not isinstance(description, str):
            description = str(description)

        desc_oneline = description.strip().split('\n')[0].strip()[:200]

        # Get unique content (strip placeholders)
        unique_content = strip_template_placeholders(content)
        template_lines = len(content.split('\n'))
        unique_lines = len(unique_content.split('\n'))
        phases = extract_phases(unique_content)

        phase = classify_phase(dir_name, description)

        skill_data = {
            'dir_name': dir_name,
            'name': name,
            'slash': slash_name(dir_name),
            'description': description.strip(),
            'description_oneline': desc_oneline,
            'version': str(version) if version else '',
            'phase': phase,
            'template_lines': template_lines,
            'unique_lines': unique_lines,
            'section_count': len(phases),
            'sections': [p['title'] for p in phases],
        }
        skills.append(skill_data)

        # Generate lesson
        lesson = generate_lesson(skill_data, unique_content, phases)
        lesson_file = lessons_dir / f'{dir_name}.md'
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

    # Build catalog
    phases_order = ['Think', 'Review', 'Test', 'Ship', 'Safety', 'Meta', 'Other']
    by_phase = {}
    for s in skills:
        by_phase.setdefault(s['phase'], []).append(s)

    cat = [
        '# gstack Skills Catalog',
        '',
        f'> Auto-generated from [garrytan/gstack](https://github.com/garrytan/gstack) **templates**',
        f'> {len(skills)} skills | Generated: {datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")}',
        '',
        '## Quick Reference',
        '',
        '| Phase | Skill | What You Say | Lines | Version |',
        '|-------|-------|-------------|-------|---------|',
    ]

    for phase in phases_order:
        for s in by_phase.get(phase, []):
            ver = s['version'] or '-'
            cat.append(
                f"| {phase} | [`{s['slash']}`](lessons/{s['dir_name']}.md) "
                f"| `{s['slash']}` | {s['template_lines']} | {ver} |"
            )

    cat.append('')
    cat.append('## The Sprint Flow')
    cat.append('')
    cat.append('```')
    cat.append('THINK:  /office-hours → /plan-ceo-review → /plan-eng-review')
    cat.append('        /plan-design-review → /design-consultation')
    cat.append('BUILD:  [you describe what you want, Claude writes code]')
    cat.append('REVIEW: /review → /investigate → /design-review')
    cat.append('TEST:   /qa → /qa-only → /browse')
    cat.append('SHIP:   /ship → /document-release → /retro')
    cat.append('SAFETY: /careful → /freeze → /guard → /unfreeze')
    cat.append('```')
    cat.append('')
    cat.append('## Lessons by Phase')
    cat.append('')

    for phase in phases_order:
        phase_skills = by_phase.get(phase, [])
        if not phase_skills:
            continue
        cat.append(f'### {phase}')
        cat.append('')
        for s in phase_skills:
            cat.append(f'- [`{s["slash"]}`](lessons/{s["dir_name"]}.md) — {s["description_oneline"][:80]}')
        cat.append('')

    with open(output_path / 'skills-catalog.md', 'w') as f:
        f.write('\n'.join(cat))

    print(f"Generated from templates: {len(skills)} skills")
    print(f"  → {output_path / 'skill-index.json'}")
    print(f"  → {output_path / 'skills-catalog.md'}")
    print(f"  → {lessons_dir}/ ({len(skills)} lesson files)")


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <gstack-repo-path> <output-dir>")
        sys.exit(1)

    generate(sys.argv[1], sys.argv[2])
