function solution(book_time) {
    var answer = 0;
    let time =[]
    
    for(let i=0; i<book_time.length; i++){
        let s = book_time[i][0]
        let e = book_time[i][1]
        
        s = Number(s.split(":")[0]) * 60 + Number(s.split(':')[1])
        e = Number(e.split(":")[0]) * 60 + Number(e.split(':')[1]) +10
        time.push([s, e])
    }
    let endTime = []
    time.sort((a, b) => a[0]-b[0])
    
    for(let i=0; i<time.length; i++){
        if(endTime.length==0){
            answer+=1
            endTime.push(time[i][1])
        }else{
            endTime.sort((a, b) => b-a)
            
            if(time[i][0]<endTime.slice(-1)){
                answer+=1
            }else{
                endTime.pop()
            }
            endTime.push(time[i][1])
        }
    }
    
    
    return answer;
}