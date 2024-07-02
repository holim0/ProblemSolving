function solution(cards) {
    let answer = 0;
    let cnt = []
    let cardSize= cards.length    
    
    let q = []
    
    let check = new Array(cardSize).fill(false)
    
    for(let i=0; i<cardSize; i++){
        if(check[i] === false){
            q = []
            check[i] = true
            q.push([i, cards[i]-1])
            let curCnt = 1
            while(q.length){
                let [cur, nxt] = q.shift()
                
                if(check[nxt]=== false){
                    check[nxt] = true
                    curCnt+=1
                    q.push([nxt, cards[nxt]-1])
                }
            }
            cnt.push(curCnt)   
        }
    }
    if(cnt.length===1){
        return 0
    }
    cnt.sort((a, b) => b-a)
    
    answer = cnt[0] * cnt[1]
    return answer;
}