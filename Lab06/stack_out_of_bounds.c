#include <stdlib.h>
#include <stdio.h>

int main(int argc, char* argv[]){
    int staticVar[10];
    //staticVar[10]=1;  //can not assign
    printf("%d",staticVar[10]);
    return staticVar[10];
}
