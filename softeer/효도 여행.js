const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let answer = 0;
const inputs = [];
rl.on("line", (line) => {
  inputs.push(line);
}).on("close", () => {
  const [n, m] = inputs[0].split(" ").map((value) => Number(value));
  const likeRoute = inputs[1].split("");
  const g = {};

  for (let i = 0; i < n - 1; i++) {
    const curInput = inputs[i + 2].split(" ");

    const f = Number(curInput[0]);
    const t = Number(curInput[1]);
    const s = curInput[2];

    if (!g[f]) {
      g[f] = [];
    }
    if (!g[t]) {
      g[t] = [];
    }
    g[f].push([t, s]);
    g[t].push([f, s]);
  }

  const dp = [];

  for (let i = 0; i <= m; i++) {
    dp.push(new Array(5001).fill(0));
  }

  const check = {};
  const curRouterStr = [];
  const getRoute = (cur, size) => {
    check[cur] = true;

    for (let i = 0; i < m + 1; i++) {
      if (i === 0 || size === 0) {
        dp[i][size] = 0;
      } else if (likeRoute[i - 1] === curRouterStr[size - 1]) {
        dp[i][size] = dp[i - 1][size - 1] + 1;
      } else {
        dp[i][size] = Math.max(dp[i - 1][size], dp[i][size - 1]);
      }
      answer = Math.max(dp[i][size], answer);
    }

    for (let nextNode of g[cur]) {
      const [nextNodeNumber, curRouteChar] = nextNode;
      if (!check[nextNodeNumber]) {
        curRouterStr.push(curRouteChar);
        getRoute(nextNodeNumber, size + 1);
        curRouterStr.pop();
      }
    }
  };

  getRoute(1, 0);

  console.log(answer);

  process.exit(0);
});
