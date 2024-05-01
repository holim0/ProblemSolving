import sys
from collections import Counter
string  =input()
string = list(string)

word_cnt = Counter(string)

mid = ""
hol = 0
for alpha, cnt in list(word_cnt.items()):
    if cnt % 2 ==1:
        hol+=1
        mid = alpha
        if hol>=2:
            print("I'm Sorry Hansoo")
            sys.exit()

result = ""
for alpha, cnt in sorted(list(word_cnt.items())):
    result += (alpha * (cnt//2))

answer = result + mid + result[::-1]
print(answer)

