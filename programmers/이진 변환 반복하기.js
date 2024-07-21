let zeroCnt = 0;
let transCnt = 0;

function transStr(cursStr) {
  let originLen = cursStr.length;
  let nxt = cursStr.replaceAll("0", "");

  zeroCnt += originLen - nxt.length;

  return nxt.length.toString(2);
}

function solution(s) {
  var answer = [];

  while (s !== "1") {
    s = transStr(s);
    transCnt += 1;
  }

  return [transCnt, zeroCnt];
}
