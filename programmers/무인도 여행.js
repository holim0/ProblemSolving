function solution(maps) {
    let answer = [];
    let q = []
    let w = maps[0].length
    let h = maps.length
    let check = []
    let newMap =[]
    for(let i=0;i<h; i++){
        check.push(new Array(w).fill(false))
    }
    
    maps.forEach((m)=>{
        newMap.push(m.split(""))
    })
    let dx = [1, -1, 0, 0]
    let dy = [0, 0, -1, 1]
    for(let i=0;i<h; i++){
        for(let j=0; j<w; j++){
            if(newMap[i][j]=== "X" || check[i][j]) { continue}
            let cnt = 0
            check[i][j] = true
            q.push([i, j])
            
            while(q.length){
                let [cx, cy] = q.shift()
                
                cnt+=Number(newMap[cx][cy])
                
                
                for(let k=0; k<4; k++){
                    let [nx, ny] = [cx+dx[k], cy+dy[k]]
                    
                    if(nx>=0 && nx<h && ny>=0 && ny<w && !check[nx][ny] && newMap[nx][ny]!="X"){
                        check[nx][ny] = true
                        q.push([nx, ny])
                    }
                }    
            }
            answer.push(cnt)
            
            
        }
    }
    
    
    if(answer.length===0) return [-1]
    answer.sort((a, b) => a-b)
    return answer;
}