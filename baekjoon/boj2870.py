n = int(input())

number = []

text = []

for _ in range(n):
    t = input()
    text.append(t)
cur = ""
for t in text:
    for s in t:
        if s.isdigit():
            cur+=s
        else:
            if cur != "":
                number.append(int(cur))
                cur = ""
    if cur !="":
        number.append(int(cur))
    
    cur = ""



number = sorted(number)

for n in number:
    print(n)
