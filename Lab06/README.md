# 軟體測試Lab06

## 比較圖
|Program             |Valgrind|ASan                        |
|--------------------|--------|----------------------------|
|Stack_out_of_bounds |N       |Y                           |
|Global_out_of_bounds|N       |Y                           |
|Heap_out_of_bounds  |Y       |Y                           |
|Use_after_return    |N       |Y(with environment variable)|
|Use_after_free      |Y       |Y                           |
## Stack_out_of_bounds

### Code
```
#include <stdlib.h>
#include <stdio.h>

int main(int argc, char* argv[]){
    int staticVar[10];
    //staticVar[10]=1;  //can not assign
    printf("%d",staticVar[10]);
    return staticVar[10];
}

```

### ASan report
```
==16666==ERROR: AddressSanitizer: stack-buffer-overflow on address 0x7faed054d058 at pc 0x563107580311 bp 0x7ffd094d0ee0 sp 0x7ffd094d0ed0
READ of size 4 at 0x7faed054d058 thread T0
    #0 0x563107580310 in main (/home/laxiflora/311551169-ST-2023/Lab06/stack_out_of_bounds+0x1310)
    #1 0x7faed3bead8f in __libc_start_call_main ../sysdeps/nptl/libc_start_call_main.h:58
    #2 0x7faed3beae3f in __libc_start_main_impl ../csu/libc-start.c:392
    #3 0x563107580164 in _start (/home/laxiflora/311551169-ST-2023/Lab06/stack_out_of_bounds+0x1164)

Address 0x7faed054d058 is located in stack of thread T0 at offset 88 in frame
    #0 0x563107580238 in main (/home/laxiflora/311551169-ST-2023/Lab06/stack_out_of_bounds+0x1238)

  This frame has 1 object(s):
    [48, 88) 'staticVar' (line 5) <== Memory access at offset 88 overflows this variable
HINT: this may be a false positive if your program uses some custom stack unwind mechanism, swapcontext or vfork
      (longjmp and C++ exceptions *are* supported)
SUMMARY: AddressSanitizer: stack-buffer-overflow (/home/laxiflora/311551169-ST-2023/Lab06/stack_out_of_bounds+0x1310) in main
Shadow bytes around the buggy address:
  0x0ff65a0a19b0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ff65a0a19c0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ff65a0a19d0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ff65a0a19e0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ff65a0a19f0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0ff65a0a1a00: f1 f1 f1 f1 f1 f1 00 00 00 00 00[f3]f3 f3 f3 f3
  0x0ff65a0a1a10: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ff65a0a1a20: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ff65a0a1a30: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ff65a0a1a40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ff65a0a1a50: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:       fa
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
  Shadow gap:              cc
==16666==ABORTING
```
Stack buffer overflow

### Valgrind report
```
==16758== Memcheck, a memory error detector
==16758== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.
==16758== Using Valgrind-3.18.1 and LibVEX; rerun with -h for copyright info
==16758== Command: ./stack_out_of_bounds
==16758== 
-313154048==16758== 
==16758== HEAP SUMMARY:
==16758==     in use at exit: 0 bytes in 0 blocks
==16758==   total heap usage: 1 allocs, 1 frees, 1,024 bytes allocated
==16758== 
==16758== All heap blocks were freed -- no leaks are possible
==16758== 
==16758== For lists of detected and suppressed errors, rerun with: -s
==16758== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)
```
抓不到錯


### 結論
ASan: 能
Valgrind: 不能


## global_out_of_bounds
### Code
```
#include <stdlib.h>
#include <stdio.h>
int someGlobVar[10];

int main(int argc, char* argv[]){
    someGlobVar[10]=1;
    printf("%d",someGlobVar[10]);
    return 0;
}
```

