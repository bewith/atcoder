#!/usr/bin/env python3
import sys


def solve(N: int):
    results = []
    for i in range(2 ** N):
        record = ""
        for j in range(N):
            if ((i >> j) & 1):
                record += "("
            else:
                record += ")"
        results.append(record)

    ret = []
    for r in results:
        if judge(r):
            ret.append(r)

    if len(ret) == 0:
        print()
        return 
    
    for r in sorted(ret):
        print(r)
    return

def judge(record):
    stack = []
    for s in record:
        if s == "(":
            stack.append("")
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    
    return len(stack) == 0




# Generated by 2.3.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)

if __name__ == '__main__':
    main()
