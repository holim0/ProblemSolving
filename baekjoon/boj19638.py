import heapq as hp
import sys
n, h, t = map(int, input().split())

tall =[]

q = []

for _ in range(n):
    tt = int(input())
    hp.heappush(q, -tt)


for i in range(1, t+1):
    curBig = hp.heappop(q)
    curBig*= (-1)
    if curBig<h:
        print("YES")
        print(i-1)
        sys.exit()
    if curBig !=1:
        curBig = curBig//2
        hp.heappush(q, -curBig)
    else:
        hp.heappush(q, -curBig)
        break


biggest = hp.heappop(q) * (-1)

if biggest>=h:
    print("NO")
    print(biggest)
else:
    print("YES")
    print(t)



    