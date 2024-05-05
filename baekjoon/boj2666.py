n = int(input())

o1, o2 = map(int, input().split())
m =int(input())
use = []

for _ in range(m):
    u =int(input())
    use.append(u)


dp = [[[-1 for _ in range(21)] for _ in range(21)] for _ in range(21)]

def find(depth, open1, open2):
    if depth == m:
        return 0
    
    if dp[open1][open2][depth] != -1:
        return dp[open1][open2][depth]
    
    
    open1_cnt = find(depth+1, use[depth], open2) + abs(open1-use[depth])
    open2_cnt = find(depth+1, open1, use[depth]) + abs(open2-use[depth])
    dp[open1][open2][depth] = min(open1_cnt, open2_cnt)
    
    return dp[open1][open2][depth]

print(find(0, o1, o2))