### ASan report
```
SUMMARY: AddressSanitizer: global-buffer-overflow (/home/laxiflora/311551169-ST-2023/Lab06/global_out_of_bounds+0x122d) in main
Shadow bytes around the buggy address:
  0x0ab226ec8dd0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ab226ec8de0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ab226ec8df0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ab226ec8e00: 00 00 00 00 00 00 00 00 f9 f9 f9 f9 f9 f9 f9 f9
  0x0ab226ec8e10: f9 f9 f9 f9 f9 f9 f9 f9 00 00 00 00 00 00 00 00
=>0x0ab226ec8e20: 00[f9]f9 f9 f9 f9 f9 f9 00 00 00 00 00 00 00 00
  0x0ab226ec8e30: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ab226ec8e40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ab226ec8e50: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ab226ec8e60: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ab226ec8e70: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:       fa
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
  Shadow gap:              cc
==16212==ABORTING
```
global-buffer-overflow

### Valgrind report
```
==16126== Memcheck, a memory error detector
==16126== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.
==16126== Using Valgrind-3.18.1 and LibVEX; rerun with -h for copyright info
==16126== Command: ./global_out_of_bounds
==16126== 
1==16126== 
==16126== HEAP SUMMARY:
==16126==     in use at exit: 0 bytes in 0 blocks
==16126==   total heap usage: 1 allocs, 1 frees, 1,024 bytes allocated
==16126== 
==16126== All heap blocks were freed -- no leaks are possible
==16126== 
==16126== For lists of detected and suppressed errors, rerun with: -s
==16126== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)
```
沒錯

### 結論
ASan: 能
Valgrind: 不能

## heap_out_of_bounds

### Code
```
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

```
### ASan report
```
=================================================================
==15972==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x6040000001a0 at pc 0x557916219227 bp 0x7ffd992191b0 sp 0x7ffd992191a0
READ of size 4 at 0x6040000001a0 thread T0
    #0 0x557916219226 in main (/home/laxiflora/311551169-ST-2023/Lab06/heap_out_of_bounds+0x1226)
    #1 0x7fd457c2dd8f in __libc_start_call_main ../sysdeps/nptl/libc_start_call_main.h:58
    #2 0x7fd457c2de3f in __libc_start_main_impl ../csu/libc-start.c:392
    #3 0x557916219104 in _start (/home/laxiflora/311551169-ST-2023/Lab06/heap_out_of_bounds+0x1104)

0x6040000001a0 is located 360 bytes to the right of 40-byte region [0x604000000010,0x604000000038)
allocated by thread T0 here:
    #0 0x7fd457ee0867 in __interceptor_malloc ../../../../src/libsanitizer/asan/asan_malloc_linux.cpp:145
    #1 0x5579162191e5 in main (/home/laxiflora/311551169-ST-2023/Lab06/heap_out_of_bounds+0x11e5)
    #2 0x7fd457c2dd8f in __libc_start_call_main ../sysdeps/nptl/libc_start_call_main.h:58

SUMMARY: AddressSanitizer: heap-buffer-overflow (/home/laxiflora/311551169-ST-2023/Lab06/heap_out_of_bounds+0x1226) in main
Shadow bytes around the buggy address:
  0x0c087fff7fe0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c087fff7ff0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c087fff8000: fa fa 00 00 00 00 00 fa fa fa fa fa fa fa fa fa
  0x0c087fff8010: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c087fff8020: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
=>0x0c087fff8030: fa fa fa fa[fa]fa fa fa fa fa fa fa fa fa fa fa
  0x0c087fff8040: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c087fff8050: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c087fff8060: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c087fff8070: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c087fff8080: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:       fa
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
  Shadow gap:              cc
==15972==ABORTING
```
有heap-buffer-overflow


