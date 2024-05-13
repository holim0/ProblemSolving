import sys
n = int(input())

number = []

for _ in range(n):
    num = int(input())
    number.append(num)

number = sorted(number)
summ = set()

for i in range(n):
    for j in range(n):
        summ.add(number[i] + number[j])

summ = list(summ)
summ = sorted(summ)

def find(target):
    global summ
    s, e = 0, len(summ)
    while s<=e:

        mid = (s+e)//2

        if summ[mid] == target:
            return True
        
        elif summ[mid] <target:
            s = mid+1

        elif summ[mid] > target:
            e = mid-1

    return False
        

for i in range(n-1, -1, -1):
    for j in range(0, i+1):
        diff = number[i] - number[j]

        if find(diff):
            print(number[i])
            sys.exit()