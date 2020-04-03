# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6
    cnt = 0
    stack = []
    for i in range(len(A)):
        if B[i] == 1:
            stack.append(A[i])
            
        while stack:
            if stack[-1] < A[i]:
                stack.pop()
            else:
                break
        else:
            cnt += 1
    return cnt + len(stack)
