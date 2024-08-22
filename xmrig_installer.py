#!/usr/bin/env python3

import subprocess as sb
from os import chdir

sb.call("sudo apt update", shell=True)
sb.call("sudo apt install git build-essential cmake libuv1-dev libssl-dev libhwloc-dev -y", shell=True)
sb.call("git clone https://github.com/xmrig/xmrig.git", shell=True)
chdir("xmrig")
sb.call("mkdir build", shell=True)
chdir("build")
sb.call("cmake ..", shell=True)
sb.call("make", shell=True)

