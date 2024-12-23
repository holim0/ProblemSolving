var minimumOperations = function (root) {
  let answer = 0;
  const q = [];

  // BFS를 위한 큐 초기화
  if (root) q.push(root);

  while (q.length) {
    const curLen = q.length;
    const valueList = [];

    // 현재 레벨의 노드 값과 인덱스를 수집
    for (let i = 0; i < curLen; i++) {
      const curNode = q.shift();
      valueList.push([curNode.val, i]);
      if (curNode.left) q.push(curNode.left);
      if (curNode.right) q.push(curNode.right);
    }

    // 노드 값을 정렬하여 최소 스왑 횟수 계산
    const sortedList = [...valueList].sort((a, b) => a[0] - b[0]);

    const map = new Map();

    for (let i = 0; i < sortedList.length; i++) {
      map.set(sortedList[i], i);
    }
    for (let i = 0; i < valueList.length; ) {
      const ind = map.get(valueList[i]);
      if (ind === i) {
        i++;
      } else {
        [valueList[i], valueList[ind]] = [valueList[ind], valueList[i]];
        answer++;
      }
    }
  }

  return answer;
};
