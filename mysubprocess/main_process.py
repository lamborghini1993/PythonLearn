#!/usr/bin/env python

import subprocess
import shlex

shell_cmd = "python3 child_process.py"
cmd = shlex.split(shell_cmd)
print(cmd)
p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

while p.poll() is None:
    line = p.stdout.readline()
    print("child process output:[{}]".format(line))
if p.returncode == 0:
    print("success")
else:
    print("failed")

