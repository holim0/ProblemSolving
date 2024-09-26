n = int(input())
k = int(input())

pos = list(map(int, input().split()))
pos.sort()

diff = []

for i in range(len(pos)-1):
    diff.append(pos[i+1]-pos[i])


diff.sort()

answer = 0 

for i in range(len(diff)-k+1):
    answer+=diff[i]
print(answer)