Lab 5
========

Create an LLVM Pass that can log the following message when a function is invoked:
* Indent N spaces before outputting, where N is the function depth, and define the depth of the main function as 0
* Function name
* Function address

You can only modify the files listed below:
* lab/llvmpass/lab-pass.cc
* lab/llvmpass/lab-pass.h

The output of the solution should resemble the following image:

![](https://i.imgur.com/cimRbvy.png)

(Note that due to ASLR and PIE, the addresses of the functions will be different in each execution, but the offset will remain the same.)


## 寫作業心得
- 這份作業真的很有挑戰，陸陸續續花了快五天才寫完，大多是依靠chatGPT+文件輔助才過關的

### LLVM pass介紹
編譯器分為前後端，在clang體系中為了降低不同計算機架構所需要重新設計編譯器的成本，採用了IR(中間碼)的設計，而LLVM pass提供一個讓我們可以優化與修改IR code的平台，使我們可以從貼近assembly的層級去檢視程式碼與除錯

- LLVM pass處理的是compile階段的程式，只能從text(code)層面下手，無法在當下得知run time variable實際的值
- LLVM pass允許我們新增basic block、instruction等等指令用於除錯或優化效能，也允許我們讀取IR邏輯下的register的值(IR code的register為無限多，實際如何分派給暫存器還要看後端編譯器如何實作)
    - example中演示如何使用金絲雀測試法來驗證是否有stack overflow

### 寫作業歷程
- 花了好久時間才了解到pass處理的是靜態的程式，我們只能觀看一個function的程式碼，無從得知是誰去呼叫他的(要知道的話只能從ret register下手)。

<br>

- 因為前面的原因所以導致了追蹤遞迴深度及其麻煩，最後用的方法是令一個全域變數glob_depth，並且在每個function的起頭插入一個glob_depth++，在每個function的結尾(ret前)插入一個glob_depth--，並且呼叫printf(%d)並推入參數Value* loaded_depth，這樣就能在run time實際追蹤到這個函數時的深度了

<br>

- 但是因為技術問題(global type i32 ptr Value* 死活cast不回int type)，不論如何都無法讀取全域變數到pass中操作，所以最後用的土炮方法是`printf("%.*s", depth, "          ")`
    - 這樣就不用讀取depth的值以後製作一個string再送回IRBuilder，直接呼叫printf將得到的Value* type全域變數作為參數送入即可

<br>

- 如果想要取用全域變數，需要先進行讀取、操作、存放的動作，因為值是從記憶體中取得 (其實只要不是從register取到的值均需要load&store)，這裡沒有考慮到static scheduler optimization(畢竟光寫出來就有夠累了orz)，而且真的考慮到的效益也不高，畢竟IR code還會再經過一層後端編譯器進一步優化。

<br>

- function pointer address也同理，在runtime的時候用printf傳入`i64 ptrtoint (ptr @func3 to i64))` (func3 函數的地址)並且轉成i64格式以後用%lx印出來，就會得到正確的地址了

<br>

下面附上一段修改後的IR code:
```
func3

BB: 

  %glob_depth = load i32, ptr @glob_depth, align 4, !dbg !18
  %sum = add i32 %glob_depth, 1, !dbg !18
  store i32 %sum, ptr @glob_depth, align 4, !dbg !18
  %glob_depth1 = load i32, ptr @glob_depth, align 4, !dbg !18
  %1 = load i64, ptr @glob_depth, align 8, !dbg !18
  %2 = call i32 (ptr, ...) @printf(ptr @fmt.4, i32 %glob_depth1, ptr @space.1, i64 ptrtoint (ptr @func3 to i64)), !dbg !18
  ret void, !dbg !18
```

### Reference
[官方新手教學](https://llvm.org/docs/WritingAnLLVMPass.html#introduction-what-is-a-pass)
[知乎教學](https://zhuanlan.zhihu.com/p/122522485)
[官方文件](https://llvm.org/doxygen/classllvm_1_1Value.html) (其實有繼承關係圖還不錯，不過類別真的好多好雜...，global variable讀進來一律當pointer似乎也沒寫清楚，print type只會顯示i32(int global variable)，胡亂cast到ConstantInt卻又會失敗回傳NULL pointer，一不小心就是segmentation fault)
