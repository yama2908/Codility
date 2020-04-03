# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6
    cnt = 0
    for x, y in zip(A, B):
        if hasSamePrimeDivisors(x, y):
            cnt += 1
        return cnt
    
    
def gcd(x, y):
    if x % y == 0:
        return y;
    else:
        return gcd(y, x % y)
    
    
def removeCommonPrimeDivisors(x, y):
    while x != 1:
        gcd_value = gcd(x, y)
        if gcd_value == 1:
            break
        x /= gcd_value
    return x


def hasSamePrimeDivisors(x, y):
    gcd_value = gcd(x, y)
    x = removeCommonPrimeDivisors(x, gcd_value)
    y = removeCommonPrimeDivisors(y, gcd_value)
    if x != 1 or y != 1:
        return False
    else:
        return True
