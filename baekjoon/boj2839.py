import sys

n = int(input())

answer = -1

if n>=5:
    max_five= n//5

    for i in range(max_five, -1, -1):
        s = n-5*i
        if s%3 == 0:
            answer = i + (s/3)
            print(int(answer))
            sys.exit() 
    
    print(-1)
     

else:
    if n%3 == 0:
        answer = int(n/3)
        print(int(answer))

    else:
        print(-1)
