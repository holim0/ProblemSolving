function solution(maps) {
    let answer = 0;
    
    let q = []
    
    let check = []
    
    for (let i=0; i<maps.length; i++){
        check.push(new Array(maps[0].length).fill(false))
    }
    let n = maps.length
    let m = maps[0].length
    check[0][0] = true
    q.push([0, 0, 1])
    let dx= [0, 0, -1, 1]
    let dy = [-1, 1, 0, 0]
    while (q.length){
        let [cx, cy, dist] = q.shift()
        
        if (cx==n-1 && cy==m-1){
            return dist
        }
        
        
        for(let k=0; k<4; k++){
            let [nx, ny] = [cx+dx[k], cy+dy[k]]
            
            if(nx>=0 && nx<n && ny>=0 && ny<m && check[nx][ny]===false && maps[nx][ny]===1){
                check[nx][ny] = true
                q.push([nx, ny, dist+1])
            }
        }
        
        
    }
    
    return -1;
}