#!/usr/bin/env python3

import subprocess as sb
from os import chdir
from os.path import expanduser

pool = ""
wallet = "" 
machine_id = ""

# change if installer script was not run in home directory
path = "/xmrig/build"
home = expanduser("~") # ~ does not work in chdir(), this will return the home directory path

full_path = home + path
chdir(full_path)

sb.call(f"./xmrig -o {pool} -u {wallet} -p {machine_id}", shell=True)

