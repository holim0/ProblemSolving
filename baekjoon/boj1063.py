k, d, n = input().split()

n = int(n)

oper ={
    "R": (0, 1),
    "L": (0, -1),
    "B": (1, 0),
    "T": (-1, 0),
    "RT": (-1, 1),
    "LT": (-1, -1),
    "RB": (1, 1),
    "LB": (1, -1)
}
row = {
    "1": 8,
    "2": 7,
    "3": 6,
    "4": 5,
    "5": 4, 
    "6": 3, 
    "7": 2, 
    "8": 1
}

col = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6, 
    "G": 7, 
    "H": 8
}


k =list(k)
d = list(d)
kx, ky = row[k[1]], col[k[0]]
dx, dy = row[d[1]], col[d[0]]

for _ in range(n):
    move_info = input()

    a, b = oper[move_info]

    nkx, nky = kx+a, ky+b

    if 1<=nkx<=8 and 1<=nky<=8:
        if nkx == dx and nky == dy:
            ndx, ndy = dx+a, dy+b

            if 1<=ndx<=8 and 1<=ndy<=8:
                kx, ky = nkx, nky
                dx, dy = ndx, ndy
            else:
                continue

        else:
            kx, ky = nkx, nky

    else:
        continue

toAlpha = {
    "1": "A",
    "2": "B",
    "3": "C",
    "4": "D",
    "5": "E",
    "6": "F", 
    "7": "G", 
    "8": "H"
}

print(toAlpha[str(ky)]+str(9-kx))
print(toAlpha[str(dy)]+ str(9-dx))