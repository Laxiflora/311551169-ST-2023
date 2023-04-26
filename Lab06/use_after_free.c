#include <stdlib.h>
#include <stdio.h>

int main(int argc, char* argv[]){
    int* someVar = malloc(sizeof(int)*10);
    *(someVar+3) = 1;
    printf("%d\n", *(someVar+3));
    printf("%p\n", (someVar+3));
    free(someVar);
    printf("%d\n",*(someVar+3));
    printf("%p\n", (someVar+3));
    return 0;
}