dna = input()
dna = list(dna)

dnaSize = len(dna)

dp = [[0] * dnaSize for _  in range(dnaSize)]


for size in range(2, dnaSize+1):
    for i in range(dnaSize):
        s, e = i, i+size-1
        if e>=dnaSize: break
        
        if (dna[s]=="a" and dna[e]=="t"):
            dp[s][e] = dp[s+1][e-1] + 2 
        
        elif (dna[s]=="g" and dna[e]=="c"):
            dp[s][e] = dp[s+1][e-1] + 2
        
        for k in range(s, e):
            value = dp[s][k] + dp[k+1][e]
            dp[s][e] = max(dp[s][e], value)



print(dp[0][dnaSize-1])
