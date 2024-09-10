/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var solve = function (board) {
  let m = board[0].length;
  let n = board.length;
  const check = [];
  for (let i = 0; i < n; i++) {
    check.push(new Array(m).fill(false));
  }
  const dir = [
    [0, 1],
    [1, 0],
    [-1, 0],
    [0, -1],
  ];
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (board[i][j] === "X" || check[i][j]) continue;

      let isInside = true;
      let pos = [[i, j]];
      let q = [];
      check[i][j] = true;
      q.push([i, j]);
      while (q.length) {
        let [cx, cy] = q.shift();

        for (let k = 0; k < 4; k++) {
          let [a, b] = dir[k];
          let [nx, ny] = [cx + a, cy + b];

          if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
            if (!check[nx][ny] && board[nx][ny] === "O") {
              q.push([nx, ny]);
              pos.push([nx, ny]);
              check[nx][ny] = true;
            }
          } else {
            isInside = false;
          }
        }
      }
      if (isInside) {
        pos.forEach((p) => {
          let [a, b] = p;
          board[a][b] = "X";
        });
      }
    }
  }
};
/////////////////////////

/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var solve = function (board) {
  let m = board[0].length;
  let n = board.length;
  const check = [];
  for (let i = 0; i < n; i++) {
    check.push(new Array(m).fill(false));
  }
  const dir = [
    [0, 1],
    [1, 0],
    [-1, 0],
    [0, -1],
  ];
  const q = [];
  for (let i = 0; i < m; i++) {
    if (board[0][i] === "O") {
      check[0][i] = true;
      q.push([0, i]);
    }
    if (board[n - 1][i] === "O") {
      check[n - 1][i] = true;
      q.push([n - 1, i]);
    }
  }
  for (let i = 1; i < n - 1; i++) {
    if (board[i][0] === "O") {
      check[i][0] = true;
      q.push([i, 0]);
    }
    if (board[i][m - 1] === "O") {
      check[i][m - 1] = true;
      q.push([i, m - 1]);
    }
  }
  while (q.length) {
    let [cx, cy] = q.shift();
    for (let i = 0; i < 4; i++) {
      let [nx, ny] = [cx + dir[i][0], cy + dir[i][1]];
      if (
        nx >= 0 &&
        nx < n &&
        ny >= 0 &&
        ny < m &&
        !check[nx][ny] &&
        board[nx][ny] === "O"
      ) {
        check[nx][ny] = true;
        q.push([nx, ny]);
      }
    }
  }

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (board[i][j] === "O" && !check[i][j]) {
        board[i][j] = "X";
      }
    }
  }
};
