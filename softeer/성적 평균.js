const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const inputs = [];

rl.on("line", (line) => {
  inputs.push(line.split(" ").map((value) => Number(value)));
}).on("close", () => {
  const [n, k] = inputs[0];
  const s = inputs[1];

  const acc = [0, s[0]];

  for (let i = 1; i < n; i++) {
    acc.push(acc[acc.length - 1] + s[i]);
  }

  for (let i = 2; i < 2 + k; i++) {
    const [a, b] = inputs[i];

    const curSum = acc[b] - acc[a - 1];
    const cnt = b - a + 1;

    console.log((curSum / cnt).toFixed(2));
  }

  process.exit(0);
});
