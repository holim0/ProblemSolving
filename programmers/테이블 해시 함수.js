function solution(data, col, row_begin, row_end) {
    let answer = 0;
    
    data.sort((a, b)=> a[col-1] - b[col-1] || b[0]-a[0])
    
    row_begin-=1
    sumValue =[]
    for(let i=row_begin; i<row_end; i++){
        let cur = data[i]
        let cnt = 0
        let idx = i+1
        cur.forEach((c)=>{
            cnt+= (c%idx)
        })
        
        sumValue.push(cnt)
    }
    answer = sumValue[0]
    
    for(let i=1; i<sumValue.length; i++){
        answer = (answer ^ sumValue[i])
    }
    return answer;
}