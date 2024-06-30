function getSum(arr, s, e){
    let minValue = Infinity
    for(let i=s; i<e; i++){
        minValue = Math.min(arr[i], minValue)
    }
    return (minValue * (e-s))
}

function solution(k, m, score) {
    let answer = 0;
    
    let sortedScore = [...score].sort((a, b)=> b-a)
    for(let i=0; i<score.length; i+=m){
        if (i+m<=score.length){
            answer+=getSum(sortedScore, i, i+m)
        }
        
    }
    
    return answer;
}