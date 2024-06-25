function isSame(l, r){
    let leftSize = Object.keys(l).length
    let rightSize = Object.keys(r).length
    
    if (leftSize===rightSize){
        return true
    }
    
    return false
}

function solution(topping) {
    let answer = 0
    let topSize = topping.length
    let rightCnt = {}
    let rightSize = 0
    let leftCnt ={}
    let leftSize = 0
    
    leftCnt[topping[0]] = 1
    leftSize+=1
    
    for(let i=1; i<topSize; i++){
        let curTopping = topping[i]
        if(!rightCnt[curTopping]){
            rightCnt[curTopping] = 1
            rightSize+=1
        }else{
            rightCnt[curTopping]+=1
        }
    }
    
    
    
    for(let i=0; i<topSize-1; i++){
        let curTopp = topping[i]
        if(i===0){
            if(rightSize===leftSize){
                answer+=1
            }
        }else{
            rightCnt[curTopp]-=1
            if(rightCnt[curTopp]===0){
                rightSize-=1
            }
            
            if(leftCnt[curTopp]=== undefined ||leftCnt[curTopp]=== 0){
                leftCnt[curTopp] = 1
                leftSize+=1
            }else{
                leftCnt[curTopp]+=1
            }
            
            if(leftSize=== rightSize){
                answer+=1
            }
            
        }
        
        
        
    }
    
    return answer;
}