 you can write to stdout for debugging purposes, e.g.
 # print("this is a debug message")

 def solution(A):
     # write your code in Python 3.6
     candidate = -1
     cnt = 0
     index = -1
     for i in range(len(A)):
         if cnt == 0:
             candidate = A[index]
             index = i
             cnt += 1
         else:
             if A[i] == candidate:
                 cnt += 1
             else:
                 cnt -= 1
                 
    leader_cnt = len([number for number in A if number == candidate])
    if leader_cnt <= len(A) // 2:
        return 0
    else:
        leader = candidate
        
    equi_leaders = 0
    cnt_so_far = 0
    for i in range(len(A)):
        if A[i] == leader:
            cnt_so_far += 1
        if cnt_so_far > (i+1) // 2 and leader_cnt - cnt_so_far > (len(A) - (i+1)) // 2:
            equi_leaders += 1
    return equi_leaders
