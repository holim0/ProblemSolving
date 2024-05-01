n = int(input())

number =  list(map(int, input().split()))

accum = [number[0]]

for i in range(1, n):
    accum.append(accum[-1] + number[i])

answer = 0

for i in range(n-1):
    cur = number[i]
    sum = accum[-1] - accum[i]
    answer += cur * sum

print(answer)