### Valgrind report
```
==15862== Memcheck, a memory error detector
==15862== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.
==15862== Using Valgrind-3.18.1 and LibVEX; rerun with -h for copyright info
==15862== Command: ./heap_out_of_bounds
==15862== 
==15862== Invalid read of size 4
==15862==    at 0x10918E: main (in /home/laxiflora/311551169-ST-2023/Lab06/heap_out_of_bounds)
==15862==  Address 0x4a8d1d0 is 288 bytes inside an unallocated block of size 4,194,096 in arena "client"
==15862== 
==15862== 
==15862== HEAP SUMMARY:
==15862==     in use at exit: 0 bytes in 0 blocks
==15862==   total heap usage: 1 allocs, 1 frees, 40 bytes allocated
==15862== 
==15862== All heap blocks were freed -- no leaks are possible
==15862== 
==15862== For lists of detected and suppressed errors, rerun with: -s
==15862== ERROR SUMMARY: 1 errors from 1 contexts (suppressed: 0 from 0)
```
有Invalid read of size 4

### 結論
Valgrind能
ASan能


## use_after_return

### Code
```
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
```

### ASan report
- 預設抓不到錯誤，但如果使用`export ASAN_OPTIONS=detect_stack_use_after_return=1`，則抓的到，下面是使用環境變數以後的結果
```
=================================================================
==15416==ERROR: AddressSanitizer: stack-use-after-return on address 0x7fbe42638030 at pc 0x55d3790224a6 bp 0x7ffebfa19a00 sp 0x7ffebfa199f0
WRITE of size 4 at 0x7fbe42638030 thread T0
    #0 0x55d3790224a5 in main (/home/laxiflora/311551169-ST-2023/Lab06/use_after_return+0x14a5)
    #1 0x7fbe45cd4d8f in __libc_start_call_main ../sysdeps/nptl/libc_start_call_main.h:58
    #2 0x7fbe45cd4e3f in __libc_start_main_impl ../csu/libc-start.c:392
    #3 0x55d3790221a4 in _start (/home/laxiflora/311551169-ST-2023/Lab06/use_after_return+0x11a4)

Address 0x7fbe42638030 is located in stack of thread T0 at offset 48 in frame
    #0 0x55d379022278 in foo (/home/laxiflora/311551169-ST-2023/Lab06/use_after_return+0x1278)

  This frame has 1 object(s):
    [48, 88) 'die' (line 5) <== Memory access at offset 48 is inside this variable
HINT: this may be a false positive if your program uses some custom stack unwind mechanism, swapcontext or vfork
      (longjmp and C++ exceptions *are* supported)
SUMMARY: AddressSanitizer: stack-use-after-return (/home/laxiflora/311551169-ST-2023/Lab06/use_after_return+0x14a5) in main
Shadow bytes around the buggy address:
  0x0ff8484befb0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ff8484befc0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ff8484befd0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ff8484befe0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ff8484beff0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0ff8484bf000: f5 f5 f5 f5 f5 f5[f5]f5 f5 f5 f5 f5 f5 f5 f5 f5
  0x0ff8484bf010: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ff8484bf020: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ff8484bf030: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ff8484bf040: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ff8484bf050: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:       fa
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
  Shadow gap:              cc
==15416==ABORTING
```

### valgrind report
```
==15593== Memcheck, a memory error detector
==15593== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.
==15593== Using Valgrind-3.18.1 and LibVEX; rerun with -h for copyright info
==15593== Command: ./use_after_return
==15593== 
1==15593== 
==15593== HEAP SUMMARY:
==15593==     in use at exit: 0 bytes in 0 blocks
==15593==   total heap usage: 1 allocs, 1 frees, 1,024 bytes allocated
==15593== 
==15593== All heap blocks were freed -- no leaks are possible
==15593== 
==15593== For lists of detected and suppressed errors, rerun with: -s
==15593== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)
```

### 結論
Valgrind不能
ASan加上環境變數以後能，預設不能


## Use_after_free

### Code
```
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
```

