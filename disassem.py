import sys 
from subprocess import call
import os
import re
import collections

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
                hexa_to_linenum[key.lstrip('0')] = parts[1]
                linenum_to_hex[parts[1]] = key.lstrip('0')
list_hexa = sorted(hexa_to_linenum)
#creating dictionary from source code of c to line number
sourceC_to_line = {}
i = 1
with open('hello.c', 'r') as read_file:
    for line in read_file:
        sourceC_to_line[i] = line
        i = i + 1
        
#print(hexa_to_linenum)
line_to_assembly = {}

# dict with line number to the assembly code
# with open('objdumpoutput.txt', 'r') as read_file:
#     for line in read_file:
#         parts = line.split()
#         if(len(parts) > 0):
#             key = parts[0].replace(':', '')
#             if(key in hexa_to_linenum ):
#                 line_to_assembly[hexa_to_linenum.get(key)] = parts

Assembly = {}
with open('objdumpoutput.txt', 'r') as read_file:
    for line in read_file:
        parts = line.split()
        if(len(parts) > 0):
            # print(parts)
            key = parts[0].replace(':', '')
            Assembly[key] = parts
Assembly_Addresses = sorted(Assembly)

# dict for souce to assembly 
cSource_to_Assembly = {}
for key in line_to_assembly :
    cSource_to_Assembly[key] = line_to_assembly[key] 


assembly_Array = []

for i in range( len(list_hexa) - 1 ):
    nlist = [list_hexa[i], list_hexa[i + 1], hexa_to_linenum.get(list_hexa[i]) ]
    assembly_Array.append(nlist)




        
        
    