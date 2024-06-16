a, b, c = map(int, input().split())

mod = 2147483647
answer = 1


def fastMul():
    global b
    global a
    global c
    result = 1

    while b:
        if b%2==1:
            result = (result *a) % c
        
        a = (a*a) %c
        b= b//2
    
    return result

print(fastMul())

