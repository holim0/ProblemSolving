function processData(input) {
  let data = input.split("\n");
  data = data.slice(1);
  let arr = [];
  for (let i = 0; i < data.length; i++) {
    let cur = data[i].split(" ");
    arr.push(cur);
  }
  arr.sort((a, b) => Number(b[1]) - Number(a[1]) || a[0].localeCompare(b[0]));
  for (let i = 0; i < arr.length; i++) {
    let cur = arr[i].join(" ");
    console.log(cur);
  }
}

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
  _input += input;
});

process.stdin.on("end", function () {
  processData(_input);
});
