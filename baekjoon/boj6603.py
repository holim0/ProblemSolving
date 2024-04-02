from itertools import combinations
while True:
    number = list(map(int, input().split()))

    if number[0] == 0: break

    number = number[1:]

    answer = list(combinations(number, 6))

    for a in answer:
        print(" ".join(str(b) for b in a))
    
    print()