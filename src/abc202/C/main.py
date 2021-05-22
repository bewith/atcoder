#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]", B: "List[int]", C: "List[int]"):
    ACount = {}

    for i in range(N + 1):
        ACount[i] = 0

    for i in range(N):
        ACount[A[i]] += 1

    ret = 0
    for j in range(N):
        ret += ACount[B[C[j] - 1]]

    print(ret)



    # for i in range(N):
    #     for j in range(N):
    #         if A[i] == B[C[j] - 1]:
    #             ret += 1
    # print(ret)
    return


# Generated by 2.3.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    B = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    C = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A, B, C)

if __name__ == '__main__':
    main()
