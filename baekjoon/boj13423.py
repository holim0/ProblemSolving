t = int(input())

for _ in range(t):
    n = int(input())
    number = list(map(int, input().split()))
    number = sorted(number)
    answer = 0

    for i in range(1, n-1):
        b = number[i]

        p1, p2 = 0, n-1

        while p1<i and p2>i:
            
            sum = number[p1] + number[p2]

            if sum == 2*b:
                answer +=1
                p1+=1
                p2-=1

            elif sum > 2*b:
                p2-=1
            elif sum < 2*b:
                p1+=1
    
    print(answer)

