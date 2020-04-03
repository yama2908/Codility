# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    ans = -1
    num_of_letters = 0
    num_of_digits = 0
    num_of_others = 0
    for letter in S:
        if letter.isalpha():
            num_of_letters += 1
        elif letter.isdigit():
            num_of_digits += 1
        elif letter == " ":
            if num_of_others == 0 and num_of_letters % 2 == 0 and num_of_digits % 2 == 1:
                ans = max(ans, num_of_letters + num_of_digits)
            num_of_letters = 0
            num_of_digits = 0
            num_of_others = 0
        else:
            num_of_others += 1
            
    if num_of_others == 0 and num_of_letters % 2 == 0 and num_of_digits % 2 == 1:
        ans = max(ans, num_of_letters + num_of_digits)
    return ans
