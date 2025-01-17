#!/usr/bin/env python3

from pathlib import Path

# directories to collection of file extensions
INV_EXTS = {
    "~/Books": [".pdf"],
    "~/Photos": [".jpg", ".jpeg", ".heic"],
    "~/Text": [".txt"],
}

# Convert to a dictionary mapping file extension to directory
EXTS = {
    ext: Path(dest).expanduser()
    for dest, exts in INV_EXTS.items()
    for ext in exts
}


def move_file(p: Path, dest: Path): 
    print(f'mv "{str(p)}" "{str(dest)}/."')


def filer():
    for p in Path('.').glob('*'):
        if p.is_file() and (destination := EXTS.get(p.suffix)):
            move_file(p, destination)


if __name__ == '__main__':
    filer()
