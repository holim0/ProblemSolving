/**
 * @param {number[][]} rooms
 * @return {boolean}
 */
var canVisitAllRooms = function (rooms) {
  const size = rooms.length;
  const visit = new Array(size).fill(false);

  const goVisit = (cur) => {
    visit[cur] = true;

    const nextRoom = rooms[cur];

    for (let i = 0; i < nextRoom.length; i++) {
      const curRoom = nextRoom[i];

      if (!visit[curRoom]) {
        goVisit(curRoom);
      }
    }
  };

  const startRoom = rooms[0];
  visit[0] = true;
  for (let i = 0; i < startRoom.length; i++) {
    const curRoom = startRoom[i];

    if (!visit[curRoom]) {
      goVisit(curRoom);
    }
  }

  for (let i = 0; i < size; i++) {
    if (!visit[i]) return false;
  }

  return true;
};
