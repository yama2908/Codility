# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(H):
    # write your code in Python 3.6
    stack = []
    cnt = 0
    for height in H:
        while stack and height < stack[-1]:
            stack.pop()
            cnt += 1
        if not stack or height > stack[-1]:
            stack.append(height)
    return cnt + len(stack)
