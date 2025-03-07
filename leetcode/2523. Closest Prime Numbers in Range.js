/**
 * @param {number} left
 * @param {number} right
 * @return {number[]}
 */
var closestPrimes = function (left, right) {
  const MAX = Math.pow(10, 6);
  const prime = new Array(MAX + 1).fill(true);
  const primeList = [];
  prime[0] = true;
  prime[1] = false;
  for (let i = 2; i * i < MAX; i++) {
    if (!prime[i]) continue;
    for (let j = i + i; j <= MAX; j += i) {
      prime[j] = false;
    }
  }

  for (let i = 2; i <= MAX; i++) {
    if (prime[i]) {
      primeList.push(i);
    }
  }
  const targetPrime = [];

  for (let p of primeList) {
    if (p > right) break;
    if (left <= p && p <= right) {
      targetPrime.push(p);
    }
  }

  if (targetPrime.length < 2) {
    return [-1, -1];
  }

  const diff = [];

  for (let i = 0; i < targetPrime.length - 1; i++) {
    const now = targetPrime[i];
    const next = targetPrime[i + 1];

    diff.push([next - now, now, next]);
  }

  diff.sort((a, b) => a[0] - b[0] || a[1] - b[1]);
  const answer = [diff[0][1], diff[0][2]];
  return answer;
};
