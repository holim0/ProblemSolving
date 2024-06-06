function checkWin(b, target){
    
    let targetStr = target + target +target
    let cur = ""
    for(let i=0; i<3; i++){
        cur = b[i][0] + b[i][1] + b[i][2]
        if(cur=== targetStr) {return true}
    }
    
    for(let i=0; i<3; i++){
        cur = b[0][i] + b[1][i] + b[2][i]
        if(cur=== targetStr) {return true}
    }
    
    cur = b[0][0] + b[1][1] + b[2][2]
    if(cur=== targetStr) {return true}
    
    cur = b[2][0] + b[1][1] + b[0][2]
    if(cur=== targetStr) {return true}
    
    return false
    
    
}


function solution(board) {
    let answer = 0;
    
    let [xCnt, oCnt] = [0, 0]
    let map =[]
    
    board.forEach((b)=>{
        map.push(b.split(""))
    })
    board.forEach((b) =>{
        for(const i in b){
            if(b[i]==="O"){
                oCnt+=1
            }
            if(b[i]==="X"){
                xCnt+=1
            }
        }
        
    })
    if(!(oCnt===xCnt || oCnt === xCnt+1)) {return 0}
    
    if (checkWin(map, "X") && checkWin(map, "O")) {return 0}
    
    if(checkWin(map, "O") && oCnt-xCnt !==1){ return 0}
    
    if(checkWin(map, "X") && oCnt!=xCnt){return 0}
    
    return 1
    
}