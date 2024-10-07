def solution(mat):
    answer = 0
    size = len(mat)
    
    dp = [[1e10] * size for _ in range(size)]
    
    for i in range(size-1):
        a, b, c = mat[i][0], mat[i][1], mat[i+1][1]
        dp[i][i+1] = a*b*c
    
    for i in range(size):
        dp[i][i] = 0
    
    for l in range(3, size+1):
        for i in range(size-l+1):
            left = i
            right = left+l-1 
            
            for cur in range(left, right):
                leftValue = dp[left][cur]
                rightValue = dp[cur+1][right]
                mulValue = mat[left][0] * mat[cur][1] * mat[right][1]
                totalSum = leftValue+rightValue+mulValue
                dp[left][right] = min(dp[left][right], totalSum)
            
    
    answer = dp[0][size-1]
    return answer