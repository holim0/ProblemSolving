function solution(storey) {
    let answer = 0;
    
    while(storey>0){
        let remain = storey%10
        
        if(remain>5){
            answer+= (10-remain)
            storey = Math.floor(storey/10)
            storey+=1
            continue
        }
        if(remain<5){
            answer+=remain
            storey = Math.floor(storey/10)
            continue
        }
        
        if(remain===5){
            let nxt = (Math.floor(storey/10)) %10
            
            if(nxt>=5){
                storey = Math.floor(storey/10)
                storey+=1
            }else{
                storey = Math.floor(storey/10)
            }
            answer+=5
        }
        
    }
    return answer;
}