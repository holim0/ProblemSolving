function isValid(cx, cy, rectangle) {
  for (let i = 0; i < rectangle.length; i++) {
    let [startx, starty, endx, endy] = rectangle[i];
    startx = 2 * startx;
    starty = 2 * starty;
    endx = 2 * endx;
    endy = 2 * endy;
    if (startx < cx && starty < cy && endx > cx && endy > cy) {
      return false;
    }
  }
  return true;
}

function isLine(cx, cy, nx, ny, rectangle) {
  for (let i = 0; i < rectangle.length; i++) {
    let [startx, starty, endx, endy] = rectangle[i];
    startx = 2 * startx;
    starty = 2 * starty;
    endx = 2 * endx;
    endy = 2 * endy;
    if (startx <= cx && starty <= cy && endx >= cx && endy >= cy) {
      if (startx <= nx && starty <= ny && endx >= nx && endy >= ny) {
        return true;
      }
    }
  }

  return false;
}
function solution(rectangle, characterX, characterY, itemX, itemY) {
  let answer = 0;
  let possiblePos = [];
  let check = [];
  let isPossible = [];

  for (let i = 0; i <= 100; i++) {
    check.push(new Array(101).fill(false));
    isPossible.push(new Array(101).fill(false));
  }

  rectangle.forEach((rect) => {
    let [sx, sy, ex, ey] = rect;
    sx = sx * 2;
    sy = sy * 2;
    ex = ex * 2;
    ey = ey * 2;

    for (let i = sx; i <= ex; i++) {
      if (isValid(i, sy, rectangle) && !isPossible[i][sy]) {
        isPossible[i][sy] = true;
        possiblePos.push([i, sy]);
      }
      if (isValid(i, ey, rectangle) && !isPossible[i][ey]) {
        isPossible[i][ey] = true;
        possiblePos.push([i, ey]);
      }
    }

    for (let i = sy; i <= ey; i++) {
      if (isValid(sx, i, rectangle) && !isPossible[sx][i]) {
        isPossible[sx][i] = true;
        possiblePos.push([sx, i]);
      }
      if (isValid(ex, i, rectangle) && !isPossible[ex][i]) {
        isPossible[ex][i] = true;
        possiblePos.push([ex, i]);
      }
    }
  });

  let q = [];
  let dir = [
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1],
  ];

  check[2 * characterX][2 * characterY] = true;

  q.push([2 * characterX, 2 * characterY, 0]);

  while (q.length) {
    let [cx, cy, dist] = q.shift();
    if (cx === 2 * itemX && cy === 2 * itemY) {
      return dist / 2;
    }
    for (let i = 0; i < 4; i++) {
      let [a, b] = dir[i];
      let [nx, ny] = [cx + a, cy + b];

      if (
        nx <= 100 &&
        ny <= 100 &&
        isPossible[nx][ny] &&
        !check[nx][ny] &&
        isLine(cx, cy, nx, ny, rectangle)
      ) {
        check[nx][ny] = true;
        q.push([nx, ny, dist + 1]);
      }
    }
  }

  return answer;
}
