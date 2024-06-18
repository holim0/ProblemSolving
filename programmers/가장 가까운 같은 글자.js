function solution(s) {
    let answer = [];
    
    let maxIdx = {}
    let listS = s.split("")
    for(let i=0; i<listS.length; i++){
        let cur = listS[i]
        if (maxIdx[cur] === undefined){
            answer.push(-1)
            maxIdx[cur] = i
        }else{
            
            answer.push(i-maxIdx[cur])
            maxIdx[cur] = i
        }
    }
    
    return answer;
}