# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    A.sort()
    ans = 1
    for el in A:
        if el == ans:
            ans += 1
    return ans
