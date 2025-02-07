const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let answer = "";
let input = [];
rl.on("line", (line) => {
  input = line.split(" ");

  const size = input.length;

  for (let i = 1; i < size; i++) {
    const pre = input[i - 1];
    const cur = input[i];

    if (pre < cur) {
      if (answer === "ascending") continue;
      if (answer === "descending") {
        answer = "mixed";
        break;
      }
      if (answer === "") {
        answer = "ascending";
      }
    } else if (pre > cur) {
      if (answer === "descending") continue;
      if (answer === "ascending") {
        answer = "mixed";
        break;
      }
      if (answer === "") {
        answer = "descending";
      }
    }
  }
}).on("close", () => {
  console.log(answer);
  process.exit(0);
});
