const checkHamburger = (stack) =>{
    let curLen = stack.length
    let [a, b, c, d] = [stack[curLen-4], stack[curLen-3], stack[curLen-2], stack[curLen-1]]
    
    if(a==1 && b ==2 && c==3 && d == 1){
        return true
    }
    return false
}

function solution(ingredient) {
    let answer = 0;
    let stack = []
    
    ingredient.forEach((ingre) =>{
        stack.push(ingre)
        if(stack.length>=4){
            if(checkHamburger(stack)){
                answer+=1
                stack.pop()
                stack.pop()
                stack.pop()
                stack.pop()
            }
        }
    })
    
    
    return answer;
}