function solution(n, roads, sources, destination) {
    let answer = [];
    
    let g = {}
    
    for(let i=0; i<roads.length; i++){
        let [a, b] = roads[i]
        if(g[a]=== undefined){
            g[a] = [b]
        }else{
            g[a].push(b)
        }
        
        if(g[b]=== undefined){
            g[b] = [a]
        }else{
            g[b].push(a)
        }
    }
    let INF = Math.pow(10, 10)
    let cost = new Array(n+1).fill(INF)
    cost[destination] = 0
    let start = destination
    for(let i=0; i<sources.length; i++){
        let dest = sources[i]
        let q = [[start, 0]]
        
        while(q.length){
            let [cur, dist] = q.shift()
            let nxtList = g[cur]
            for(let j=0; j<nxtList.length; j++){
                let nxt = nxtList[j]
                if(cost[nxt] > dist+1){
                    cost[nxt] = dist+1
                    q.push([nxt, dist+1])
                }
            }

        }
    }
    
    for(let i=0; i<sources.length; i++){
        if (cost[sources[i]] === INF){
            answer.push(-1)
        }else{
            answer.push(cost[sources[i]])
        }
        
    }
    
    return answer;
}