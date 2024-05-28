const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const a = +input[0];
const arr = input[1].split(" ").map(Number);


let acc = [arr[0]]

for(let i=1; i<arr.length; i++){
    if(acc[i-1] >0){
        acc.push(arr[i] + acc[i-1])
    }else{
        acc.push(arr[i])
    }
}

console.log(Math.max(...acc))

