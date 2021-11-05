import sys from subprocess import call
import os
import re


# need to run "objdump ‑d hello"
# and run "llvm-dwarfdump --debug-line hello"
#store their output in text file

# if(len(sys.argv) != 2):
#     print("found " + str(len(sys.argv)) + " arguments when we expect two.")
#     exit(1)

f = open('objdumpoutput.txt', 'w')
call(["objdump", "-d", sys.argv[1]], stdout=f)
f.close()

f = open('llvmoutput.txt', 'w')
call(["llvm-dwarfdump", sys.argv[1]], stdout=f)
f.close()