#!/usr/bin/env python

"""
Checks the exit code provided in a logfile.
Checks the last run time of a script.
"""

import os
import argparse
import time
import datetime

parser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument("logfile", help="Specify the logfile to monitor.")
parser.add_argument("-e", "--exitcode", help="Specify the accepted exit codes.", nargs="+", type=int)
parser.add_argument("-t", "--time", help="Set the time in seconds how often the script to monitor runs.", type=int)

args = parser.parse_args()
logfile = args.logfile

# Check if file exists and is readable by user

try:
    f = open(logfile)
except IOError:
    print "Cannot open the file. Check if it exists and you have the right permissions to open it."
    exit(1)


# Check if exit-code contains "0", otherwise add it to list of exitcodes
exit_code = args.exitcode

#TODO CHECK HERE
if 0 not in args.exitcode:
    exit_code = [0]
    exit_code += args.exitcode

opt_time = args.time
#last_exec_time = datetime.datetime.now() - os.path.getmtime(logfile)

statbuf = os.stat(logfile).st_mtime

print datetime.timedelta(seconds=time.time() - statbuf)

#if last_exec_time > opt_time:
#    print "CRITICAL:", logfile, "last modified", last_exec_time, "minutes, "