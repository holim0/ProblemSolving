function solution(sequence) {
  var answer = 0;
  const seq1 = [];
  const seq2 = [];

  for (let i = 0; i < sequence.length; i++) {
    let cur = sequence[i];
    if (i % 2 === 0) {
      seq1.push(cur * -1);
    } else {
      seq1.push(cur);
    }
  }

  for (let i = 0; i < sequence.length; i++) {
    let cur = sequence[i];
    if (i % 2 === 0) {
      seq2.push(cur);
    } else {
      seq2.push(cur * -1);
    }
  }

  const getMaxSum = (curSeq) => {
    let max_sum = -100000;
    let sum = 0;

    for (let i = 0; i < curSeq.length; i++) {
      sum = Math.max(sum + curSeq[i], curSeq[i]);

      max_sum = Math.max(max_sum, sum);
    }
    return max_sum;
  };

  answer = Math.max(getMaxSum(seq1), getMaxSum(seq2));
  return answer;
}
