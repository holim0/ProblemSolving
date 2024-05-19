import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):

    s1 = []
    s2 = []

    stringValue = input().rstrip("\n")

    for value in stringValue:
        if value== "<":
            if s1:
                s2.append(s1[-1])
                s1.pop()
            
        elif value == "-":
            if s1:
                s1.pop()
        elif value == ">":
            if s2:
                s1.append(s2[-1])
                s2.pop()
        else:
            s1.append(value)

    answer = ""
    
    answer = "".join(s1)
   
    s2 = s2[::-1]
    answer += "".join(s2)
    
    print(answer)