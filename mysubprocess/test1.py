#!/usr/bin/env python

import subprocess

lst = [
    "ls -l /home/xiaohao",
    "pwd",
]


def run1():
    for cmd in lst:
        subprocess.Popen(cmd.split(" "))


def run2():
    for cmd in lst:
        res = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        print("-------%s------" % cmd)
        print(res.stdout.read())
        res.stdout.close()


def run3():
    tasks = []
    for cmd in lst:
        worker = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # worker = subprocess.Popen(cmd.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        tasks.append((cmd, worker))

    for cmd, worker in tasks:
        worker.wait()
        print("-------[%s]------" % cmd)
        print(worker.stdout.read())


run1()

print()
print()

run2()

print()
print()

run3()

