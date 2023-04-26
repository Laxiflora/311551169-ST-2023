#include <stdlib.h>
#include <stdio.h>

int main(int argc, char* argv[]){
    int* someVar = malloc(sizeof(int)*10);
    *(someVar+3) = 1;
    printf("%d",*(someVar+3));
    free(someVar);
    printf("%d",*(someVar+3));
    return 0;
}