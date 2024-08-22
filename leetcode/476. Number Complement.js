/**
 * @param {number} num
 * @return {number}
 */
var findComplement = function (num) {
  let reverse = "";
  let binary = num.toString(2);
  binary = binary.split("");
  binary.forEach((b) => {
    if (b === "1") {
      reverse += "0";
    } else {
      reverse += "1";
    }
  });
  return parseInt(reverse, 2);
};
