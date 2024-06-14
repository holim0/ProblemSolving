import sys
n, k = map(int, input().split())

a, b =0, n

if k==0:
    print("B" *n)
    sys.exit()


while a*b <k and b>0:
    a+=1
    b-=1

if b==0:
    print(-1)
    sys.exit()

res = k - (a - 1) * b
s = "A" * (a-1) + "B" *(b-res) + "A" + "B" * res 
print(s)