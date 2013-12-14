#!/usr/bin/env python

"""
This script can check whether a file was last modified before a time X. If it was modified after that,
an error is raised. It can also check, whether the file contains
 a specific string (e.g. "exit 0"). If it's not there, an error is raised.

 Example:
 check_exit_code.py --exitcode -t 20 /path/to/logfile
"""

import os
import argparse
import time
import re

# Parse arguments
parser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument("logfile", help="Specify the logfile to monitor.")
parser.add_argument("-t", "--time", help="Time in minutes which a log file can be unmodified before raising CRITICAL"
                                         " alert.", type=int)
parser.add_argument("--exitcode", help="If specified, check if \"exit 0\" exists in logfile.", action="store_true")

args = parser.parse_args()

if not (args.time or args.exitcode):
    print "At least one argument (--time, --exitcode) is required."
    exit(2)

#variables
log = args.logfile

# Check if file exists and is readable by user
try:
    f = open(log)
except IOError:
    print "Cannot open the file. Check if it exists and you have the right permissions to open it."
    exit(1)

# check exit code
if args.exitcode:
    logfile = f.read()
    if not re.search("exit 0", logfile, flags=re.I):
        print "CRITICAL: Exit code not found in File %s" % log
        exit(2)

# Check last file modification time
if args.time:
    # File Modification time in seconds since epoch
    file_mod_time = os.stat(log).st_mtime

    # Time in seconds since epoch for time, in which logfile can be unmodified.
    t = time.time()
    should_time = t - (args.time * 3600)

    # Time in minutes since last modification of file
    last_time = (t - file_mod_time) / 60

    if last_time > args.time:
        print "CRITICAL: {} last modified {:.2f} minutes. Threshold set to {:.2f} minutes".format(log, last_time,
                                                                                                  args.time)
        exit(2)

# If nothin went wrong, print OK and exit.
print "OK. Exitcode found or last modification time not exceeded."
exit(0)