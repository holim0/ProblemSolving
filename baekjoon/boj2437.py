n = int(input())

w = list(map(int, input().split()))

w.sort()

answer = 1

for ww in w:
    if ww > answer:
        break # sum이 만들 수 없는 최소 무게
    answer += ww

print(answer)