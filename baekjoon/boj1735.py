a, b = map(int, input().split())
c, d = map(int, input().split())

def gcd(x, y):  # 최대공약수
    while y > 0:
        x, y = y, x % y
    return x


def lcm(x, y):
    return x * y / gcd(x, y)

down = b*d
up = a * d + b * c
g = gcd(down, up)
print(int(up/g), int(down/g))
