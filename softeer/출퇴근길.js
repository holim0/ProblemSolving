const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const inputs = [];

rl.on("line", (line) => {
  inputs.push(line.split(" ").map((value) => Number(value)));
}).on("close", () => {
  const [n, m] = inputs[0];
  const [start, end] = inputs[inputs.length - 1];
  const g = Array.from({ length: n + 1 }, () => []);
  const rg = Array.from({ length: n + 1 }, () => []);

  for (let i = 1; i <= m; i++) {
    const [f, t] = inputs[i];
    g[f].push(t);
    rg[t].push(f);
  }

  const dfs = (start, visit, curg) => {
    const stack = [start];
    visit[start] = 1; // 시작 노드 방문 표시
    while (stack.length > 0) {
      const node = stack.pop();
      for (const nextNode of curg[node]) {
        if (!visit[nextNode]) {
          visit[nextNode] = 1; // 방문 표시
          stack.push(nextNode);
        }
      }
    }
  };
  const startVisit = Array.from(n + 1).fill(false);
  const rstartVisit = Array.from(n + 1).fill(false);
  const endVisit = Array.from(n + 1).fill(false);
  const rendVisit = Array.from(n + 1).fill(false);

  startVisit[end] = true;
  dfs(start, startVisit, g);

  endVisit[start] = true;
  dfs(end, endVisit, g);

  dfs(start, rstartVisit, rg);
  dfs(end, rendVisit, rg);

  let answer = 0;
  for (let i = 1; i <= n; i++) {
    if (i === start || i === end) continue;

    if (startVisit[i] && rstartVisit[i] && endVisit[i] && rendVisit[i]) {
      answer += 1;
    }
  }

  console.log(answer);
});
