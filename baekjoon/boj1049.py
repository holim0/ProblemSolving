n, m = map(int, input().split())



info = []
six_cost = []
cost = []
answer = 0
for _ in range(m):
    a, b = map(int, input().split())
    six_cost.append(a)
    cost.append(b)

min_six = min(six_cost)
min_cost = min(cost)


if min_six <= min_cost * 6:
    res = n%6
    answer  = (n//6) * min_six + min(res * min_cost, min_six) 
    print(answer)
else:
    answer = min_cost * n
    print(answer)