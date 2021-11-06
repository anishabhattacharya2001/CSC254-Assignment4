#include <stdio.h>
#include "hello2.h"

int factorial(int number);
int fibonacci(int i);

int main() {
   printf("Hello, world!");
   factorial(10);
   fibonacci(10);
   int maxval = max(10, 20);
   int sum = add(10, 20);
   return 0;
}

//this method calculates facorial of the integer sent to it
int factorial(int number){    
 int i;
 int f = 1;  
    for(i=1;i<=number;i++){    
      f=f*i;    
  }    
  printf("Factorial of %d is: %d",number,f);    
return 0;  
}  

//this is a recursive program for fibonacci sequence
int fibonacci(int i) {
   if(i == 0) {
      return 0;
   }	
   if(i == 1) {
      return 1;
   }
   return fibonacci(i-1) + fibonacci(i-2);
}


