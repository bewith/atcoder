#!/usr/bin/env python3
import sys
import copy

def loop(patterns, rest, trace, ngList):
    for ng in ngList:
        if ng in trace:
            return

    if len(rest) == 0:
        patterns.append(trace)
        return

    for r in rest:
        tmpr = copy.copy(rest)
        tmpr.remove(r)
        loop(patterns, tmpr, trace + str(r), ngList)

def solve(N: int, A: "List[List[int]]", M: int, X: "List[int]", Y: "List[int]"):
    ngList = []
    for m in range(M):
        ngList.append(str(X[m] - 1) + str(Y[m] - 1))
        ngList.append(str(Y[m] - 1) + str(X[m] - 1))

    rest = [i for i in range(N)]
    patterns = []
    loop(patterns, rest, "", ngList)

    if len(patterns) == 0:
        print(-1)
        return
    else:
        ret = 10000000000
        for o in patterns:
            sum = 0
            for i in range(len(o)):
                sum += A[i][int(o[i])]
            ret = min(sum, ret)
    print(ret)
    return


# Generated by 2.3.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [[int(next(tokens)) for _ in range(N)] for _ in range(N)]  # type: "List[List[int]]"
    M = int(next(tokens))  # type: int
    X = [int()] * (M)  # type: "List[int]"
    Y = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    solve(N, A, M, X, Y)

if __name__ == '__main__':
    main()
