# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    upper = [0] * len(A)
    lower = [0] * len(A)
    # Fill the limit_upper and limit_lower
    for i in range(len(A)):
        upper[i] = i + A[i]
        lower[i] = i - A[i]
    upper.sort()
    lower.sort()
    lower_index, cnt = 0, 0
    for upper_index in range(len(A)):
        while lower_index < len(A) and lower[lower_index] <= upper[upper_index]:
            lower_index += 1
        cnt += lower_index - upper_index - 1
        if cnt > 10000000:
            return -1
    return cnt
