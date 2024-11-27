n = int(input())
liquid = list(map(int, input().split()))

liquid.sort()

dist = 1e10
a, b, c = 0, 0, 0
for i in range(n-2):
    baseValue = liquid[i] 

    l, r = i+1, n-1
    
    while l<r:
        resultSum = baseValue + liquid[l] + liquid[r]

        if dist>abs(resultSum):
            dist = abs(resultSum)
            a, b, c = baseValue, liquid[l], liquid[r]
        
        if resultSum<0:
            l+=1
        else:
            r-=1

print(a, b, c)


