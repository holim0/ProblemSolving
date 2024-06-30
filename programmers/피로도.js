let answer = -1
let dunSize = 0

function checkAllVisit(visit){
    
    for(let i=0; i<dunSize; i++){
        if(visit[i]===false) {
            return false
        }
    }
    return true
}
function getAnswer(hp, visitCnt, dungeons, visit){
    
    
        answer = Math.max(answer, visitCnt)
        
    
    
    for(let i=0; i<dunSize; i++){
        if(visit[i]===false){
            let [minHp, useHp] = dungeons[i]
            if(hp>=minHp){
                visit[i] = true
                getAnswer(hp-useHp, visitCnt+1, dungeons, visit)
                visit[i]= false
            }
        }
    }
    
}

function solution(k, dungeons) {
    
    dunSize = dungeons.length
    
    let visit = new Array(dunSize).fill(false)
    
    for(let i=0; i<dunSize; i++){
        let [minHp, useHp] = dungeons[i]
        if(k>=minHp){
            visit[i]= true
            getAnswer(k-useHp, 1, dungeons, visit)
            visit[i] = false
        }
    }    
    return answer;
}