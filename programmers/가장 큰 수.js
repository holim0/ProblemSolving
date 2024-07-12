function solution(numbers) {
    let answer = '';
    let strNum = []
    
    for(let i =0; i<numbers.length; i++){
        strNum.push(numbers[i].toString())
        
    }
    
    strNum.sort((a, b)=> (b+a) - (a+b) )
    
    answer = strNum.join("")
    
    if(answer[0] === "0"){
        return "0"
    }
    return answer;
}