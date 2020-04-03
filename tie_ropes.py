# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(K, A):
    # write your code in Python 3.6
    cnt = 0
    length = 0
    for rope in A:
        length += rope
        if length >= K:
            cnt += 1
            length = 0
    return cnt
