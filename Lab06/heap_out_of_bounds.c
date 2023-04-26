#include <stdlib.h>
#include <stdio.h>

int main(int argc, char* argv[]){
    int* someVar = malloc(sizeof(int)*10);
    //*(someVar+10) = 1;
    //printf("%d",*(someVar+10));
    int boom = someVar[100];
    free(someVar);
    return 0;
}
