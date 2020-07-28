set -ex
docker build -f Dockerfile.llvmlite -t llvm-lite .
docker run -it --rm -v $PWD/front:/front llvm-lite python main.py
docker build -f Dockerfile.runtime -t llvm-runtime .
set +e
echo "run on Linux"
docker run -it --rm llvm-runtime ./run_main
docker run --name tmp-llvm -itd llvm-runtime sleep 10
docker cp tmp-llvm:/front/main.s .
docker rm -f tmp-llvm
clang main.s -o run_main
echo "run on OSX"
./run_main
rm run_main main.s
