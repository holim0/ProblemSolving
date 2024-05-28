function solution(board) {
    var answer = 0;
    
    b = []
    let sx =0
    let sy =0
    
    let w = board[0].length
    let h = board.length
    
    for(let i=0; i<board.length; i++){
        b.push([...board[i]])
    }
    for(let i=0; i<b.length; i++){
        for(let j=0; j<b[0].length; j++){
            if(b[i][j]=="R"){
                sx = i
                sy = j
            }
        }
    }
    
    let visit = []
    for(let i=0; i<b.length; i++){
        visit.push(Array(b[0].length).fill(false))
    }
    
    let q = []
    
    visit[sx][sy] = true
    
    q.push([sx, sy, 0])
    let dx = [0, 0, 1, -1]
    let dy = [1, -1, 0, 0]
    while(q.length !=0){
        let cur = q.shift()
        let cx = cur[0]
        let cy = cur[1]
        let curCnt = cur[2]
        
        if(b[cx][cy]=== "G"){
            return curCnt 
        }
        
        for(let i=0; i<4; i++){
            let nx = cx
            let ny = cy
            
            while (true){
                nx +=dx[i]
                ny +=dy[i]
                
                if((nx>=0 && nx<h && ny>=0 && ny<w) && b[nx][ny] !="D"){
                    continue
                }else{
                    nx-=dx[i]
                    ny-=dy[i]
                    break
                }
            }
            
            
            if(visit[nx][ny] === false){
                visit[nx][ny] = true
                q.push([nx, ny, curCnt+1])
            }
        }
        
        
        
        
    }
    
    
    return -1;
}