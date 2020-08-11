FROM ubuntu
RUN apt update && apt install -y git build-essential clang lld cmake ninja-build
ADD llvm-project /llvm-project
RUN mkdir /llvm-project/build \
    && cd llvm-project/build \
    && cmake -G Ninja ../llvm \
       -DLLVM_ENABLE_PROJECTS=mlir \
       -DLLVM_BUILD_EXAMPLES=ON \
       -DLLVM_TARGETS_TO_BUILD="X86;NVPTX;AMDGPU" \
       -DCMAKE_BUILD_TYPE=Release \
       -DLLVM_ENABLE_ASSERTIONS=ON \
       -DCMAKE_C_COMPILER=clang -DCMAKE_CXX_COMPILER=clang++ -DLLVM_ENABLE_LLD=ON \
    && cmake --build . --target check-mlir
