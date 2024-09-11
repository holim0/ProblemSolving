/**
 * @param {number} start
 * @param {number} goal
 * @return {number}
 */
var minBitFlips = function (start, goal) {
  let answer = 0;
  let startValue = start.toString(2);
  let goalValue = goal.toString(2);

  if (startValue.length > goalValue.length) {
    while (startValue.length > goalValue.length) {
      goalValue = "0" + goalValue;
    }
  } else {
    while (startValue.length < goalValue.length) {
      startValue = "0" + startValue;
    }
  }

  for (let i = 0; i < startValue.length; i++) {
    if (startValue[i] !== goalValue[i]) {
      answer += 1;
    }
  }
  return answer;
};
