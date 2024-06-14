function solution(k, tangerine) {
    let answer = 0;
    let cnt = {}
    
    tangerine.forEach((t)=>{
        if(!cnt[t]){
            cnt[t] = 1
        }else{
            cnt[t]+=1
        }
    })
    
    let cntList = [];
    for (let size in cnt) {
        cntList.push([size, cnt[size]]);
    }
    
    cntList.sort((a, b)=> a[1]-b[1])
    
    answer = cntList.length
    let total = tangerine.length
    for(let i=0; cntList.length; i++){
        let curCnt = cntList[i][1]
        
        if(total-curCnt>=k){
            answer-=1
            total-=curCnt
        }else{
            break
        }
    }
    return answer;
}