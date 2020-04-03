# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    if not A:
        return 0

    dp = [0] * len(A)
    for i in range(len(A)):
        dp[i] = max(dp[i-1] + A[i], A[i])
    return max(dp)
