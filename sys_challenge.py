import os
import platform
import sys
import getpass

print("Operating System Name:", platform.system(), platform.release())
print("Current Username:", getpass.getuser())
print("Current Working Directory:", os.getcwd())
print("Python Version:", sys.version.split()[0])