"""Export upstream development skills for the plugin's fixed skills location."""
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
    return result


def package_skills(plugin):
    root = plugin / 'skills'
    for path in root.iterdir():
        if path.is_dir() and path.name != 'reverse-engineer-anything':
            shutil.rmtree(path)
    for relative, data in exported_skills(plugin).items():
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
