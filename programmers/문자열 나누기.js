function solution(s) {
    let answer = 0;
    let sCnt = 0
    let restCnt = 0
    
    let listS = s.split("")
    let firstS = ""
    
    let stringList = []
    
    let temp =[]
    
    
    for(let i=0; i<listS.length; i++){
        if(temp.length===0){
            firstS = listS[i]
            sCnt+=1
            temp.push(listS[i])
        }else{
            if(firstS == listS[i]){
                sCnt+=1
                temp.push(listS[i])
            }else{
                restCnt+=1
                temp.push(listS[i])
            }
            
            if(sCnt===restCnt){
                stringList.push(temp.join(""))
                temp = []
                sCnt=0
                restCnt = 0
            }
        }
    }
    
    if(temp.length>0){
        stringList.push(temp.join(""))
    }
    answer = stringList.length
    return answer;
}