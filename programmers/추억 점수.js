function solution(name, yearning, photo) {
    let answer = [];
    let nameSize = name.length
    let nameToYearn = {}
    
    for(let i=0; i<nameSize; i++){
        nameToYearn[name[i]] = yearning[i]
    }
    
    photo.forEach((curPhoto)=>{
        let curYearning = 0
        
        curPhoto.forEach((curName)=>{
            if(nameToYearn[curName] !== undefined){
                curYearning+= nameToYearn[curName]
            }
        })
        
        answer.push(curYearning)
    })
    
    return answer;
}