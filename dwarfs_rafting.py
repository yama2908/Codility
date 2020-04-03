# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, S, T):
    # write your code in Python 3.6
    front_left = (N // 2) ** 2
    front_right = (N // 2) ** 2
    back_left = (N // 2) ** 2
    back_right = (N // 2) ** 2
    for s in S.split():
        row = int(s[:-1]) - 1
        column = ord(s[-1]) - ord('A')
        if row < N // 2:
            if column < N // 2:
                front_left -= 1
            else:
                back_left -= 1
        else:
            if column < N // 2:
                front_right -= 1
            else:
                back_right -= 1
    ans_fl = min(front_left, back_right)
    ans_fr = min(front_right, back_left)
    ans_bl = min(front_right, back_left)
    ans_br = min(front_left, back_right)
    for t in T.split():
        row = int(t[:-1]) - 1
        column = ord(t[-1]) - ord('A')
        if row < N // 2:
            if column < N // 2:
                ans_fl -= 1
                if ans_fl < 0:
                    return -1
            else:
                ans_bl -= 1
                if ans_bl < 0:
                    return -1
        else:
            if column < N // 2:
                ans_fr -= 1
                if ans_fr < 0:
                    return -1
            else:
                ans_br -= 1
                if ans_br < 0:
                    return -1
    return ans_fl + ans_fr + ans_bl + ans_br
