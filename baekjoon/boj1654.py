k, n = map(int, input().split())

lan = []

for i in range(k):
    value = int(input())
    lan.append(value)

start, end = 1, max(lan)

while start <= end:

    mid = (start + end)//2

    make_sum = 0

    for l in lan:
        make_sum += (l//mid)

    if make_sum>=n:
        start = mid+1

    else:
        end = mid - 1

print(end)