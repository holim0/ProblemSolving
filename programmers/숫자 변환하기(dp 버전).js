function solution(x, y, n) {
    var answer = 0;
    let inf = 100000000000
    
    let dp = new Array(y+1).fill(inf)
    
    dp[x] = 0
    
    for(let i=x+1; i<=y; i++){
        
        if(i-n>=x){
            dp[i] = Math.min(dp[i], dp[i-n]+1)
        }
        if(i%2===0 && i/2>=x){
            dp[i] = Math.min(dp[i], dp[i/2]+1)
        }
        if(i%3===0 && i/3>=x){
            dp[i] = Math.min(dp[i], dp[i/3]+1)
        }
    }
    if(dp[y]===inf){ return -1}
    return dp[y];
}