#!/usr/bin/python
from subprocess import call
import sys
cmd="python3 scheme_grader.py -q "
if len(sys.argv) > 1:
    cmd+=sys.argv[1]
call(cmd,shell=True)
