# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # write your code in Python 3.6
    position = set()
    for i in range(len(A)):
        position.add(A[i])
        if len(position) == X:
            return i
    return -1
