import re
from pathlib import Path

def check_links(directory: Path):
    link_re = re.compile(r"\[[^\]]+\]\([^\)]+\)")
    back_re = re.compile(r"\[Back\]\([^\)]+\)", re.IGNORECASE)
    flagged = []
    ignored = {"_Footer.md", "README.md", "Home.md", "tmp.md"}
    for md_file in sorted(directory.glob('*.md')):
        if md_file.name in ignored:
            continue
        text = md_file.read_text(encoding='utf-8')
        links = link_re.findall(text)
        has_links = bool(links)
        has_back = bool(back_re.search(text))
        if not has_links or not has_back:
            flagged.append((md_file, not has_links, not has_back))
    return flagged

if __name__ == '__main__':
    flagged = check_links(Path('.'))
    if flagged:
        print('Flagged files:')
        for f, no_links, no_back in flagged:
            reasons = []
            if no_links:
                reasons.append('no outbound links')
            if no_back:
                reasons.append('missing [Back] footer')
            print(f" - {f}: {', '.join(reasons)}")
    else:
        print('All files have outbound links and [Back] footer.')
