#include <stdlib.h>
#include <stdio.h>

int* foo(){
    int die = 32;
    return &die;
}

int main(int argc, char* argv[]){
    int* ptr;
    ptr = foo();
    printf("%d",*ptr);
}