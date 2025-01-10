/**
 * @param {string[]} words1
 * @param {string[]} words2
 * @return {string[]}
 */
var wordSubsets = function(words1, words2) {
    const answer = []

    const words1CntMap = {}
    const words2MaxCnt = {}
    for(let w1 of words1){
        let cnt = {}
        
        for(let ww of w1){
            if(cnt[ww]){
                cnt[ww]+=1
            }else{
                cnt[ww] = 1
            }
        }
        words1CntMap[w1] = cnt
    }

    for(let w2 of words2){
        let cnt = {}
        for(let ww of w2){
            if(cnt[ww]){
                cnt[ww]+=1
            }else{
                cnt[ww] = 1
            }
        }

        Object.entries(cnt).forEach(([key, value]) => {
            if(words2MaxCnt[key]){
                words2MaxCnt[key] = Math.max(words2MaxCnt[key], value)
            }else{
                words2MaxCnt[key] = value
            }
        }); 
    }

    for(let w1 of words1){
        const cntMap = words1CntMap[w1]
        let isAllSet = true
        const entries = Object.entries(words2MaxCnt)
        
        for(let i=0; i<entries.length; i++){
            const [key, value] = entries[i]
            if(!cntMap[key] || cntMap[key]<value ){
                isAllSet = false
                break
            }
        }


        if(isAllSet){
            answer.push(w1)
        }
    }

    return answer
};