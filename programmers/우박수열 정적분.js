function cal(a, b, pos){
    
    let value = 0
    for(let i=a; i<b; i++){
        value += (pos[i] + pos[i+1])/2
        
    }
    return value
}


function solution(k, ranges) {
    let answer = [];
    let value = []
    let n = 0 
    value.push(k)
    while(true){
        if(k==1){
            break
        }
        if(k%2==0){
            k/=2
            value.push(k)
        }else{
            k = (k*3)+1
            value.push(k)
        }
        n+=1
        
    }
    ranges.forEach((r)=>{
        let [a, b] = r
        if (a>b+n){
            answer.push(-1.0)
            
        }else{
            let curValue = cal(a, b+n, value)
            answer.push(curValue)
        }
        
    })
    return answer;
}