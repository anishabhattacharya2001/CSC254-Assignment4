import os
import re
from subprocess import call

# need to run "objdump ‑d hello"
# and run "llvm-dwarfdump --debug-line hello"
f = open('objdumpoutput.txt', 'w')
call(["objdump", "-d", "hello"], stdout=f)
f.close()

f = open('llvmoutput.txt', 'w')
call(["dwarfdump", "hello"], stdout=f)
f.close()