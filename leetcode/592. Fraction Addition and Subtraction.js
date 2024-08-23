/**
 * @param {string} expression
 * @return {string}
 */

const gcd = (a, b) => {
  while (b > 0) {
    let r = a % b;
    a = b;
    b = r;
  }
  return a;
};
var fractionAddition = function (expression) {
  const downValue = [];
  const splitValue = expression.split(/[+-]/);
  const oper = [];
  let splitValueSize = 0;
  splitValue.forEach((s) => {
    if (s) {
      splitValueSize += 1;
    }
  });
  if (splitValueSize === 1) {
    return expression;
  }

  for (let i = 0; i < expression.length; i++) {
    let e = expression[i];
    if ((e === "+") | (e === "-")) {
      oper.push(e);
    }
  }

  splitValue.forEach((v) => {
    if (v) {
      let down = v.split("/")[1];
      downValue.push(Number(down));
    }
  });

  let lcd = (downValue[0] * downValue[1]) / gcd(downValue[0], downValue[1]);
  for (let i = 2; i < downValue.length; i++) {
    lcd = (lcd * downValue[i]) / gcd(lcd, downValue[i]);
  }
  const upperValue = [];
  splitValue.forEach((sv) => {
    if (sv) {
      const [upper, curDown] = sv.split("/");
      const mulValue = lcd / Number(curDown);
      upperValue.push(Number(upper) * mulValue);
    }
  });
  if (upperValue.length === oper.length) {
    if (oper[0] === "-") {
      upperValue[0] = upperValue[0] * -1;
      oper.shift();
    }
  }
  let upperSum = upperValue[0];
  let operIdx = 0;
  for (let i = 1; i < upperValue.length; i++) {
    const curOper = oper[operIdx];
    if (curOper == "-") {
      upperSum -= upperValue[i];
    } else {
      upperSum += upperValue[i];
    }
    operIdx += 1;
  }
  if (upperSum === 0) {
    return "0/1";
  }
  let downUpperGcd = null;
  if (upperSum < 0) {
    downUpperGcd = gcd(upperSum * -1, lcd);
  } else {
    downUpperGcd = gcd(upperSum, lcd);
  }
  return `${upperSum / downUpperGcd}/${lcd / downUpperGcd}`;
};
