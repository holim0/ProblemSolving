/**
 * @param {string} s
 * @param {number[][]} shifts
 * @return {string}
 */
var shiftingLetters = function(s, shifts) {
    const idxList = []

    const moduler = 26
    for(let ss of s){
        idxList.push(ss.codePointAt()-97)
    }

    const prefixSum = new Array(s.length+1).fill(0)

    for(let sh of shifts){
        let [start, end, dir] = sh
        let value = dir === 1 ? 1: -1
        prefixSum[start] += value
        prefixSum[end+1] -= value
    }

    for(let i=1; i<s.length; i++){
        prefixSum[i]+=prefixSum[i-1]
    }
    
    let answer = prefixSum.reduce((acc, cur, idx)=>{
        let newValue = acc
        if(idx<s.length){
            let cnt = idxList[idx]
            let shift = (cur % 26) + 26
            shift %=26
            cnt = (cnt+shift)%26
            newValue+= String.fromCharCode(cnt+97)
        }

        return newValue
    }, "")

     return answer
    
};