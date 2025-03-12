/**
 * @param {string} s
 * @return {string}
 */
var decodeString = function (s) {
  const number = [];
  const str = [];

  let tmpStr = "";
  let tmpNumber = "";
  for (let ss of s) {
    if (!isNaN(parseInt(ss, 10))) {
      tmpNumber += ss;
    } else if (ss === "[") {
      number.push(parseInt(tmpNumber, 10));
      str.push(tmpStr);
      tmpNumber = "";
      tmpStr = "";
    } else if (ss === "]") {
      const cnt = number.pop();
      tmpStr = str.pop() + tmpStr.repeat(cnt);
    } else {
      tmpStr += ss;
    }
  }

  return tmpStr;
};