### ASan
```
==17333==ERROR: AddressSanitizer: heap-use-after-free on address 0x60400000001c at pc 0x556819eaa370 bp 0x7fff83e5d190 sp 0x7fff83e5d180
READ of size 4 at 0x60400000001c thread T0
    #0 0x556819eaa36f in main (/home/laxiflora/311551169-ST-2023/Lab06/use_after_free+0x136f)
    #1 0x7f2d17851d8f in __libc_start_call_main ../sysdeps/nptl/libc_start_call_main.h:58
    #2 0x7f2d17851e3f in __libc_start_main_impl ../csu/libc-start.c:392
    #3 0x556819eaa184 in _start (/home/laxiflora/311551169-ST-2023/Lab06/use_after_free+0x1184)

0x60400000001c is located 12 bytes inside of 40-byte region [0x604000000010,0x604000000038)
freed by thread T0 here:
    #0 0x7f2d17b04517 in __interceptor_free ../../../../src/libsanitizer/asan/asan_malloc_linux.cpp:127
    #1 0x556819eaa330 in main (/home/laxiflora/311551169-ST-2023/Lab06/use_after_free+0x1330)
    #2 0x7f2d17851d8f in __libc_start_call_main ../sysdeps/nptl/libc_start_call_main.h:58

previously allocated by thread T0 here:
    #0 0x7f2d17b04867 in __interceptor_malloc ../../../../src/libsanitizer/asan/asan_malloc_linux.cpp:145
    #1 0x556819eaa265 in main (/home/laxiflora/311551169-ST-2023/Lab06/use_after_free+0x1265)
    #2 0x7f2d17851d8f in __libc_start_call_main ../sysdeps/nptl/libc_start_call_main.h:58

SUMMARY: AddressSanitizer: heap-use-after-free (/home/laxiflora/311551169-ST-2023/Lab06/use_after_free+0x136f) in main
Shadow bytes around the buggy address:
  0x0c087fff7fb0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c087fff7fc0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c087fff7fd0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c087fff7fe0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c087fff7ff0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0c087fff8000: fa fa fd[fd]fd fd fd fa fa fa fa fa fa fa fa fa
  0x0c087fff8010: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c087fff8020: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c087fff8030: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c087fff8040: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c087fff8050: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:       fa
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
  Shadow gap:              cc
==17333==ABORTING
```
AddressSanitizer: heap-use-after-free

### Valgrind
```
==17471== Memcheck, a memory error detector
==17471== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.
==17471== Using Valgrind-3.18.1 and LibVEX; rerun with -h for copyright info
==17471== Command: ./use_after_free
==17471== 
1
0x4a8d04c
==17471== Invalid read of size 4
==17471==    at 0x10920B: main (in /home/laxiflora/311551169-ST-2023/Lab06/use_after_free)
==17471==  Address 0x4a8d04c is 12 bytes inside a block of size 40 free'd
==17471==    at 0x484B27F: free (in /usr/libexec/valgrind/vgpreload_memcheck-amd64-linux.so)
==17471==    by 0x109202: main (in /home/laxiflora/311551169-ST-2023/Lab06/use_after_free)
==17471==  Block was alloc'd at
==17471==    at 0x4848899: malloc (in /usr/libexec/valgrind/vgpreload_memcheck-amd64-linux.so)
==17471==    by 0x1091A5: main (in /home/laxiflora/311551169-ST-2023/Lab06/use_after_free)
==17471== 
1
0x4a8d04c
==17471== 
==17471== HEAP SUMMARY:
==17471==     in use at exit: 0 bytes in 0 blocks
==17471==   total heap usage: 2 allocs, 2 frees, 1,064 bytes allocated
==17471== 
==17471== All heap blocks were freed -- no leaks are possible
==17471== 
==17471== For lists of detected and suppressed errors, rerun with: -s
==17471== ERROR SUMMARY: 1 errors from 1 contexts (suppressed: 0 from 0)
```
Invalid read of size 

### 結論
Valgrind: 能
ASan: 能

## 剛好跳過red zone的範例

### code
```
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
```
輸出是: 
```
address of a[8] is 0x7f03c480a040, which normally equals to b[0]:0x7f03c480a040
b[0] = 0
```
我觀察到ASan雖然有插樁，但是a跟b之間的red zone大小是固定的，如果用剛好的offset，就可以成功跨過red zone。
### ASan
沒有輸出，抓不到錯