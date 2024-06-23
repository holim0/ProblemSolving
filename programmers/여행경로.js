let answer = [];
let visit = []

function checkAllVisit(size){
    
    for(let i=0; i<size; i++){
        if(visit[i]===false){
            return false
        }
    }
    return true
}

function getRoute(now, route, tickets){
    
    if(checkAllVisit(tickets.length)){
        answer.push(route)
    }
    
    for(let i=0; i<tickets.length; i++){
        let [curfrom, curto] = tickets[i]
        
        if(now === curfrom && !visit[i]){
            visit[i] = true
            getRoute(curto, [...route, curto], tickets)
            visit[i] = false
        }
    }
    
    
}

function solution(tickets) {

    
    visit = new Array(tickets.length).fill(false)
    getRoute("ICN", ['ICN'], tickets)
    answer.sort()
    return answer[0]
}