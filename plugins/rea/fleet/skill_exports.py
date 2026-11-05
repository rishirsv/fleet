"""Assemble upstream exports and Fleet-owned skills for portable discovery."""
import re
import shutil


def exported_skills(plugin):
    result = {}
    original = plugin / '.agents/skills'
    for path in original.rglob('*'):
        relative = path.relative_to(original)
        if not path.is_file() or relative.parts[0] == 'reverse-engineer-anything':
            continue
        data = path.read_bytes()
        if path.suffix == '.md':
            # .agents/skills/<name> -> skills/<name> removes one directory.
            data = re.sub(rb'(?<=\]\()\.\./(?=(?:\.\./){2})', b'', data)
        result[relative] = data
    wrappers = plugin / 'fleet/skills'
    for skill in wrappers.iterdir() if wrappers.exists() else ():
        if not skill.is_dir():
            continue
        if skill.name == 'reverse-engineer-anything' or (original / skill.name).exists():
            raise RuntimeError(f'Fleet skill collides with upstream skill: {skill.name}')
        for path in skill.rglob('*'):
            if path.is_file():
                result[path.relative_to(wrappers)] = path.read_bytes()
    return result


def package_skills(plugin):
    exports = exported_skills(plugin)
    root = plugin / 'skills'
    root.mkdir(exist_ok=True)
    for path in root.iterdir():
        if path.is_dir() and path.name != 'reverse-engineer-anything':
            shutil.rmtree(path)
    for relative, data in exports.items():
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
