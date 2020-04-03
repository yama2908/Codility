# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    cnt = 0
    for i in range(len(A)):
        if cnt == 0:
            cnt += 1
            candidate = A[i]
            index = i
        else:
            if candidate != A[i]:
                cnt -= 1
            else:
                cnt += 1
                
    cnt = 0
    for i in range(len(A)):
        if A[i] == candidate:
            cnt += 1
            if cnt > len(A) // 2:
                return index
    return -1
