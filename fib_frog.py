# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    length = len(A)
    fibs = fibonacciDynamic(length)
    
    dp = [-1] * (length + 1)
    for i in range(length + 1):
        leaf = lambda k: k == length or A[k] == 1
        if not leaf(i):
            dp[i] = 0
        else:
            if i + 1 in fibs:
                dp[i] = 1
            else:
                candidates = []
                for f in fibs:
                    if i - f >= 0 and dp[i - f] > 0:
                        candidates.append(dp[i - f] + 1)
                dp[i] = min(candidates) if len(candidates) > 0 else 0
    return dp[-1] if dp[-1] > 0 else -1


def fibonacciDynamic(n):
    fib = [0] * (n + 2)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
        if fib[i] > n:
            return fib[1: i]
