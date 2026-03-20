#!/usr/bin/env python3
"""
Generate skills-catalog.md and skill-index.json dynamically from gstack repo.
Reads every SKILL.md, extracts frontmatter, computes sizes, and builds the catalog.
"""

import json
import os
import re
import sys
import yaml
from pathlib import Path
from datetime import datetime, timezone


def extract_frontmatter(content: str) -> dict:
    """Extract YAML frontmatter from SKILL.md content."""
    match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return {}
    try:
        return yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        return {}


def extract_sections(content: str) -> list[str]:
    """Extract top-level markdown headings after frontmatter."""
    # Strip frontmatter
    stripped = re.sub(r'^---\s*\n.*?\n---\s*\n', '', content, flags=re.DOTALL)
    headings = re.findall(r'^##?\s+(.+)$', stripped, re.MULTILINE)
    return headings[:10]  # First 10 headings for overview


def classify_phase(name: str, description: str) -> str:
    """Classify a skill into a sprint phase based on name and description."""
    name_lower = name.lower()
    desc_lower = description.lower()

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

    # Fallback: check description
    if any(k in desc_lower for k in ['plan', 'brainstorm', 'design system', 'reframe']):
        return 'Think'
    if any(k in desc_lower for k in ['review', 'debug', 'investigate']):
        return 'Review'
    if any(k in desc_lower for k in ['test', 'browser', 'qa', 'dogfood']):
        return 'Test'
    if any(k in desc_lower for k in ['ship', 'deploy', 'pr', 'release', 'doc']):
        return 'Ship'

    return 'Other'


def slash_name(skill_name: str) -> str:
    """Convert skill dir name to slash command (strip gstack- prefix)."""
    if skill_name.startswith('gstack-'):
        return '/' + skill_name[7:]
    if skill_name == 'gstack':
        return '/gstack'
    return '/' + skill_name


def generate(gstack_path: str, output_dir: str):
    skills_dir = Path(gstack_path) / '.agents' / 'skills'

    if not skills_dir.exists():
        print(f"ERROR: {skills_dir} not found", file=sys.stderr)
        sys.exit(1)

    skills = []

    for skill_dir in sorted(skills_dir.iterdir()):
        if not skill_dir.is_dir():
            continue

        skill_md = skill_dir / 'SKILL.md'
        if not skill_md.exists():
            continue

        content = skill_md.read_text(encoding='utf-8')
        frontmatter = extract_frontmatter(content)
        sections = extract_sections(content)

        name = frontmatter.get('name', skill_dir.name)
        description = frontmatter.get('description', '')
        if isinstance(description, str):
            desc_oneline = description.strip().split('\n')[0].strip()
        else:
            desc_oneline = str(description)

        size_bytes = len(content.encode('utf-8'))
        phase = classify_phase(skill_dir.name, description if isinstance(description, str) else '')

        skills.append({
            'dir_name': skill_dir.name,
            'name': name,
            'slash': slash_name(skill_dir.name),
            'description': description.strip() if isinstance(description, str) else str(description),
            'description_oneline': desc_oneline[:200],
            'phase': phase,
            'size_bytes': size_bytes,
            'sections': sections,
            'has_scripts': (skill_dir / 'scripts').exists(),
            'has_references': (skill_dir / 'references').exists(),
            'has_assets': (skill_dir / 'assets').exists(),
        })

    # Build index JSON
    index = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'gstack_source': 'https://github.com/garrytan/gstack',
        'skill_count': len(skills),
        'skills': skills,
    }

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    with open(output_path / 'skill-index.json', 'w') as f:
        json.dump(index, f, indent=2)

    # Build markdown catalog
    phases_order = ['Think', 'Review', 'Test', 'Ship', 'Safety', 'Meta', 'Other']
    by_phase = {}
    for s in skills:
        by_phase.setdefault(s['phase'], []).append(s)

    lines = [
        '# gstack Skills Catalog',
        '',
        f'> Auto-generated from [garrytan/gstack](https://github.com/garrytan/gstack)',
        f'> {len(skills)} skills | Generated: {datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")}',
        '',
        '## Quick Reference',
        '',
        '| Phase | Skill | Description | Size |',
        '|-------|-------|-------------|------|',
    ]

    for phase in phases_order:
        for s in by_phase.get(phase, []):
            size_kb = f"{s['size_bytes'] / 1024:.0f}KB"
            lines.append(f"| {phase} | `{s['slash']}` | {s['description_oneline'][:80]} | {size_kb} |")

    lines.append('')
    lines.append('---')
    lines.append('')

    for phase in phases_order:
        phase_skills = by_phase.get(phase, [])
        if not phase_skills:
            continue

        lines.append(f'## Phase: {phase}')
        lines.append('')

        for s in phase_skills:
            lines.append(f"### `{s['slash']}` ({s['dir_name']})")
            lines.append('')
            lines.append(f"**Size:** {s['size_bytes']:,} bytes")
            lines.append('')

            # Description (first paragraph)
            desc_lines = s['description'].split('\n')
            for dl in desc_lines[:5]:
                if dl.strip():
                    lines.append(dl.strip())
            lines.append('')

            if s['sections']:
                lines.append('**Key sections:** ' + ', '.join(s['sections'][:6]))
                lines.append('')

            extras = []
            if s['has_scripts']:
                extras.append('scripts/')
            if s['has_references']:
                extras.append('references/')
            if s['has_assets']:
                extras.append('assets/')
            if extras:
                lines.append('**Bundled:** ' + ', '.join(extras))
                lines.append('')

            lines.append('---')
            lines.append('')

    with open(output_path / 'skills-catalog.md', 'w') as f:
        f.write('\n'.join(lines))

    print(f"Generated catalog: {len(skills)} skills")
    print(f"  → {output_path / 'skill-index.json'}")
    print(f"  → {output_path / 'skills-catalog.md'}")


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <gstack-repo-path> <output-dir>")
        sys.exit(1)

    generate(sys.argv[1], sys.argv[2])
