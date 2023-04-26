#include <stdlib.h>
#include <stdio.h>
int someGlobVar[10];

int main(int argc, char* argv[]){
    someGlobVar[10]=1;
    printf("%d",someGlobVar[10]);
    return 0;
}
