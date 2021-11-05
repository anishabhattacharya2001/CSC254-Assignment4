import sys 
from subprocess import call
import os
import re

obj_file = open('objdumpoutput.txt', 'w')
call(["objdump", "-d", sys.argv[1]], stdout = obj_file )
obj_file.close()

llvm_file = open('llvmoutput.txt', 'w')
call(["llvm-dwarfdump", "--debug-line", sys.argv[1]], stdout= llvm_file)
llvm_file.close()