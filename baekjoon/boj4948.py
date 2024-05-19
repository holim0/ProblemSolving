sosu = [True for _ in range(250000)]
sosu[1] = False
for i in range(2, 250000):
    if not sosu[i]: continue
    for j in range(2*i, 250000, i):
        sosu[j] = False


while True:

    n = int(input())
    if n==0: break

    cnt =0

    for i in range(n+1, 2*n+1):
        if sosu[i]: cnt+=1

    print(cnt)