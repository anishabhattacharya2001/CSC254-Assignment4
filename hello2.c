#include "hello2.h"

int add(int a, int b){
    int sum = a+b;
    return sum;
}

int max(int a, int b){
    if( a > b){
        return a;
    }
    else{
        return b;
    }
}