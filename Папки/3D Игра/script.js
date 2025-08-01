body {
  margin: 0;
  background: linear-gradient(to top, #444, #999);
  overflow: hidden;
  font-family: sans-serif;
}

canvas {
  display: block;
  margin: 0 auto;
  background: #222;
  border: 5px solid #fff;
}

const canvas = document.getElementById('game');
const ctx = canvas.getContext('2d');

const roadLines = [
  { y: 0 }, { y: 100 }, { y: 200 }, { y: 300 }, { y: 400 }
];

const player = {
  x: 100,
  y: 300,
  width: 50,
  height: 100,
  color: 'red'
};

const keys = {};
let speed = 5;

function drawCar(car) {
  ctx.fillStyle = car.color;
  ctx.fillRect(car.x, car.y, car.width, car.height);
}

function drawRoad() {
  ctx.fillStyle = '#333';
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  ctx.fillStyle = '#fff';
  for (let line of roadLines) {
    ctx.fillRect(canvas.width / 2 - 5, line.y, 10, 40);
  }
}

function updateRoad() {
  for (let line of roadLines) {
    line.y += speed;
    if (line.y > canvas.height) {
      line.y = -40;
    }
  }
}

function updatePlayer() {
  if (keys['ArrowLeft'] && player.x > 0) player.x -= 6;
  if (keys['ArrowRight'] && player.x + player.width < canvas.width) player.x += 6;
}

function gameLoop() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  drawRoad();
  updateRoad();
  updatePlayer();
  drawCar(player);
  requestAnimationFrame(gameLoop);
}

document.addEventListener('keydown', e => keys[e.key] = true);
document.addEventListener('keyup', e => keys[e.key] = false);

gameLoop();