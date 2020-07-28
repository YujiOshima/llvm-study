set -ex
docker build -f Dockerfile.llvmlite -t llvm-lite .
docker build -f Dockerfile.runtime -t llvm-runtime .
