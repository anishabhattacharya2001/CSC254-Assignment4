import os
import re
import sys
from subprocess import call

# need to run "objdump ‑d hello"
# and run "llvm-dwarfdump --debug-line hello"
#store their output in text file

if(len(sys.argv) != 2):
    print("found " + str(len(sys.argv)) + " arguments when we expect two.")
    exit(1)

executable_name = sys.argv[1]

f = open('objdumpoutput.txt', 'w')
call(["objdump", "-d", executable_name], stdout=f)
f.close()

f = open('llvmoutput.txt', 'w')
call(["llvm-dwarfdump", executable_name], stdout=f)
f.close()