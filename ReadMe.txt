Anisha Bhattacharya (abhatta9)
Piyush Saini (psaini2)

CSC254 - Assignment4

To run this file first run (you can try -g0)
gcc -g3 -o myprogram myfile1.c myfile2.c ... 
And then
Python disassem.py myprogram

For each file that you have created there will be a separate html file created corresponding to its name. The webpage contains side-by-side assembly language and corresponding source code for a given program in a table. 

The output of commands llvm-dwarfdump and objdump ‑d  is stored in a text file and using the table of line to assembly code we look into object dump to find the range of commands associated with a particular instruction. 

There is a separate array created for each file's llvm table content to separate the information.

For each address in the objdump we have added an id to it and anytime there is a callq or jmp (or other control flow instructions) an href tag is added to which makes it jump to the address required.

