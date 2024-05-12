from itertools import permutations

n = int(input())

number = list(map(int, input().split()))


permu = list(permutations(number, len(number)))
answer = 0
for p in permu:
    p = list(p)
    cur_sum = 0
   
    for i in range(0, len(p)-1):
        s = abs(p[i]- p[i+1])
        cur_sum+=s

    
    answer = max(answer, cur_sum)

print(answer)
