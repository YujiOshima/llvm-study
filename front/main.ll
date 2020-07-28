; ModuleID = '<string>'
source_filename = "<string>"
target triple = "unknown-unknown-unknown"

@fstr = internal constant [4 x i8] c"%d\0A\00"

define void @main() {
.2:
  %.3 = alloca i32
  store i32 5, i32* %.3
  %.5 = alloca i32
  %.6 = load i32, i32* %.3
  store i32 %.6, i32* %.5
  %.8 = bitcast [4 x i8]* @fstr to i8*
  %.9 = load i32, i32* %.3
  %.10 = add i32 %.9, 1
  %.11 = call i32 (i8*, ...) @printf(i8* %.8, i32 %.10)
  %.12 = load i32, i32* %.5
  %.13 = call i32 (i8*, ...) @printf(i8* %.8, i32 %.12)
  %.14 = load i32, i32* %.3
  %.15 = add i32 %.14, 2
  %.16 = call i32 (i8*, ...) @printf(i8* %.8, i32 %.15)
  ret void
}

declare i32 @printf(i8*, ...)
