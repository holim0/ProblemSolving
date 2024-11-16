a = input()
b = input()


a = list(a)
b = list(b)

a.insert(0, 0)
b.insert(0, 0)

lcs = [[0] * len(b) for _ in range(len(a))]


for i in range(1, len(a)):
    aValue = a[i]
    for j in range(1, len(b)):
        bValue = b[j]

        if aValue == bValue:
            lcs[i][j] = lcs[i-1][j-1] + 1

        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])


print(lcs[len(a)-1][len(b)-1])
