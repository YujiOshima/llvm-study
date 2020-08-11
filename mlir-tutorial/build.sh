REFGISTORY="dev"
docker build -t ${REFGISTORY}/mlir-tutorial .
docker push ${REFGISTORY}/mlir-tutorial
