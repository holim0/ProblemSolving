/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var reverseOddLevels = function (root) {
  let curLevel = 0;
  const q = [];

  q.push(root);

  while (q.length) {
    const curSize = q.length;
    if (curLevel % 2 === 1) {
      let i = 0,
        j = curSize - 1;

      while (i < j) {
        let leftValue = q[i].val;
        let rightValue = q[j].val;
        q[i].val = rightValue;
        q[j].val = leftValue;
        i += 1;
        j -= 1;
      }
    }
    for (let i = 0; i < curSize; i++) {
      let cur = q.shift();

      if (cur.left && cur.right) {
        q.push(cur.left);
        q.push(cur.right);
      }
    }
    curLevel += 1;
  }

  return root;
};
