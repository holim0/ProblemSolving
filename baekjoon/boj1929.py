m, n = map(int, input().split())


check ={}
check[1] = True
for i in range(2, int(n**(1/2))+1):
    if i in check: continue
    for j in range(i+i, n+1, i):
        check[j] = True

for i in range(m, n+1):
    if i not in check:
        print(i)