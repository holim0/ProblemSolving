/**
 * @param {string} s
 * @param {string} locked
 * @return {boolean}
 */
var canBeValid = function(s, locked) {
    if(s.length % 2 !==0) return false
    const isLocked = new Array(locked.length).fill(false)
    for(let i=0; i<locked.length; i++){
        if(locked[i]==="1"){
            isLocked[i]= true
        }
    }
    let closeCnt = 0
    let possibleOpenCnt = 0
    
    for(let i=0; i<s.length; i++){
        if(s[i]=== "(" || isLocked[i] === false){
            possibleOpenCnt+=1
        }else{
            possibleOpenCnt-=1
        }

        if(possibleOpenCnt<0) return false
    }

    let possibleCloseCnt = 0;
    for (let i = s.length-1; i >= 0; i--) {
        if (s[i] === ')' || locked[i] === '0') {
            possibleCloseCnt+=1
        } else {
            possibleCloseCnt-=1;
        }
        if (closeCount < 0) {
            return false;
        }
    }

    return true
};