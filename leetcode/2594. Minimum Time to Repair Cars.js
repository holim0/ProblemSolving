/**
 * @param {number[]} ranks
 * @param {number} cars
 * @return {number}
 */
var repairCars = function (ranks, cars) {
  const getTime = (r, n) => {
    return r * n * n;
  };

  const size = ranks.length;
  const maxRank = Math.min(...ranks);

  let l = 1,
    r = getTime(maxRank, cars);

  while (l <= r) {
    const mid = Math.floor((l + r) / 2);

    let cnt = 0;

    for (let rank of ranks) {
      cnt += Math.floor(Math.sqrt(mid / rank));
    }

    if (cars <= cnt) {
      r = mid - 1;
    } else {
      l = mid + 1;
    }
  }

  return l;
};
