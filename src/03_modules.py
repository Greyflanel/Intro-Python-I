import sys
print('Length of sys.argv :', len(sys.argv))
print('Argument(s)  :', str(sys.argv))

import platform
print('OS Platform  :', sys.platform)
print('Python Version  :', platform.python_version())

import os
print('Current Process ID :', os.getpid())
print('Current Working Directory  :', os.getcwd())

import getpass
print('Current login name  :', getpass.getuser())