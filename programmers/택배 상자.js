function solution(order) {
    let answer = 0;
    let stack =[]
    let oSize = order.length
    let containerNum = 1
    
    for(let i=0; i<oSize; i++){
        let curOrder = order[i]
        
        while(containerNum<=curOrder && containerNum<=oSize){
            stack.push(containerNum)
            containerNum+=1
        }
        if(stack.at(-1)!=curOrder){
            break
        }else{
            answer+=1
            stack.pop()
        }
        
    }
    

    return answer;
}