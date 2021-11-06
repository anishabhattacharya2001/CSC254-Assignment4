/* function returning the max between two numbers */
#include "hello2.h"
int max(int num1, int num2) {
   int result;
   if (num1 > num2)
      result = num1;
   else
      result = num2;
   return result; 
}
int add(int num1, int num2)
{
    int sum = num1 + num2;
    return sum;
}