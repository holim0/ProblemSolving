function solution(number, k) {
    let stack = [];
    
    number = number.split("")
    
    for(let i=0; i<number.length; i++){
        let curValue = Number(number[i])
        if(i==0){
            stack.push(curValue)
        }else{
            while(stack.length && curValue>stack.at(-1) && k>0){
                k-=1
                stack.pop()
            }
            stack.push(curValue)       
        }
    }
    
    if(k!=0){
        while(k>0){
            k-=1
            stack.pop()
        }
    }
    let answer =""
    stack.forEach((s)=>{
        answer+= String(s)
    })
    
    
    
    
    return answer;
}