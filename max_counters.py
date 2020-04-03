# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # write your code in Python 3.6
    ans = [0] * N
    max_counter = 0
    current_max = 0
    for command in A:
        if 1 <= command <= N:
            if max_counter > ans[command - 1]:
                ans[command - 1] = max_counter    
            ans[command - 1] += 1

            if current_max < ans[command - 1]:
                current_max = ans[command - 1]
                    
        else:
            max_counter = current_max

    for index in range(N):
        if ans[index] < max_counter:
            ans[index] = max_counter
    return ans 
