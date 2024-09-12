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
 * @return {number}
 */
var maxDepth = function (root) {
  if (root === null) return 0;
  let depth = 0;

  const getDepth = (cur, curDepth) => {
    if (cur.left === null && cur.right === null) {
      depth = Math.max(depth, curDepth);
      return;
    }

    if (cur.left !== null) {
      getDepth(cur.left, curDepth + 1);
    }
    if (cur.right !== null) {
      getDepth(cur.right, curDepth + 1);
    }
  };
  getDepth(root, 1);
  return depth;
};
