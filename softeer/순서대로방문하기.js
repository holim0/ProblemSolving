const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const dir = [
  [0, 1],
  [1, 0],
  [-1, 0],
  [0, -1],
];
let answer = 0;
const inputs = [];

rl.on("line", (line) => {
  inputs.push(line.split(" ").map((v) => Number(v)));
}).on("close", () => {
  const [n, m] = inputs[0];
  const mapp = [];
  for (let i = 1; i < 1 + n; i++) {
    mapp.push(inputs[i]);
  }

  const visit = new Array(n + 1)
    .fill(false)
    .map(() => new Array(n + 1).fill(false));
  const mustVisitCheck = new Array(n + 1)
    .fill(false)
    .map(() => new Array(n + 1).fill(false));
  const mustVisit = [];
  for (let i = n + 1; i < n + m + 1; i++) {
    const [x, y] = inputs[i];
    mustVisitCheck[x - 1][y - 1] = true;
    mustVisit.push([x - 1, y - 1]);
  }
  let [sx, sy] = mustVisit[0];
  let [ex, ey] = mustVisit[mustVisit.length - 1];

  const isRange = (x, y) => {
    if (x >= 0 && x < n && y >= 0 && y < n) return true;
    return false;
  };

  const dfs = (cx, cy, nextIdx) => {
    if (cx === ex && cy === ey) {
      answer += 1;
      return;
    }

    for (let i = 0; i < 4; i++) {
      const [a, b] = dir[i];
      const nx = cx + a,
        ny = cy + b;

      if (isRange(nx, ny) && !visit[nx][ny]) {
        if (mapp[nx][ny] === 1) continue;

        if (nx === mustVisit[nextIdx][0] && ny === mustVisit[nextIdx][1]) {
          visit[nx][ny] = true;
          dfs(nx, ny, nextIdx + 1);
          visit[nx][ny] = false;
        } else {
          if (!mustVisitCheck[nx][ny]) {
            visit[nx][ny] = true;
            dfs(nx, ny, nextIdx);
            visit[nx][ny] = false;
          }
        }
      }
    }
  };
  visit[sx][sy] = true;
  dfs(sx, sy, 1);
  console.log(answer);
  process.exit(0);
});
