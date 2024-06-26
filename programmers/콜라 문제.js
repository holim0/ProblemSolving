function solution(a, b, n) {
    let answer = 0;
    
    while(n>=a){
        let mok = Math.floor(n/a)
        let mod = Math.floor(n%a)
        
        answer+= (mok*b)
        
        n = mok*b + mod
    }
    
    return answer;
}