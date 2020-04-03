# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    min_avg_value = (A[0] + A[1]) / 2.0
    min_avg_pos = 0
    for i in range(len(A) - 2):
        if (A[i] + A[i + 1]) / 2.0 < min_avg_value:
            min_avg_value = (A[i] + A[i + 1]) / 2.0
            min_avg_pos = i
        if (A[i] + A[i + 1] + A[i + 2]) / 3.0 < min_avg_value:
            min_avg_value = (A[i] + A[i + 1] + A[i + 2]) / 3.0
            min_avg_pos = i
    if (A[-1] + A[-2]) / 2.0 < min_avg_value:
        min_avg_value = (A[-1] + A[-2]) / 2.0
        min_avg_pos = len(A) - 2
    return min_avg_pos
