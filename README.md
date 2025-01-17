# Purpose
Move files in the current directory to archive locationis based on their file extension / file type.

# Usage
The script does not actually move the files. It prints out the shell command to move files to their desired location. this makes it possible to review the commands before executed.

To move the files, pipe the program output through a linux shell like `bash` or `sh`:
```
$ file_filer.py | sh
``` 
