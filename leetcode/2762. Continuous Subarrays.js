/**
 * @param {number[]} nums
 * @return {number}
 */
var continuousSubarrays = function (nums) {
  const n = nums.length;
  let left = 0;
  let count = 0;

  // 두 개의 Deque를 사용하여 윈도우의 최대값과 최소값을 관리
  const maxDeque = [];
  const minDeque = [];

  for (let right = 0; right < n; right++) {
    // 최대값을 관리하는 Deque 업데이트
    while (
      maxDeque.length > 0 &&
      nums[maxDeque[maxDeque.length - 1]] < nums[right]
    ) {
      maxDeque.pop();
    }
    maxDeque.push(right);

    // 최소값을 관리하는 Deque 업데이트
    while (
      minDeque.length > 0 &&
      nums[minDeque[minDeque.length - 1]] > nums[right]
    ) {
      minDeque.pop();
    }
    minDeque.push(right);

    // 조건을 만족하지 않으면 윈도우 축소
    while (nums[maxDeque[0]] - nums[minDeque[0]] > 2) {
      left++;

      // Deque에서 윈도우 밖으로 나간 인덱스를 제거
      if (maxDeque[0] < left) maxDeque.shift();
      if (minDeque[0] < left) minDeque.shift();
    }

    // 유효한 부분 배열의 개수를 더함
    count += right - left + 1;
  }

  return count;
};
