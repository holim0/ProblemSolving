function solution(wallpaper) {
    let answer = [];
    let wallpaperMap = []
    let [lux, luy, rdx, rdy] = [100, 100, 0, 0]
    wallpaper.forEach((w)=>{
        let row = w.split("")
        wallpaperMap.push(row)
    })
    
    let [w, h] = [wallpaperMap[0].length, wallpaperMap.length]
    
    for(let i=0; i<h; i++){
        for(let j=0; j<w; j++){
            if(wallpaperMap[i][j]==="#"){
                lux = Math.min(lux, i)
                luy = Math.min(luy, j)
                rdx = Math.max(rdx, i+1)
                rdy = Math.max(rdy, j+1)
            }
        }
    }
    
    answer = [lux, luy, rdx, rdy]
    
    
    return answer;
}