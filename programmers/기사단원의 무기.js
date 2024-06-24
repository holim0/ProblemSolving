function getValue(number){
    
    let cnt = 0
    
    for(let i = 1 ; i <= Math.sqrt(number) ; i++){
        if(number % i === 0) {
            cnt+=1
            if(number / i != i){
                cnt+=1
            }
        }
    }
    return cnt
}

function solution(number, limit, power) {
    let answer = 0;
    
    for(let i=1; i<=number; i++){
        let cnt = getValue(i)

        if(cnt<=limit){
            answer+=cnt
        }else{
            answer+=power
        }
    }
    
    return answer;
}