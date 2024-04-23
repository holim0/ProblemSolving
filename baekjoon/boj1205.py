import sys
n, score, p = map(int, input().split())

answer = -1

if n ==0:
    print(1)
    sys.exit()

rank = list(map(int, input().split()))

for i in range(len(rank)):
    if rank[i]<=score:
        if len(rank)+1 <=p:
            print(i+1)
            sys.exit()

        else:
            if score > rank[-1]:
                print(i+1)
                sys.exit()
            else:
                print(-1)
                sys.exit()


if len(rank) +1 <=p:
    print(len(rank)+1)
else:
    print(-1)
