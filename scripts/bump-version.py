#!/usr/bin/env python3
"""
Bump skill version in SKILL.md and progress template when gstack changes are detected.
Reads current version from skill-index.json metadata, bumps patch.
"""

import json
import re
import sys
from pathlib import Path


def bump(version_str: str) -> str:
    """Bump patch version: 0.1.2 -> 0.1.3"""
    parts = version_str.split('.')
    parts[-1] = str(int(parts[-1]) + 1)
    return '.'.join(parts)


def main():
    repo_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('.')

    # Read current version from version.json
    version_file = repo_root / 'version.json'
    if version_file.exists():
        data = json.loads(version_file.read_text())
        current = data.get('version', '0.1.0')
    else:
        current = '0.1.0'
        data = {}

    new_version = bump(current)

    # Update version.json
    data['version'] = new_version
    version_file.write_text(json.dumps(data, indent=2) + '\n')

    # Update SKILL.md if it references version
    skill_md = repo_root / 'SKILL.md'
    if skill_md.exists():
        content = skill_md.read_text()
        # Update any version references in the file
        content = re.sub(
            r'gstack-course v[\d.]+',
            f'gstack-course v{new_version}',
            content
        )
        skill_md.write_text(content)

    print(f"{current} → {new_version}")
    return new_version


if __name__ == '__main__':
    main()
