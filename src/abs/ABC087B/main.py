#!/usr/bin/env python3
import sys


def solve(A: int, B: int, C: int, X: int):
    ret = 0
    for i in range(A+1):
        for j in range(B+1):
            for k in range(C+1):
                if(i * 500 + j * 100 + k * 50 == X):
                    ret += 1
    print(ret)
    return


# Generated by 2.3.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    solve(A, B, C, X)

if __name__ == '__main__':
    main()
