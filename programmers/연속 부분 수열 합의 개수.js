function solution(elements) {
    let answer = 1
    let check = {}
    let double = [...elements, ...elements]
    let acc = [double[0]]
    let elesize = elements.length
    
    for(let i=1; i<double.length; i++){
        acc.push(acc.at(-1)+double[i])
    }
    let totalSum = 0
    
    for(let e of elements){
        totalSum+=e
    }
    
    for(let i=1; i<elesize; i++){
    
        for(let j=0; j<elesize; j++){
            let curSum = 0
            let [start, end] = [j, j+i-1]
            if(j==0){
                curSum = acc[end]
            }else{

                curSum = acc[end] - acc[start-1]
            }

            if(!check[curSum]){
                check[curSum] = true
                answer+=1
            }
        }
    }
    
    
    return answer;
}