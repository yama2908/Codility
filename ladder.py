# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6
    length = len(A)
    dp = [0] * length
    B = [(1 << item) - 1 for item in B]
    fib = [0] * (length + 2)
    fib[1] = 1
    for i in range(2, length + 2):
        fib[i] = fib[i - 1] + fib[i - 2]
    for i in range(length):
        dp[i] = fib[A[i] + 1] & B[i]
    return dp
