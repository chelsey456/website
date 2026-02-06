//board
let board;
let boardWidth = 360;
let boardHeight = 640;
let context;

let birdWidth = 34;
let birdHeight = 24;
let birdX = boardWidth / 8;
let birdY = boardHeight / 2;
let birdimg;

let bird = {
	x: birdX,
	y: birdY,
	width: birdWidth,
	height: birdHeight
}

//pipes
let pipeArray = [];
let pipeWidth = 64; // ratio of 1/8
let pipeHeight = 512;
let pipeX = boardWidth;
let pipeY = 0;

let toppipeimg;
let bottompipeimg;

//physics
let velocityX = -2;
let velocityY = 0;
let gravity = 0.3;

let gameOver = false;
let score = 0;

window.onload = function () {
	board = document.getElementById("board");
	board.height = boardHeight;
	board.width = boardWidth;
	context = board.getContext("2d");

	context.fillstyle = "green";
	context.fillRect(bird.x, bird.y, bird.width, bird.height);

	birdimg = new Image();
	birdimg.src = "https://www.pngall.com/wp-content/uploads/15/Flappy-Bird-PNG-Photos.png"
	birdimg.onload = function () {
		context.drawImage(birdimg, bird.x, bird.y, bird.width, bird.height);

	}

	toppipeimg = new Image();
	toppipeimg.src = "https://scuba.cs.uchicago.edu/summer2023/flappybird/top.png"

	bottompipeimg = new Image();
	bottompipeimg.src = "https://www.nicepng.com/png/full/38-388476_flappy-bird-pipes-png-bottle.png"

	requestAnimationFrame(update);
	setInterval(placepipes, 1500);
	document.addEventListener("keydown", moveBird);

}

function update() {
	requestAnimationFrame(update);
	if (gameOver) {
		return;
	}
	context.clearRect(0, 0, board.width, board.height);

	//bird
	velocityY += gravity;
	bird.y += velocityY;
	bird.y = Math.max(bird.y + velocityY, 0);
	context.drawImage(birdimg, bird.x, bird.y, bird.width, bird.height);

	if (bird.y > board.height) {
		gameOver = true;
	}

	//pipes
	for (let i = 0; i < pipeArray.length; i++) {
		let pipe = pipeArray[i];
		pipe.x += velocityX;
		context.drawImage(pipe.img, pipe.x, pipe.y, pipe.width, pipe.height);

		if (!pipe.passed && bird.x > pipe.x + pipe.width) {
			score += 0.5;
			pipe.passed = true;
		}

		if (detectCollision(bird, pipe)) {
			gameOver = true;
		}
	}

	//clear pipes
	while (pipeArray.length > 0 && pipeArray[0].x + pipeWidth < 0) {
		pipeArray.shift();

	}

	//score
	context.fillstyle = "white";
	context.font = "45px sans-serif";
	context.fillText(score, 5, 45);

	if (gameOver) {
		context.fillText("GAME OVER", 5, 90);
		context.font = "25px sans-serif"
		context.fillText("Press Space to Restart", 10, 120);
	}
}

function placepipes() {
	if (gameOver) {
		return;
	}

	let randomPipeY = pipeY - pipeHeight / 4 - Math.random() * (pipeHeight / 2);
	let openingSpace = board.height / 4;
	let toppipe = {
		img: toppipeimg,
		x: pipeX,
		y: randomPipeY,
		width: pipeWidth,
		height: pipeHeight,
		passed: false
	}

	pipeArray.push(toppipe);

	let bottompipe = {
		img: bottompipeimg,
		x: pipeX,
		y: randomPipeY + pipeHeight + openingSpace,
		width: pipeWidth,
		height: pipeHeight,
		passed: false
	}
	pipeArray.push(bottompipe);
}

function moveBird(e) {
	if (e.code == "Space" || e.code == "ArrowUp" || e.code == "KeyW" || e.code == "KeyT" || e.code == "KeyI") {
		velocityY = -5;

		//reset game
		if (gameOver) {
			bird.y = birdY;
			pipeArray = [];
			score = 0;
			gameOver = false;
		}
	}
}

function detectCollision(a, b) {
	return a.x < b.x + b.width &&
		a.x + a.width > b.x &&
		a.y < b.y + b.height &&
		a.y + a.height > b.y;
}