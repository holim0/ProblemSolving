function solution(bandage, maxhealth, attacks) {
    let answer = 0;
    
    [castingTime, healPerSec, extraHeal] = bandage
    
    let attackSize = attacks.length
    let maxTime = attacks[attackSize-1]
    maxTime = maxTime[0]
    let curTime = 0
    let curHealth = maxhealth
    let success = 0
    
    while(curTime<=maxTime){
        if(curTime===0){
            curTime+=1
            continue
        }
        let isAttack = false
        for(let i=0; i<attacks.length; i++){
            [attackTime, attackValue] = attacks[i]
            if(attackTime===curTime){
                isAttack = true
                success = 0
                curHealth -= attackValue
                if(curHealth<=0) return -1
            }
        }
        
        if(isAttack === false){
            success+=1
            if(curHealth+healPerSec >= maxhealth){
                curHealth = maxhealth
            }else{
                curHealth += healPerSec
            }
            
            if(success===castingTime){
                if(curHealth+extraHeal >= maxhealth){
                    curHealth = maxhealth
                }else{
                    curHealth += extraHeal
                }
                success=0
            }
        }
        
        curTime+=1
    }
    
    
    
    answer = curHealth
    
    return answer;
}