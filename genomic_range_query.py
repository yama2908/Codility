# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, P, Q):
    # write your code in Python 3.6
    ans = []
    for i in range(len(P)):
        if 'A' in S[min(P[i], Q[i]):max(P[i], Q[i]) + 1]:
            ans.append(1)
        elif 'C' in S[min(P[i], Q[i]):max(P[i], Q[i]) + 1]:
            ans.append(2)
        elif 'G' in S[min(P[i], Q[i]):max(P[i], Q[i]) + 1]:
            ans.append(3)
        else:
            ans.append(4)
    return ans
