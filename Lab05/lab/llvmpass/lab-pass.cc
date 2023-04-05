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



bool LabPass::runOnModule(Module &M) {

LLVMContext &ctx = M.getContext();

// create a new LLVM module
llvm::Module *module = new llvm::Module("MyModule", ctx);



// create a new global variable of type i32 with initial value 0
llvm::Constant *initValue = llvm::ConstantInt::get(ctx, llvm::APInt(32, -1));
llvm::GlobalVariable *globalVar = new llvm::GlobalVariable(
  M,
  llvm::Type::getInt32Ty(ctx),
  false,
  GlobalValue::InternalLinkage,
  initValue, "glob_depth");



// Create a global string with name "space"
GlobalVariable* spaceGlobal = new GlobalVariable(M, llvm::ArrayType::get(llvm::Type::getInt8Ty(ctx), 2),
                                                  true, llvm::GlobalValue::PrivateLinkage, 0, "space");
spaceGlobal->setInitializer(llvm::ConstantDataArray::getString(ctx, " ", true));


    Constant* strConstant = ConstantDataArray::getString(ctx, "                                              ");
GlobalVariable* globalString = new GlobalVariable(
    M,
    strConstant->getType(),
    true, // is constant
    GlobalValue::PrivateLinkage,
    strConstant,
    "space"
);


  errs() << "runOnModule\n";
  FunctionCallee exitCallee = exitPrototype(M);
  FunctionCallee printfCallee = printfPrototype(M);
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


GlobalVariable* key = M.getNamedGlobal("glob_depth");
Value *loadValue = Builder.CreateLoad(globalVar->getValueType(), globalVar, "glob_depth");
Value *addValue = llvm::ConstantInt::get(ctx, llvm::APInt(32, 1));
Value *sumValue = Builder.CreateAdd(loadValue, addValue, "sum");
StoreInst *Store = Builder.CreateStore(sumValue, globalVar);

loadValue = Builder.CreateLoad(globalVar->getValueType(), globalVar, "glob_depth");



// Create a printf call that prints the value of the global variable
// Value *formatString = Builder.CreateGlobalStringPtr("depth: %d\n");


// std::vector<Value*> printfArgs = { formatString, loadValue };
// Builder.CreateCall(printfCallee, printfArgs);




ConstantInt* constInt = dyn_cast<ConstantInt>(globalVar->getInitializer());
    unsigned _depth = constInt->getSExtValue();
    errs() << _depth<<"\n";
    Value *globalVal = Builder.CreateLoad(IntegerType::getInt64Ty(ctx), globalVar);
    errs() << "\n" << "Global value: " << constInt->getSExtValue() << "\n";


    std::string f_info = "";

    int depth = 0;
    //depth = intValue;

    f_info = f_info + (std::string(depth, ' ') + F.getName().str());
    std::vector<Value*> printfArgument;



Value* stringPointer = Builder.CreateBitCast(
    globalString,
    Type::getInt8PtrTy(ctx)
);



    printfArgument.push_back(Builder.CreateGlobalStringPtr(
        ( "%.*s" + f_info + ": 0x%lx\n").c_str(),"fmt"
        ));

    printfArgument.push_back(loadValue);

          printfArgument.push_back(stringPointer);


    printfArgument.push_back(Builder.CreatePtrToInt(
      ConstantExpr::getBitCast(&F, Type::getInt64PtrTy(ctx)), Type::getInt64Ty(ctx)
      ));
    Builder.CreateCall(printfCallee, printfArgument);

    errs() << "Depth of calling stack for function " << F.getName() << ": " << depth << "\n";

    dumpIR(F);


for (BasicBlock &BB : F) {
    for (Instruction &I : BB) {
        if (ReturnInst *ret = dyn_cast<ReturnInst>(&I)) {
            IRBuilder<> Builder_end(ret);
            // Create a new instruction right before the return instruction
            // For example, to print the value of the global variable:
loadValue = Builder_end.CreateLoad(globalVar->getValueType(), globalVar, "glob_depth");
addValue = llvm::ConstantInt::get(ctx, llvm::APInt(32, -1));
sumValue = Builder_end.CreateAdd(loadValue, addValue, "sum");
Store = Builder_end.CreateStore(sumValue, globalVar);
        }
    }
}


    // TODO
  }

  return true;
}

static RegisterPass<LabPass> X("labpass", "Lab Pass", false, false);