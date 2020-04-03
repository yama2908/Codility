# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    length = len(A)
    maxi = max(A)
    count = {}
    for element in A:
        count[element] = count.get(element, 0) + 1
        
    divisors = {}
    for element in A:
        divisors[element] = [1]

    divisor = 2
    while divisor * divisor <= max(A):
        multiple = divisor
        while multiple  <= max(A):
            if multiple in divisors and not divisor in divisors[multiple]:
                divisors[multiple].append(divisor)
            multiple += divisor
        divisor += 1

    for element in divisors:
        temp = [element // div for div in divisors[element]]
        temp = [item for item in temp if item not in divisors[element]]
        divisors[element].extend(temp)

    ans = []
    for element in A:
        ans.append(len(A) - sum([count.get(div, 0) for div in divisors[element]]))
    return ans
