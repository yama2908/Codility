# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import collections
def solution(A):
    # write your code in Python 3.6
    if len(A) < 3:
        return 0
    block = collections.namedtuple("Block", ["height", "max_depth"])
    stack = [block(A[0],0)]
    for height in A[1:]:
        if height == stack[-1].height:
            continue
        elif height < stack[-1].height:
            stack.append(block(height, 0))
        else:
            max_depth = 0
            while len(stack) > 1 and height > stack[-1].height:
                additional_depth = min(stack[-2].height, height) - stack[-1].height
                max_depth = max(max_depth, stack[-1].max_depth) + additional_depth
                stack.pop()
                
            while len(stack) > 0 and height >= stack[-1].height:
                max_depth = max(max_depth, stack[-1].max_depth)
                stack.pop()
                stack.append(block(height, max_depth))
        overall_max_depth = 0
        for b in stack:
            if b.max_depth > overall_max_depth:
                overall_max_depth = b.max_depth
        return overall_max_depth
