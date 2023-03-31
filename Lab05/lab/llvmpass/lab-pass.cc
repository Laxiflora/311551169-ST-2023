/*
  Ref:
  * https://llvm.org/doxygen/
  * https://llvm.org/docs/GettingStarted.html
  * https://llvm.org/docs/WritingAnLLVMPass.html
  * https://llvm.org/docs/ProgrammersManual.html
 */
#include "lab-pass.h"
#include "llvm/IR/LegacyPassManager.h"
#include "llvm/IR/Module.h"

using namespace llvm;

char LabPass::ID = 0;

bool LabPass::doInitialization(Module &M) {
  return true;
}


static FunctionCallee printfPrototype(Module &M) {
  LLVMContext &ctx = M.getContext();

  FunctionType *printfType = FunctionType::get(
    Type::getInt32Ty(ctx),
    { Type::getInt8PtrTy(ctx) },
    true);

  FunctionCallee printfCallee = M.getOrInsertFunction("printf", printfType);

  return printfCallee;
}

static FunctionCallee exitPrototype(Module &M) {
  LLVMContext &ctx = M.getContext();

  FunctionType *exitType = FunctionType::get(
    Type::getInt32Ty(ctx),
    { Type::getInt32Ty(ctx) },
    false);

  FunctionCallee exitCallee = M.getOrInsertFunction("exit", exitType);

  return exitCallee;
}






static void dumpIR(Function &F)
{
  for (auto &BB : F) {
    errs() << "BB: " << "\n";
    errs() << BB << "\n";
  }
}

bool LabPass::runOnModule(Module &M) {
  errs() << "runOnModule\n";

  // get printf and exit() function for creating call
  FunctionCallee exitCallee = exitPrototype(M);
  FunctionCallee printfCallee = printfPrototype(M);


    //BuilderBof.CreateCall(printfCallee, { stackBofMsg });
    //BuilderBof.CreateCall(exitCallee, { one });
  for (auto &F : M) {
    errs() << F.getName() << " " << &F.getEntryBlock().front() << "\n";
    errs()<< getDepth(M,F) << "\n";
    dumpIR(F);
    // TODO
  }

  return true;
}

static RegisterPass<LabPass> X("labpass", "Lab Pass", false, false);