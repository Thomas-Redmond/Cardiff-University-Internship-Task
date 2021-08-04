import sys
import os

filename = sys.argv[1]
address = os.getcwd()
sys.path.append(address)
Squash = __import__(filename)
