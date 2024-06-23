function solution(k, score) {
    let answer = [];
    let winner = []
    
    for(let i=0; i<score.length; i++){
        if (i<k){
            winner.push(score[i])
            winner.sort((a, b) => a-b)
            answer.push(winner[0])
        }else{
            if(score[i]>winner[0]){
                winner[0] = score[i]
                winner.sort((a, b) => a-b)
                answer.push(winner[0])
            }else{
                answer.push(winner[0])
            }
        }
        
    }
    return answer;
}