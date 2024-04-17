import sys
n = int(input())

if n == 1:
    print(1)
    sys.exit()

p1, p2 = 1, 1


accum = [1]
answer = 0



while p1<=p2 and p1<=n and p2<=n:

    curSum = 0
    
    curSum = ((p1+p2) * (p2-p1+1)) //2
    
    if curSum == n:
        
        answer+=1
        p1+=1
    elif curSum > n:
        p1+=1
    elif curSum < n:
        p2+=1

print(answer)