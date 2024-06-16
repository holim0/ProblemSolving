function gcd(a, b){
    while(b > 0){
    let r = a % b;
    a = b;
    b = r;
  }
  return a;
    
}

function checkAnswer(agcd, arrayA, bgcd, arrayB){
    
    let isAnswer = true
    let list = []
    for(let i=0; i<arrayB.length; i++){
        if(arrayB[i]%agcd===0){
            isAnswer = false
            break
        }
    }
    
    if(isAnswer){
        list.push(agcd)
    }
    
    isAnswer = true
    for(let i=0; i<arrayA.length; i++){
        if(arrayA[i]%bgcd===0){
            isAnswer = false
            break
        }
    }
    
    if(isAnswer){
        list.push(bgcd)
    }
    
    if(list.length==0){
        return 0
    }
    
    return Math.max(...list)
    
    
}


function solution(arrayA, arrayB) {
    let answer = 0;
    
    let agcd = arrayA[0]
    let bgcd = arrayB[0]
    
    for(let i=0; i<arrayA.length; i++){
    
        agcd = gcd(agcd, arrayA[i])
    }
    for(let i=0; i<arrayB.length; i++){
        bgcd = gcd(bgcd, arrayB[i])
    }
    
    
    
    answer = checkAnswer(agcd, arrayA, bgcd, arrayB)
    return answer;
}