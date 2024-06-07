function solution(weights) {
    let answer = 0;
    let wSize = weights.length
    let cnt = {}
   
    weights.sort((a, b) => a-b)
    let noDouble = []
    weights.forEach((w)=>{
        if(!cnt[w]){
            cnt[w] = 1
            noDouble.push(w)
        }else{
            cnt[w] +=1
        }
    })
    
    
    for(let i =0; i<noDouble.length; i++){
        let value = noDouble[i]
        answer+= (cnt[value] * (cnt[value]-1))/2
        
        if(cnt[value*3/2]){
            answer+= (cnt[value] * cnt[value*3/2])
        }
        
        if(cnt[value*4/3]){
            answer+= (cnt[value] * cnt[value*4/3])
        }
        
        if(cnt[value*2]){
            answer+= (cnt[value] * cnt[value*2])
        }
        
    }
    
        
    
    return answer;
}