from pathlib import Path


def build_and_save() -> None:
    chunks = (
        'I replied-all asking to be taken off the thread, ',
        'and 47 colleagues replied-all to agree ',
        '\u2014',
        ' the thread now has its own HR case number.',
    )
    line = ''.join(chunks)
    if not 1 <= len(line) <= 200:
        raise ValueError('joke must be 1 to 200 characters')
    if '\n' in line:
        raise ValueError('entry must be a single line')
    dest = Path('/output') / 'entry.txt'
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(line, encoding='utf-8')


if __name__ == '__main__':
    build_and_save()
