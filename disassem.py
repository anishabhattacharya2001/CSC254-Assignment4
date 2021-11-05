import sys from subprocess import call
import os
import re


# need to run "objdump ‑d hello"
# and run "llvm-dwarfdump --debug-line hello"
#store their output in text file


f = open('objdumpoutput.txt', 'w')
call(["objdump", "-d", sys.argv[1]], stdout=f)
f.close()

f = open('llvmoutput.txt', 'w')
call(["llvm-dwarfdump", "--debug-line", sys.argv[1]], stdout=f)
f.close()