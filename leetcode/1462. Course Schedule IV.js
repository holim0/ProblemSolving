var checkIfPrerequisite = function (numCourses, prerequisites, queries) {
  // 플로이드-와샬을 위한 그래프 초기화
  const reachable = Array.from({ length: numCourses }, () =>
    Array(numCourses).fill(false)
  );

  // prerequisites를 기반으로 초기화
  for (const [u, v] of prerequisites) {
    reachable[u][v] = true; // u에서 v로 도달 가능
  }

  // 플로이드-와샬 알고리즘 수행
  for (let k = 0; k < numCourses; k++) {
    for (let i = 0; i < numCourses; i++) {
      for (let j = 0; j < numCourses; j++) {
        if (reachable[i][k] && reachable[k][j]) {
          reachable[i][j] = true; // i에서 j로 k를 통해 도달 가능
        }
      }
    }
  }

  // 쿼리 처리
  const result = [];
  for (const [u, v] of queries) {
    result.push(reachable[u][v]);
  }
  return result;
};
