# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    if len(A) <= 1:
        return 0
    
    dp = [0] * len(A)
    for i in range(1, len(A)):
        dp[i] = max(dp[i-1] + A[i] - A[i-1], 0)
        return max(dp)
