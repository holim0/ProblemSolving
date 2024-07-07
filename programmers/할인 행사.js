function checkValid(want, goalCnt, curSlidingCnt){
    for(let i=0; i<want.length; i++){
        let curWant = want[i]
        if (curSlidingCnt[curWant] === undefined){
            return false
        }
        if(goalCnt[curWant]>curSlidingCnt[curWant]){
            return false
        }
    }
    return true
    
}

function solution(want, number, discount) {
    let answer = 0;
    let goalCnt = {}
    let wantSize = want.length
    
    for(let i=0; i<wantSize; i++){
        goalCnt[want[i]] = number[i]
    }
    
    let curSlidingCnt = {}
    
    for(let i=0; i<10; i++){
        let curName = discount[i]
        if(curSlidingCnt[curName]=== undefined){
            curSlidingCnt[curName] = 1
        }else{
            curSlidingCnt[curName]+=1
        }
    }
    
    let s=0;
    let e=9;
    
    while (e<discount.length){
        
        if(checkValid(want, goalCnt, curSlidingCnt)){
            answer+=1
        }
        
        s+=1
        e+=1
        
        if(e<discount.length){
            curSlidingCnt[discount[s-1]]-=1
            
            if(curSlidingCnt[discount[e]] === undefined){
                curSlidingCnt[discount[e]] = 1
            }else{
                curSlidingCnt[discount[e]]+=1
            }
        }
        
        
    }
    
    
    
    return answer;
}