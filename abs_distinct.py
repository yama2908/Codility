# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    seen = set()
    for i in range(len(A)):
        seen.add(abs(A[i]))
    return len(seen)
