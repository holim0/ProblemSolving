import sys
cryto = input()

alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
         "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u"
         , "v", "w", "x", "y", "z"]

size = len(alpha)

n = int(input())

word = []

for _ in range(n):
    w = input()
    word.append(w)

for i in range(0, size):
    cur_s = ""
    for c in cryto:
        cur_idx = alpha.index(c)
        nxt_idx = (cur_idx + i)%size
        cur_s += alpha[nxt_idx]
    
    for w in word:
        if w in cur_s:
            print(cur_s)
            sys.exit()