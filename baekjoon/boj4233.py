import sys
input = sys.stdin.readline

def isPrime(cur):

    if cur==2: return False
    end = int(cur**(1/2))
    for i in range(2, end+1):
        if cur % i == 0: return False
    return True

def fastExponentiation(a, x, n):    # a^x mod n
    y = 1
    while x > 0:
        if x & 1  == 1:         # 지수의 LSB가 1인지 확인
            y = (a * y) % n     # Multiply Operation
        a = (a * a) % n         # Square Operation
        x = x >> 1
    return y
while True:
    p, a = map(int, input().split())
    if p==0 and a==0: break
    if (isPrime(p)):
        print("no")
        continue

    value = fastExponentiation(a, p, p)


        
    
    if value==a:
        print("yes")
    else:
        print("no")