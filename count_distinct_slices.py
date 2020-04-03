# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(M, A):
    # write your code in Python 3.6
    accessed = [-1] * (M + 1)
    front, back = 0, 0
    ans = 0
    for front in range(len(A)):
        if accessed[A[front]] == -1:
            accessed[A[front]] = front
        else:
            newback = accessed[A[front]] + 1
            ans -= (front - newback) * (front - newback + 1) // 2
            ans += (front - back) * (front - back + 1) // 2
            if ans >= 1000000000:
                return 1000000000
            
            for i in range(back, newback):
                accessed[A[i]] = -1
            accessed[A[front]] = front
            back = newback
            
    ans += (front - back + 1) * (front - back + 2) // 2
    return min(ans, 1000000000)
