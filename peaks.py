# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    peaks = [0] * len(A)
    for i in range(1, len(A) - 1):
        peaks[i] = peaks[i-1]
        if A[i-1] < A[i] > A[i+1]:
            peaks[i] += 1
    if len(A) <= 2 or peaks[-2] == 0:
        return 0
    peaks[-1] = peaks[-2]
    
    ans, candidate = 0, 1
    while candidate * candidate <= len(A):
        if len(A) % candidate == 0:
            blocks, size = candidate, len(A) // candidate
            if peaks[0] < peaks[size - 1]:
                for each in range(size, len(A), size):
                    if peaks[each - 1] == peaks[size + each - 1]:
                        break
                else:
                    ans = blocks
                    
            blocks, size = len(A) // candidate, candidate
            if peaks[0] < peaks[size - 1]:
                for each in range(size, len(A), size):
                    if peaks[each - 1] == peaks[size + each - 1]:
                        break
                else:
                    return blocks
        candidate += 1
    return ans
