
let piroMap = [
    {"diamond": 1, "iron": 1, "stone": 1},
    {"diamond": 5, "iron": 1, "stone": 1},
    {"diamond": 25, "iron": 5, "stone": 1},
]

function isUse(picks){
    for(let i=0; i<picks.length; i++){
        if(picks[i]!==0) {return false}
    }
    return true
}
function checkDone(picks, idx, limit){
    
    if (idx>=limit || isUse(picks)) { return true}
    
    return false
    
}
    
function solve(picks, orderbyCntMinerals){
    let curPiro = 0
    let mineralGroupLength = orderbyCntMinerals.length
    let idx = 0
    while(!checkDone(picks, idx, mineralGroupLength)){
        
        let curMineralGroup = orderbyCntMinerals[idx]
        let diaCnt = curMineralGroup["diamond"]
        let ironCnt = curMineralGroup["iron"]
        let stoneCnt = curMineralGroup["stone"]
        if(picks[0] >0){
            
            curPiro += (piroMap[0]["diamond"] * diaCnt)
            curPiro += (piroMap[0]["iron"] * ironCnt)
            curPiro += (piroMap[0]["stone"] * stoneCnt)
            picks[0] -=1
            idx+=1
            continue
        }
        
        if(picks[1] >0){
            
            curPiro += (piroMap[1]["diamond"] * diaCnt)
            curPiro += (piroMap[1]["iron"] * ironCnt)
            curPiro += (piroMap[1]["stone"] * stoneCnt)
            picks[1]-=1
            idx+=1
        
            continue
        }
        
        if(picks[2] >0){
            curPiro += (piroMap[2]["diamond"] * diaCnt)
            curPiro += (piroMap[2]["iron"] * ironCnt)
            curPiro += (piroMap[2]["stone"] * stoneCnt)
            picks[2]-=1
            idx+=1
            continue
        }   
    }
    
    return curPiro
}

function getNewMineral(minerals){
    
    let newMinerals = []
    
    let idx = 0
    
    while (idx<minerals.length){
        
        let curCnt = {
            "diamond": 0,
            "iron": 0,
            "stone": 0
        }
        
        let limit = idx+5
        if (limit >= minerals.length){ limit = minerals.length}
        for(let i=idx; i<limit; i++){
            let curName = minerals[i]
            curCnt[curName]+=1
        }
    
        newMinerals.push(curCnt)
        idx+=5
    }
    newMinerals.sort((a, b) => b["diamond"] - a["diamond"] || b["iron"] - a["iron"] || b["stone"] - a["stone"])
    return newMinerals
}

function solution(picks, minerals) {
    let answer = 0;
    let newMinerals = [...minerals]
    let pickSum = 0
    picks.forEach((p)=>{
        pickSum+= (5*p)
    })
    if(pickSum<minerals.length){
        newMinerals = minerals.slice(0, pickSum)
    }
    console.log(newMinerals)
    let orderbyCntMinerals = getNewMineral(newMinerals)
    answer = solve(picks, orderbyCntMinerals)
    return answer;
}