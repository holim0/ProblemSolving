n = int(input())

tree = []

for _ in range(n):
    t = int(input())
    tree.append(t)

diff = []

for i in range(n-1):
    diff.append(tree[i+1]-tree[i])

curGcd = diff[0]


def getGcd(a, b):

    while b!=0:
        r = a%b
        a = b
        b = r

    return a

for i in range(1, len(diff)):
    curGcd = getGcd(curGcd, diff[i])

cnt = tree[-1] - tree[0]+1

total =0

if cnt%curGcd ==0:
    total = cnt//curGcd

else:
    total = cnt//curGcd+1

print(total-n)