let order = []
let origin = ['A', 'E', 'I', 'O', 'U']
function getValue(curWord){
    
    if(curWord.length<=5){
        order.push(curWord)
    }else{
        return 
    }
    
    for(let i=0; i<5; i++){
        getValue(curWord + origin[i])
    }
    
}

function solution(word) {
    let answer = 0;
    

    for(let i=0;i <5; i++){
        let cur = origin[i]
        getValue(cur)
    }
    for(let i=0;i <order.length; i++){
        let cur = order[i]
        
        if(word===cur){
            return i+1
        }
    }
    return answer;
}