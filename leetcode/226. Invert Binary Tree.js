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
var invertTree = function (root) {
  let cur = root;

  const swap = (curRoot) => {
    if (!curRoot) {
      return;
    }
    let l = curRoot.left;
    let r = curRoot.right;

    curRoot.left = r;
    curRoot.right = l;

    if (curRoot.left) {
      swap(curRoot.left);
    }
    if (curRoot.right) {
      swap(curRoot.right);
    }
  };

  swap(cur);
  return cur;
};
