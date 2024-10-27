n, k = map(int, input().split())

h = list(map(int, input().split()))

diff =[]

for i in range(len(h)-1):
    diff.append(h[i+1]-h[i])

diff.sort(reverse=True)
answer = sum(diff)

for i in range(k-1):
    answer-=diff[i]

print(answer)