function solution(n) {
  let answer = 0;

  const getSol = (openCnt, closeCnt, curLen) => {
    if (curLen === 2 * n) {
      answer += 1;
      return;
    }

    let useOpenCnt = n - openCnt;
    let useCloseCnt = n - closeCnt;

    if (openCnt > 0) {
      getSol(openCnt - 1, closeCnt, curLen + 1);
    }

    if (closeCnt > 0 && useOpenCnt > useCloseCnt) {
      getSol(openCnt, closeCnt - 1, curLen + 1);
    }
  };

  getSol(n, n, 0);

  return answer;
}

//https://bb-dochi.tistory.com/51
