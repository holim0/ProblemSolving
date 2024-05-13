import sys
n = int(input())

number = []

for _ in range(n):
    num = int(input())
    number.append(num)

number = sorted(number)

check = {}

for num in number:
    check[num] = True

answer = 0 

max_value = max(number)

for i in range(n):
    for j in range(n):
        s, e = 0, n-1
        two_sum = number[i]+number[j]
        while s<=e:
            mid = (s+e)//2

            three_sum = two_sum + number[mid]

            if three_sum > max_value:
                e = mid-1

            elif three_sum < max_value:
                if three_sum in check:
                    answer = max(answer, three_sum)
                s = mid+1

            else:
                print(max_value)
                sys.exit()

print(answer)