function solution(cards1, cards2, goal) {
    let answer = '';
    
    for(let i=0; i<goal.length; i++){
        if(goal[i] === cards1[0]){
            cards1.shift()
            continue
        }
        
        if (goal[i]===cards2[0]){
            cards2.shift()
            continue
        }
        
        return "No"
    }

    
    return "Yes";
}