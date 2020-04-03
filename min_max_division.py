# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(K, M, A):
    # write your code in Python 3.6
    blocksNeeded = 0
    lower, upper = max(A), sum(A)
    ans = 0
    if K == 1:
        return upper
    if K >= len(A):
        return lower
    
    while lower <= upper:
        mid = (lower + upper) // 2
        blocksNeeded = blocksNo(A, mid)
        if blocksNeeded <= K:
            upper = mid - 1
            ans = mid
        else:
            lower = mid + 1
    return ans


def blocksNo(A, maxBlock):
    blocksNumber = 1
    blockSum = A[0]
    for element in A[1:]:
        if blockSum + element > maxBlock:
            blockSum = element
            blocksNumber += 1
        else:
            blockSum += element
    return blocksNumber
