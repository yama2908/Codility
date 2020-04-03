# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    length = len(A)
    max_ending = [0] * length
    temp = 0
    for i in range(1, length - 2):
        temp = max(0, A[i] + temp)
        max_ending[i] = temp
        
    max_beginning = [0] * length
    temp = 0
    for i in range(length - 2, 1, -1):
        temp = max(0, A[i] + temp)
        max_beginning[i] = temp
        
    ans = 0
    for i in range(length - 2):
        ans = max(ans, max_ending[i] + max_beginning[i + 2])
    return ans
