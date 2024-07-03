function solution(food) {
    let answer = '';
    
    let value = []
    for (let i=1; i<food.length; i++){
        let divideValue = Math.floor(food[i]/2)
        
        for(let j=0; j<divideValue; j++){
            value.push(i.toString())
        }
    }
    
    value.push("0")
    
    for (let i=value.length-2; i>=0; i--){
        value.push(value[i])
    }
    
    answer = value.join("")
    return answer;
}