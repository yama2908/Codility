# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6
    if len(A) < 2:
        return len(A)
    cnt = 1
    end = B[0]
    i = 1
    while i < len(A):
        while i < len(A) and A[i] <= end:
            i += 1
        if i == len(A):
            break
        cnt += 1
        end = B[i]
    return cnt
