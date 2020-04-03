if res % 2 == 0:
    cail = res // 2 - 2
else:
    cail = res // 2 - 1

ans = []
if cail >= 0:
    q, r = cail // 4, (cail + 3) % 4
else:
    q, r = cail // 4, (cail - 1) % 4
while q != 0:
    if r == 0:
        ans += [0, 1]
    elif r == 1:
        ans += [1, 1]
    elif r == 2:
        ans += [0, 0]
    else:
        ans += [1, 0]
    if cail >= 0:
        r = (q + 3) % 4
    else:
        r = (q - 1) % 4
    q //= 4

if r == 0:
    ans += [0, 1]
elif r == 1:
    ans += [1, 1]
elif r == 2:
    ans += [0, 0]
else:
    ans += [1, 0]

if cail >= 0:
    ans += [1]
    
if ans[-1] == 0:
    if ans[-2] == 0:
        return ans[:-2]
    return ans[:-1]
else:
    return ans
