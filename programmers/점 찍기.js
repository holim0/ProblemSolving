function solution(k, d) {
    let answer = 0;
    
    let maxValue = d
    
    for(let i=0; i<=d; i++){
        if(i%k===0){
            let remain = (d*d) - (i*i)
            remain = Number(Math.floor(Math.sqrt(remain)))
            answer+= (Math.floor(remain/k))+1
        }
    }
    return answer;
}