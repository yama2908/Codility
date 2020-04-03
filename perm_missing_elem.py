# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    xor = 0
    for index in range(len(A)):
        xor ^= A[index] ^ (index + 1)
    return xor^(len(A) + 1)
