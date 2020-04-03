# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, M):
    # write your code in Python 3.6
    lcm = N * M // gcd(N, M)
    return lcm // M

def gcd(a, b):
    # Euclidean Algorithm
    if (a % b == 0):
        return b
    else:
        return gcd(b, a % b)
