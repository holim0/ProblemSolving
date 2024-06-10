function getIdx(cur, filterAlpha){
    
    for(let i=0; i<filterAlpha.length; i++){
        if(cur===filterAlpha[i]){
            return i
        }
    }
    
}
function solution(s, skip, index) {
    let answer = '';
    let skipDict = {}
    let alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
                "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    
    let filterAlpha = []
    for(let i in skip){
        skipDict[skip[i]] = true
    }
    s = s.split("")
    alpha.forEach((a)=>{
        if(!skipDict[a]){
            filterAlpha.push(a)
        }
    })
    let moduler = filterAlpha.length
    
    
    s.forEach((curAlpha)=>{
        let curIdx = getIdx(curAlpha, filterAlpha)
        
        let nextIdx = (curIdx+index)%moduler
        
        answer+=filterAlpha[nextIdx]
    })
    
    return answer;
}