# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in S:
        if char in mapping:
            if not stack:
                return 0
            elif mapping[char] != stack.pop():
                return 0
        else:
            stack.append(char)
    if not stack:
        return 1
    else:
        return 0
