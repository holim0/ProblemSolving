function solution(a) {
  var answer = -1;
  let cnt = {};

  for (let i = 0; i < a.length; i++) {
    let value = a[i];
    if (cnt[value]) {
      cnt[value] += 1;
    } else {
      cnt[value] = 1;
    }
  }
  let cntSize = Object.keys(cnt).length;
  let keys = Object.keys(cnt);
  for (let i = 0; i < cntSize; i++) {
    let k = keys[i];
    if (answer >= cnt[k]) continue;
    let curSize = 0;
    let j = 0;
    while (j < a.length - 1) {
      if (a[j] !== a[j + 1] && (a[j] == k || a[j + 1] == k)) {
        curSize += 1;
        j += 2;
      } else {
        j += 1;
      }
    }
    answer = Math.max(answer, curSize);
  }
  return answer * 2;
}
