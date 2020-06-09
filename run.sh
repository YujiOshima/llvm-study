set -ex
docker run -it --rm -v $PWD/src://llvm-project/src gcr.io/professor-x-dev/oshima/llvm-dev $@
