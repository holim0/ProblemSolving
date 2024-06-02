function solution(park, routes) {
    let answer = [];
    let dir = {
        "N": [-1, 0],
        "S": [1, 0],
        "W": [0, -1],
        "E": [0, 1]
    }
    let w = park[0].length
    let h = park.length
    let cx, cy;
    let newPark = []
    
    park.forEach((p)=>{
        let row = p.split("")
        newPark.push(row)
    })
    
    for(let i=0; i<h; i++){
        for(let j=0; j<w; j++){
            if(newPark[i][j] == "S"){
                cx = i
                cy = j
            }
        }
    }
    routes.forEach((order) => {
        let curDir = order.split(" ")[0]
        let moveCnt = order.split(" ")[1]
        
        let nx = cx
        let ny = cy
        let isStop = false
        while(moveCnt>0){
            nx += dir[curDir][0]
            ny += dir[curDir][1]
            if (nx<0 || nx>=h || ny<0 || ny>=w){
                isStop = true
                break
            }else{
                if(newPark[nx][ny] === "X"){
                    isStop = true
                    break
                }
            }
            
            moveCnt-=1
        }
        
        if(isStop === false){
            cx = nx
            cy = ny
        }
        
        
    })
    
    answer.push(cx)
    answer.push(cy)
    
    
    return answer;
}