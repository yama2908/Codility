# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.6
    if len(A) == 0:
        return A

    K = K % len(A)
    return A[-K:] + A[:-K]
