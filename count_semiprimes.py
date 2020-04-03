# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, P, Q):
    # write your code in Python 3.6
    prime_table = [False] * 2 + [True] * (N - 1)
    prime = []
    cnt = 0
    el = 2
    while el * el <= N:
        if prime_table[el] == True:
            prime.append(el)
            cnt += 1
            multiple = el * el
            while multiple <= N:
                prime_table[multiple] = False
                multiple += el
        el += 1
    
    while el <= N:
        if prime_table[el] == True:
            prime.append(el)
            cnt += 1
        el += 1
        
    semiprime = [0] * (N + 1)
    for i_former in range(cnt - 1):
        for i_latter in range(i_former, cnt):
            if prime[i_former] * prime[i_latter] > N:
                break
            semiprime[prime[i_former] * prime[i_latter]] = 1
            
    for i in range(1, N + 1):
        semiprime[i] += semiprime[i - 1]
        
    ans = [0] * len(P)
    for i in range(len(P)):
        ans[i] = semiprime[Q[i]] - semiprime[P[i] - 1]
    return ans
