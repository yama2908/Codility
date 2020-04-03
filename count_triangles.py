# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    A.sort()
    ans = 0
    for first in range(len(A) - 2):
        third = first + 2
        for second in range(first + 1, len(A) - 1):
            while third < len(A) and A[first] + A[second] > A[third]:
                third += 1
            ans += (third - 1) - second
    return ans
