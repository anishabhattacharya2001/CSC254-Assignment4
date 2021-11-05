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

hexa = re.compile("0x[0-9a-f]{16}")


# dictionaries 
hexa_to_linenum = {}
linenum_to_hex = {}
with open('llvmoutput.txt', 'r') as read_file:
    for line in read_file:
        parts = line.split()
        if(len(parts) > 0):
            if(hexa.match(parts[0])):
                key = parts[0].replace('0x', '')
                hexa_to_linenum[key] = parts[1]
                linenum_to_hex[parts[1]] = key

                
                
        
        
    