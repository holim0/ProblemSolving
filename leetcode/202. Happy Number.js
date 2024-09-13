/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n) {
    let cur = n
    const checked = [];
    if(n===1) return true
    while (cur!==1){
        let stringCur = cur.toString()
        if (checked.includes(cur)) return false;
        checked.push(cur)
        let next = 0

        for(let i=0; i<stringCur.length; i++){
            next+= Math.pow(Number(stringCur[i]), 2)
        }
            
        cur = next
        if(cur===1) return true
    }
    return false
};