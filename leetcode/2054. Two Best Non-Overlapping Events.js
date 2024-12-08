/**
 * @param {number[][]} events
 * @return {number}
 */
var maxTwoEvents = function(events) {
    events.sort((a, b) => a[1] - b[1]); // start 기준 정렬

    let max_end = []

    let max_value = 0
    for (let e of events){
        let [start, end, value] = e
        max_value = Math.max(max_value, value)
        max_end.push([end, max_value])
    }
    let answer = 0

    for (let e of events){
        let [start, end, value] = e
        answer = Math.max(answer, value)

        let l = 0
        let r = max_end.length-1
        let nearEndIdx = -1
        while(l<=r){
            let mid= Math.floor((l+r)/2)

            let curEnd = max_end[mid][0]

            if(start>curEnd){
                nearEndIdx = mid
                l = mid + 1
            }else{
                r = mid - 1
            }
        }
        if(nearEndIdx !==-1){
            answer = Math.max(answer, max_end[nearEndIdx][1] + value)
        }
    } 

    return answer
};