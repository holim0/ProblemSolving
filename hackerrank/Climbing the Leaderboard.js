"use strict";

const fs = require("fs");

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString = "";
let currentLine = 0;

process.stdin.on("data", function (inputStdin) {
  inputString += inputStdin;
});

process.stdin.on("end", function () {
  inputString = inputString.split("\n");

  main();
});

function readLine() {
  return inputString[currentLine++];
}

/*
 * Complete the 'climbingLeaderboard' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY ranked
 *  2. INTEGER_ARRAY player
 */

function climbingLeaderboard(ranked, player) {
  let answer = [];
  let setRank = new Set();
  for (const curR of ranked) {
    setRank.add(curR);
  }
  let curRank = Array.from(setRank);
  curRank.sort((a, b) => a - b);
  for (const curPlayerScore of player) {
    let [s, e] = [0, curRank.length - 1];
    while (s <= e) {
      let mid = Math.floor((s + e) / 2);

      if (curPlayerScore >= curRank[mid]) {
        s = mid + 1;
      } else {
        e = mid - 1;
      }
    }
    e += 1;
    answer.push(curRank.length - e + 1);
  }
  return answer;
}

function main() {
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

  const rankedCount = parseInt(readLine().trim(), 10);

  const ranked = readLine()
    .replace(/\s+$/g, "")
    .split(" ")
    .map((rankedTemp) => parseInt(rankedTemp, 10));

  const playerCount = parseInt(readLine().trim(), 10);

  const player = readLine()
    .replace(/\s+$/g, "")
    .split(" ")
    .map((playerTemp) => parseInt(playerTemp, 10));

  const result = climbingLeaderboard(ranked, player);

  ws.write(result.join("\n") + "\n");

  ws.end();
}
