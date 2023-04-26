#include <stdlib.h>
#include <stdio.h>

int main(int argc, char* argv[]){
    int a[3] = {0};
    int b[3] = {1};
    // int n;
    // scanf("%d", &n);  //a[8]會出問題
    for(int i=0;i<3;i++){
        b[i] = 1;
        a[i] = 0;
    }
    printf("address of a[8] is %p, which normally equals to b[0]:%p\n", &a[8], &b[0]);
    a[8] = 0;
    printf("b[0] = %d\n",b[0]);
    return 0;
}
