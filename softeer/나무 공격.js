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
  const mapp = [];
  const targetCnt = new Array(n + 1).fill(0);
  let totalCnt = 0;
  for (let i = 1; i <= n; i++) {
    for (let j = 0; j < m; j++) {
      if (inputs[i][j] === 1) {
        targetCnt[i] += 1;
        totalCnt += 1;
      }
    }
  }

  const [f1, t1] = inputs[n + 1];
  const [f2, t2] = inputs[n + 2];

  for (let i = f1; i <= t1; i++) {
    if (targetCnt[i] > 0) {
      targetCnt[i] -= 1;
      totalCnt -= 1;
    }
  }
  for (let i = f2; i <= t2; i++) {
    if (targetCnt[i] > 0) {
      targetCnt[i] -= 1;
      totalCnt -= 1;
    }
  }

  console.log(totalCnt);
});
