
function solution(scores) {
    let answer = 0;
    
    let scoresWithSum = []
    let [ta, tb] = scores[0]
    let tSum = ta+tb
    

    
    scores.sort((a, b)=> b[0]-a[0] || a[1]-b[1])
    
    let maxb = 0
    for(let i=0; i<scores.length; i++){
        let [ca, cb]= scores[i]
        if (ta<ca && tb<cb){
            return -1
        }
        if (cb>=maxb){
            maxb = cb
            if(ca+cb>tSum){
                answer+=1
            }
        }
    }
    return answer+1;
}