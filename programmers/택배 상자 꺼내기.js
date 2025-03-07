function solution(n, w, num) {
  let answer = 1;

  const h = Math.ceil(n / w);
  const rest = n % w;

  const cur_h = Math.ceil(num / w);

  if (h === cur_h) return 1;
  answer += h - cur_h;
  if (rest === 0) {
    return answer;
  }

  const check = new Array(w).fill(false);

  if (h % 2 === 0) {
    let start = w - 1;
    for (let i = 0; i < rest; i++) {
      check[start] = true;
      start -= 1;
    }
  } else {
    let start = 0;
    for (let i = 0; i < rest; i++) {
      check[start] = true;
      start += 1;
    }
  }

  let cur_pos = (num - 1) % w; // 올바른 위치 계산

  if (cur_h % 2 === 0) {
    cur_pos = w - cur_pos - 1;
  }

  if (!check[cur_pos]) {
    answer -= 1;
  }

  return answer;
}
