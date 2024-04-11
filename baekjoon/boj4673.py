check = [False for _ in range(10001)]

def genSelf(number):

    cur = number

    for n in str(number):
        cur += int(n)
    
    return cur

for i in range(1, 10001):
    if check[i]: continue

    num = i

    while num<=10000:
        nxt = genSelf(num)
        if nxt <=10000:
            check[nxt] = True
        num = nxt

for i in range(1, 10001):
    if not check[i]:
        print(i)
