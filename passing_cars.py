# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    west, count = 0, 0
    for i in range(len(A) - 1, -1, -1):
        if A[i] == 1:
            west += 1
        else:
            count += west
            if count > 1000000000:
                return -1
    return count
