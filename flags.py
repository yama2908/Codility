# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from math import sqrt

def solution(A):
    # write your code in Python 3.6
    length = len(A)
    next_peak = [-1] * length
    peaks_cnt = 0
    first_peak = -1
    for i in range(length - 2, 0, -1):
        if A[i-1] < A[i] > A[i+1]:
            next_peak[i] = i
            peaks_cnt += 1
            first_peak = i
        else:
            next_peak[i] = next_peak[i+1]
    if peaks_cnt < 2:
        return peaks_cnt

    ans = 1
    for min_distance in range(int(sqrt(length)) + 1, 1, -1):
        flags_used = 1
        flags_have = min_distance - 1
        pos = first_peak
        while flags_have > 0:
            if pos + min_distance >= length - 1:
                break
            pos = next_peak[pos + min_distance]
            if pos == -1:
                break
            flags_used += 1
            flags_have -= 1
        ans = max(ans, flags_used)
    return ans
