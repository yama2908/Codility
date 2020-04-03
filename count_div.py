# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):
    # write your code in Python 3.6
    if A % K == 0:
        return B // K - A // K + 1
    else:
        return B // K - A // K
