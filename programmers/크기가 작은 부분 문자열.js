function solution(t, p) {
    let answer = 0;
    
    let windowSize = p.length
    
    
    for(let i=0; i<t.length-windowSize+1; i++){
        let cur = t.substring(i, i+windowSize)
        
        cur = Number(cur)
        
        if(cur<=Number(p)){
            answer+=1
        }
        
        
    }
    return answer;
}