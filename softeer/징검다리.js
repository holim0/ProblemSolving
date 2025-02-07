const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on("line", (line) => {
  input.push(line);
}).on("close", () => {
  let answer = 1;
  const size = Number(input[0]);
  const rocks = input[1].split(" ").map((value) => Number(value));
  const dp = new Array(size).fill(1);

  for (let i = 1; i < size; i++) {
    const curRock = rocks[i];

    for (let j = 0; j < i; j++) {
      if (rocks[j] < curRock) {
        dp[i] = Math.max(dp[i], dp[j] + 1);
      }
    }
    answer = Math.max(answer, dp[i]);
  }

  console.log(answer);
  process.exit(0);
});
