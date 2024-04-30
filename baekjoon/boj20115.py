n = int(input())

number = list(map(int, input().split()))

number = sorted(number)

answer = number[-1]

answer+= round(float(sum(number[:-1])/2), 5)

print(answer)