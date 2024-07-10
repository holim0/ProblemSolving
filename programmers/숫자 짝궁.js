function solution(X, Y) {
    let answer = '';
    let cnt = new Array(10).fill(0)
    let answerList = []
    for(let i=0; i<X.length; i++){
        let cur = Number(X[i])
        cnt[cur]+=1
    }
    
    for(let i=0; i<Y.length; i++){
        let cur = Number(Y[i])
        if(cnt[cur]>0){
            answerList.push(cur)
            cnt[cur]-=1
        }
    } 
    answerList.sort((a, b) => b-a)
    
    
    
    if(answerList.length===0){
        return "-1"
    }
    
    for(let i=0; i<answerList.length; i++){
        answer+= answerList[i].toString()
    }
    if(Number(answer)===0){
        return "0"
    }
    return answer;
}