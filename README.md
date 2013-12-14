check_exit-code
===============

This script can check whether a file was last modified before a time X. If it was modified after that, an error is raised. It can also check, whether the file contains  a specific string (e.g. "exit 0"). If it's not there, an error is raised.

Example:

```check_exit_code.py --exitcode -t 20 /path/to/logfile/```
