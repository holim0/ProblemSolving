function checkStack(stack, curValue){
    if(stack.length===0) {return false}
    
    let stackTopValue = stack[stack.length-1][1]
    
    if (stackTopValue<curValue){
        return true
    }
    return false
    
    
}

function solution(numbers) {
    let numSize = numbers.length
    let answer = new Array(numSize).fill(-1)
    
    
    stack = []
    
    
    for(let i=0; i<numSize; i++){
        let curIdx = i
        let curValue = numbers[i]
        
        if(stack.length===0){
            stack.push([curIdx, curValue])
        }else{
            
            while(checkStack(stack, curValue)){
                let [topIdx, topVale] = stack.pop()
                answer[topIdx] = curValue
            }
            
            stack.push([curIdx, curValue])
            
            
        }
        
    }
    
    return answer;
}