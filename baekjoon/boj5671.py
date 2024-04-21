import sys

def check(number):
    
    number = str(number)
    dict = {}

    for n in number:
        if n not in dict:
            dict[n] = 1
        else:
            return False
    return True

while True:
    try:
        n, m = map(int, input().split())
        answer =0
        for i in range(n, m+1):
            if check(i):
                answer+=1
        
        print(answer)
    except EOFError:
        break




