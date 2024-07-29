function solution(routes) {
  let answer = 0;

  routes.sort((a, b) => a[1] - b[1]);

  let cur = -30000;

  for (let i = 0; i < routes.length; i++) {
    let [s, e] = routes[i];

    if ((cur >= s) & (cur <= e)) {
      continue;
    } else {
      answer += 1;
      cur = e;
    }
  }

  return answer;
}
