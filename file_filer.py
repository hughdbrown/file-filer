#!/usr/bin/env python3

from pathlib import Path

# directories to collection of file extensions
INV_EXTS = {
    "~/Books": [".pdf"],
    "~/Images": [".jpg", ".jpeg", ".heic", ".png", ".gif"],
    "~/Text": [".txt"],
    "~/Videos": [".mp4", ".mkv"],
}

# Convert to a dictionary mapping file extension to directory
EXTS = {
    ext: Path(dest).expanduser()
    for dest, exts in INV_EXTS.items()
    for ext in exts
}


def move_file(p: Path, dest: Path): 
    """ Write a shell command to move the file. """
    print(f'mv "{str(p)}" "{str(dest)}/."')


def filer(start_dir="."):
    """ Move all files that match a known extension. """
    for p in Path(start_dir).glob('*'):
        # Move only files that have a known file extension
        if p.is_file() and (destination := EXTS.get(p.suffix)):
            move_file(p, destination)


if __name__ == '__main__':
    filer()
