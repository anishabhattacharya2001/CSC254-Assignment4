import sys 
from subprocess import call
import os
import re
import collections
import datetime

#find time taken to run
running = str(datetime.datetime.now())
obj_file = open('objdumpoutput.txt', 'w')
call(["objdump", "-d", sys.argv[1]], stdout = obj_file )
obj_file.close()
llvm_file = open('llvmoutput.txt', 'w')
call(["llvm-dwarfdump", "--debug-line", sys.argv[1]], stdout= llvm_file)
llvm_file.close()
hexa_Pattern = re.compile("(\d|a|b|c|d|e|f){16}")
hexa = re.compile("0x[0-9a-f]{16}")
small_hexa = re.compile("[0-9a-f]")

#need to take care of multiple files
#find the file names that exist
filename = []
fileandtable = {}
#this is a dictionary that will hold the file name and the corresponding llvmdwarfdump table
flag = 0
tablecontent = ""
fn = ""
with open('llvmoutput.txt', 'r+') as f:
    lines = f.readlines()
    for i in range(0, len(lines)):
        line = lines[i]
        if flag == 1:
            tablecontent +=line

        if line == "file_names[  0]:\n":
            if flag == 1:
                fileandtable[fn] = tablecontent
                flag = 2
            flag = 1
            tablecontent = ""
            nex = lines[i + 1]
            parts = nex.split()
            fn = parts[1].replace('"', '')
            filename.append(fn)
        
        if i == len(lines)-1:
            fileandtable[fn] = tablecontent          

arrTables = []
for tab in arrTables:
    print("FILE START")
    print(tab)

#put the dwarfdump output of each file into a separate text file
for i in range( len(filename) ):
    file = open(filename[i]+"output.txt", "w")
    file.writelines(fileandtable.get(filename[i]))
    arrTables.append(fileandtable.get(filename[i]))

hex_and_func_regex = re.compile("[0-9a-f]{16}\s<.+>:")

def everything(filen, n):
    # dictionaries 
    hexa_to_linenum = {}
    linenum_to_hex = {}

    for i in range(len(arrTables)):
        table = arrTables[i]
        if i==n:
            line = table.splitlines()
            for l in line:
                parts = l.split()
                if(len(parts) > 0):
                    if(hexa.match(parts[0])):
                        key = parts[0].replace('0x', '')
                        hexa_to_linenum[key.lstrip('0')] = parts[1]
                        linenum_to_hex[parts[1]] = key.lstrip('0')
            
    list_hexa = sorted(hexa_to_linenum)


    line_to_assembly = {}
    #dict with line number to the assembly code
    with open('objdumpoutput.txt', 'r') as read_file:
        for line in read_file:
            parts = line.split()
            if(len(parts) > 0):
                key = parts[0].replace(':', '')
                if(key in hexa_to_linenum ):
                    line_to_assembly[hexa_to_linenum.get(key)] = parts


    Assembly = {}
    with open('objdumpoutput.txt', 'r') as read_file:
        for line in read_file:
            parts = line.split()
            if(len(parts) > 0):
                if(small_hexa.match(parts[0])):
                    key = parts[0].replace(':', '')
                    Assembly[key] = line
    Assembly_Addresses = sorted(Assembly)

    # creating a dict with line and the range
    assembly_Array = {}
    for i in range( len(list_hexa) - 1 ):
        nlist = [list_hexa[i], list_hexa[i + 1] ]
        assembly_Array[ hexa_to_linenum.get(list_hexa[i]) ] = nlist

    # creating the dict with C line and the associated Assembly code
    Line_to_Addresses = {}
    for key in assembly_Array :
        _range = assembly_Array.get(key)
        start = _range[0]
        end = _range[1]
        ek_list = []
        for i in range( len(Assembly_Addresses) ):
            if(Assembly_Addresses[i] >= start and Assembly_Addresses[i] < end ):
                ek_list.append(Assembly_Addresses[i])
        Line_to_Addresses[key] = ek_list

    line_to_cCode = {}
    i = 1
    with open(filen, 'r') as read_file:
        for line in read_file:
            if(line != '\n'):
                line_to_cCode[i] = line
            i = i + 1 

    # # FINAL C CODE to Assembly code 
    Final_C_to_Assembly = {}
    i = 1
    with open(filen, 'r') as read_file:
        for line in read_file:
            answer = []
            if(not(str(i) in Line_to_Addresses)):
                if(line != "\n"):
                    answer.append("No Assembly code reference found for this source")      
            else:
                list = Line_to_Addresses.get(str(i))
                for j in range(len(list)):
                    answer.append(Assembly.get(list[j]))
            if(len(answer) != 0):
                Final_C_to_Assembly[line_to_cCode.get(i)] = answer
            i = i + 1   


    # Function to convert   
    def listToString(lis):    
        s = ""
        if(lis == "No Assembly code reference found for this source"):
            return "No Assembly code reference found for this source"
        for ele in lis:  
            s += ele
            s += " "        
        return s

    small_hexa_col = re.compile("[0-9a-f]:")
    def func_Div(ass):
        A = ass.split()
        retString = ''
        if(small_hexa.match(A[0])):
            stringg = '<div id=' + A[0] + '>' + A[0] + '</div>'
            A[0] = stringg
            retString = " ".join(A)
            return retString
        else:
            return ass

    control_flow = ["jmp", "je", "jne", "jz", "jg", "jge", "jl", "jle", "callq"]
    def func_href(abss):
        retString = ''
        for cf in control_flow:
            if cf in abss:
                A = abss.split()
                for i in range(len(A)):
                    if(A[i] == cf):
                        something = '<a href= \" #' + A[i + 1] + ':\">' + A[i + 1] + '</a>'
                        A[i + 1] = something
                        retString = " ".join(A)
                        return retString     
        return abss 

    path = os.path.dirname(os.path.realpath(__file__))
    fileout = open(filen+"index.html", "w")
    htmlcode = "<html> \n <style>\n"
    htmlcode += "table, th, td {border:1px solid black;}\n </style>"
    htmlcode += "<hr>\n"
    htmlcode += "  Time Ran: "+running+ "<br>"
    htmlcode += "  Location: "+path+"<br>"
    htmlcode += "<body>\n <h1>Disassemble<h1>"

    # Create table
    table = "<table style=\"width:100%\">  \n"
    table += "  <tr>\n"
    table += "  <th>source</th>\n"
    table += "  <th>assembly</th>\n"
    table += "  </tr>\n"
    for key, value in Final_C_to_Assembly.items():
        table += " <tr> \n"
        table += "  <td>"+key+" </td> \n"
        ass = " <td>"
        for assemblyLine in value:
            abss = func_Div(assemblyLine)
            abb = func_href(abss)
            ass += abb
            ass += '\n<br>'
        ass += "</td>"
        table += ass
        table += "  </tr>\n"
    table += "</table>"
    htmlcode += table
    htmlcode += "</body> \n </html>"
    fileout.writelines(htmlcode)
    fileout.close()


for i in range(len(filename)):
    filen = filename[i]
    everything(filen, i)