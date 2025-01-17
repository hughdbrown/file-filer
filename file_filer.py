#!/usr/bin/env python3

from pathlib import Path


def move_file(p: Path, dest: Path): 
    print(f'mv "{str(p)}" "{str(dest)}/."')


def filer():
    inv_exts = {
        "~/Books": [".pdf"],
        "~/Photos": [".jpg", ".jpeg", ".heic"],
    }
    exts = {
        ext: Path(dest).expanduser()
        for dest, exts in inv_exts.items()
        for ext in exts
    }

    for p in Path('.').glob('*'):
        if p.is_file() and (destination := exts.get(p.suffix)):
            move_file(p, destination)

if __name__ == '__main__':
    filer()
