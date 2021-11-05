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

hexa_Pattern = re.compile("(\d|a|b|c|d|e|f){16}")


#QuizList = []
with open('llvmoutput.txt', 'r') as read_file:
    for line in read_file:
        parts = line.split()
        print(len(parts))
        if len(parts) > 0:
            if hexa_Pattern.match(parts[0]):
                print("uyyyyyy")
    