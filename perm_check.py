# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    orx = 0
    for i in range(len(A)):
        orx ^= A[i] ^ (i + 1)

    if orx == 0:
        return 1
    else:
        return 0
