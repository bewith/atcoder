#!/usr/bin/env python3
import sys

def solve(H: int, W: int, A: "List[List[str]]"):
    points = [[[0, 0] for _ in range(W)] for _ in range(H)]


    for i in reversed(range(H)):
        for j in reversed(range(W)):
            if ((i == (H - 1)) and (j == (W - 1))):
                continue


            target = (i + j) % 2

            if i == (H - 1):
                moveFromRight(A, points, i, j, target)
                continue
            if j == (W - 1):
                moveFromBottom(A, points, i, j, target)
                continue

            if target == 0:
                
                if (points[i + 1][j][0] - points[i + 1][j][1] + (1 if A[i + 1][j] == "+" else -1)) >= (points[i][j + 1][0] - points[i][j + 1][1] + (1 if A[i][j + 1] == "+" else -1)):
                    moveFromBottom(A, points, i, j, target)
                else:
                    moveFromRight(A, points, i, j, target)
            else:
                if (points[i + 1][j][1] - points[i + 1][j][0] + (1 if A[i + 1][j] == "+" else -1)) >= (points[i][j + 1][1] - points[i][j + 1][0] + (1 if A[i][j + 1] == "+" else -1)):
                    moveFromBottom(A, points, i, j, target)
                else:
                    moveFromRight(A, points, i, j, target)

    # for p in points:
    #     print(p)

    if points[0][0][0] > points[0][0][1]:
        print("Takahashi")
    elif points[0][0][0] < points[0][0][1]:
        print("Aoki")
    else:
        print("Draw")
    return

def moveFromRight(A, points, i, j, target):
    points[i][j][0] = points[i][j + 1][0]
    points[i][j][1] = points[i][j + 1][1]
    if A[i][j + 1] == "+":
        points[i][j][target] += 1
    else:
        points[i][j][target] -= 1

def moveFromBottom(A, points, i, j, target):
    points[i][j][0] = points[i + 1][j][0]
    points[i][j][1] = points[i + 1][j][1]
    if A[i + 1][j] == "+":
        points[i][j][target] += 1
    else:
        points[i][j][target] -= 1


# Generated by 2.3.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))
    W = int(next(tokens))

    A = []
    for _ in range(H):
        A.append(list(next(tokens)))

    solve(H, W, A)

if __name__ == '__main__':
    main()
