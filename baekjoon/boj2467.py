import sys
n = int(input())
number = list(map(int, input().split()))

answer = (0, 0)

diff = 1e10

p1, p2 = 0, n-1
a, b = 0, 0

while p1<p2:

    n1, n2 = number[p1], number[p2]

    sum = n1 + n2

    if abs(sum)<diff:
        diff = abs(sum)
        a, b = n1, n2
      
    if abs(n1)>abs(n2):
        p1+=1
    else:
        p2-=1
print(a, b)

