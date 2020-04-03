# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    l = bin(N).split('1')
    ans = 0
    for i in range(1, len(l) - 1):
        ans = max(ans, len(l[i]))
    return ans
