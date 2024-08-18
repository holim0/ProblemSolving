/**
 * @param {string} s
 * @return {string}
 */
const isAlpha = (cur) => {
    if(cur[0] >= "a" && cur[0] <= "z") {
        return true
    }
    return false
}

const isNumber = (cur) =>{
    if(Number.isInteger(Number(cur))){
        return true
    }
    return false
}
var decodeString = function(s) {
    let stack =[]
    let answer =""

    for(let i=0; i<s.length; i++){
        if(s[i] !=="]"){
            stack.push(s[i])
            continue
        }
        let curString = ""
        let curNumber = ""
        while(isAlpha(stack[stack.length-1])){
            curString = stack.pop() + curString
        }
        stack.pop()
        while(isNumber(stack[stack.length-1])){
            curNumber = stack.pop() + curNumber
        }
        curNumber = Number(curNumber)
        curString = curString.repeat(curNumber)
        stack.push(curString)
    }
    let tmp = ""
    while(stack.length>0){
        tmp = stack.pop() + tmp
    }
    answer+=tmp
    return answer
};