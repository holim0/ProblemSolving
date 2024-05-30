function solution(players, callings) {
    let answer = [];
    let nameToOrder = {}
    let orderToName = {}
    for(let i=0; i<players.length; i++){
        let name = players[i]
        nameToOrder[name] = i
        orderToName[i] = name
    }
    
    callings.forEach((curCallPlayer) =>{
        let curCallPlayerOrder = nameToOrder[curCallPlayer]
        let beforePlayerName = orderToName[curCallPlayerOrder-1]
        
        nameToOrder[curCallPlayer] = curCallPlayerOrder-1
        nameToOrder[beforePlayerName] = curCallPlayerOrder
        orderToName[curCallPlayerOrder]  = beforePlayerName
        orderToName[curCallPlayerOrder-1] = curCallPlayer
        
    })
    
    let tmp = []
    for (name in nameToOrder){
        tmp.push([nameToOrder[name], name])
    }
    tmp.sort((a, b) => a[0]-b[0])
    for(let i=0; i<tmp.length; i++){
        let curName = tmp[i][1]
        answer.push(curName)
    }
    return answer;
}