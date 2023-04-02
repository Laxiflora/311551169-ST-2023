/*
  Ref:
  * https://llvm.org/doxygen/
  * https://llvm.org/docs/GettingStarted.html
  * https://llvm.org/docs/WritingAnLLVMPass.html
  * https://llvm.org/docs/ProgrammersManual.html
  * https://stackoverflow.com/questions/28168815/adding-a-function-call-in-my-ir-code-in-llvm
  * https://stackoverflow.com/questions/30234027/how-to-call-printf-in-llvm-through-the-module-builder-system
  * https://gite.lirmm.fr/grevy/llvm-tutorial/-/blob/master/src/exercise3bis/ReplaceFunction.cpp
 */
#include "lab-pass.h"
#include "llvm/IR/LegacyPassManager.h"
#include "llvm/IR/Module.h"
#include "llvm/IR/BasicBlock.h"
#include "llvm/IR/IRBuilder.h"
#include "llvm/IR/Constants.h"

#include "llvm/Pass.h"
#include "llvm/IR/Function.h"
#include "llvm/IR/DebugInfo.h"
#include "llvm/IR/IntrinsicInst.h"
#include "llvm/Support/raw_ostream.h"
#include "llvm/IR/InstIterator.h"
#include "llvm/IR/LLVMContext.h"
#include "llvm/IR/Module.h"
#include "llvm/IR/DebugInfoMetadata.h"

#include "llvm/IR/Constants.h"
#include "llvm/IR/Function.h"
#include "llvm/IR/Type.h"
#include "llvm/Support/raw_ostream.h"

#include "llvm/IR/Constants.h"
#include "llvm/IR/Function.h"
#include "llvm/IR/Type.h"
#include "llvm/Pass.h"
#include "llvm/Support/raw_ostream.h"

#include "llvm/Analysis/CallGraph.h"


using namespace llvm;

char LabPass::ID = 0;

bool LabPass::doInitialization(Module &M) {
  return true;
}

static Constant* getI8StrVal(Module &M, char const *str, Twine const &name) {
  LLVMContext &ctx = M.getContext();

  Constant *strConstant = ConstantDataArray::getString(ctx, str);

  GlobalVariable *gvStr = new GlobalVariable(M, strConstant->getType(), true,
    GlobalValue::InternalLinkage, strConstant, name);

  Constant *zero = Constant::getNullValue(IntegerType::getInt32Ty(ctx));
  Constant *indices[] = { zero, zero };
  Constant *strVal = ConstantExpr::getGetElementPtr(Type::getInt8PtrTy(ctx),
    gvStr, indices, true);

  return strVal;
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

  // int getCallStackDepth(CallGraphNode *Node, int currentDepth) {
  //   int maxDepth = currentDepth;
  //   for (auto &Caller : *Node) {
  //     CallGraphNode *CallerNode = Caller.second;
  //     int depth = getCallStackDepth(CallerNode, currentDepth + 1);
  //     maxDepth = std::max(maxDepth, depth);
  //   }
  //   return maxDepth;
  // }


bool LabPass::runOnModule(Module &M) {
  errs() << "runOnModule\n";
  FunctionCallee exitCallee = exitPrototype(M);
  FunctionCallee printfCallee = printfPrototype(M);
  LLVMContext &ctx = M.getContext();
  for (auto &F : M) {
    if(F.empty()){
      continue;
    }
    StringMap<Constant*> CallCounterMap;
    StringMap<Constant*> funcNameMap;
    errs() << F.getName() << "\n";
    BasicBlock &Bstart = F.front();
    Instruction &Istart = Bstart.front();
    IRBuilder<> Builder(&Istart);
    std::string f_info = "";

    //ConstantInt* constDepth = &llvm::cast < llvm::ConstantInt, llvm::Value>(CallCounterMap[F.getName()]);
    int depth = 0;
    //depth = constDepth->getSExtValue();

    f_info = f_info + (std::string(depth, ' ') + F.getName().str());
    std::vector<Value*> printfArgument;
    printfArgument.push_back(Builder.CreateGlobalStringPtr(
        (f_info + ": 0x%lx\n").c_str(), "fmt"
        ));
    printfArgument.push_back(Builder.CreatePtrToInt(
      ConstantExpr::getBitCast(&F, Type::getInt64PtrTy(ctx)), Type::getInt64Ty(ctx)
      ));
    Builder.CreateCall(printfCallee, printfArgument);

    errs() << "Depth of calling stack for function " << F.getName() << ": " << depth << "\n";

    //BuilderBof.CreateCall(exitCallee, { one });
   // dumpIR(F);

    // TODO
  }

  return true;
}

static RegisterPass<LabPass> X("labpass", "Lab Pass", false, false);