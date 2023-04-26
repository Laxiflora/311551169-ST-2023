#include <stdlib.h>
#include <stdio.h>

int main(int argc, char* argv[]){
    int staticVar[10];
    staticVar[3]=1;
    printf("%d",staticVar[3]);
    return 0;
}
