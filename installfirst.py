import os

# Check if program is run as root, else exit.
# Root is needed to power off the computer.
if not os.geteuid() == 0:
	import sys
	sys.exit("\n[ERROR] This program needs to run as root.\n")

import killswitch
killswitch.go()
