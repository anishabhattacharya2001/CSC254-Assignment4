import os
import re
from subprocess import call

f = open('objdumpoutput.txt', 'w')
call(["objdump", "-d", "hello"], stdout=f)
f.close()

f = open('llvmoutput.txt', 'w')
call(["dwarfdump", "hello"], stdout=f)
f.close()