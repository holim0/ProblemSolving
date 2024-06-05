function solution(x, y, n) {
    let answer = -1
    
    
    let visit ={}
    
    visit[y] = true
    
    let q = []

    q.push([y, 0])
    
    while(q.length){
        let [cur, cnt] = q.shift()
        
        if(cur===x){
            return cnt
        }
        
        let nxt = cur-n
        
        if(nxt>=x && !visit[nxt]){
            visit[nxt] = true
            q.push([nxt, cnt+1])
        }
        
        if(cur%2===0){
            nxt = cur/2
            if(nxt>=x &&!visit[nxt]){
                visit[nxt] = true
                q.push([nxt, cnt+1])
            }
        }
        
        if(cur%3===0){
            nxt = cur/3
            if(nxt>=x &&!visit[nxt]){
                visit[nxt] = true
                q.push([nxt, cnt+1])
            }
        }
        
        
    }    
    
    
    
    return answer;
}