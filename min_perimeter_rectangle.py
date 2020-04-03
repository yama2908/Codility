# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    i, ans = 1, float('inf')
    while i * i <= N:
        if N % i == 0:
            ans = min(ans, 2 * (i + N // i))
        i += 1
    return ans
