s = input()

number = []
oper = []
value =""
for i in range(len(s)):
    
    if s[i] =="+" or s[i] =="-":
        oper.append(s[i])
        number.append(int(value))
        value = ""
    else:
        value += s[i]
number.append(int(value))

answer = []
minus = []
temp = 0

for i in range(len(number)):
    if i==0:
        answer.append(number[i])
        continue

    if oper[i-1] == "+":
        last = answer.pop()
        answer.append(last + number[i])
    else:
        answer.append(number[i])

real_answer = 0

for i in range(len(answer)):
    if i==0: real_answer += answer[i]

    else:
        real_answer -= answer[i]

print(real_answer)