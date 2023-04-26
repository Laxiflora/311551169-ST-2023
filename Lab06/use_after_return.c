#include <stdlib.h>
#include <stdio.h>
int* ptr;
void foo(){
    int die[10] = {1};
    ptr = die;
    //return &die[2];
}

int main(int argc, char* argv[]){
    foo();
    *ptr = 1;
    printf("%d",*ptr);
}