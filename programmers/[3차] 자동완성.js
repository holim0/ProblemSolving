class Node {
  constructor(value = "") {
    this.value = value;
    this.end = false;
    this.child = {};
    this.makeWordsCnt = 0;
  }
}

class Trie {
  constructor() {
    this.root = new Node();
  }

  insert(curValue) {
    let curNode = this.root;

    for (let i = 0; i < curValue.length; i++) {
      let curChar = curValue[i];

      if (curNode.child[curChar] === undefined) {
        curNode.child[curChar] = new Node(curNode.vale + curChar);
      }
      curNode = curNode.child[curChar];
      curNode.makeWordsCnt += 1;
    }
    curNode.end = true;
  }

  getTypeCnt(curValue) {
    let curNode = this.root;
    let cnt = 0;
    for (let i = 0; i < curValue.length; i++) {
      curNode = curNode.child[curValue[i]];
      cnt += 1;
      if (curNode.makeWordsCnt === 1) return cnt;
    }
    return cnt;
  }
}

function solution(words) {
  var answer = 0;

  const trie = new Trie();

  words.forEach((w) => trie.insert(w));

  words.forEach((w) => {
    answer += trie.getTypeCnt(w);
  });

  return answer;
}
