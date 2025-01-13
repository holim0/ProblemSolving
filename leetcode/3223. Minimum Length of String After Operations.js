/**
 * @param {string} s
 * @return {number}
 */
var minimumLength = function(s) {
    const cnt = {}
    let answer = 0
    for(let ss of s){
        if(!cnt[ss]){
            cnt[ss] = 1
        }else{
            cnt[ss]+=1
        }
    }

    Object.entries(cnt).forEach(([key, value]) => {
        if(value%2==0){
            answer+=2
        }else{
            answer+=1
        }
    })
    return answer
};