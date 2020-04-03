# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    dp = [A[0]] * (len(A) + 6)
    for i in range(1, len(A)):
        dp[i + 6] = max(dp[i: i + 6]) + A[i]
    return dp[-1]
