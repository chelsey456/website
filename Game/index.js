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

window.onload = function () {
	board = document.getElementById("board");
	board.height = boardHeight;
	board.width = boardWidth;
	context = board.getContext("2d");

	context.fillstyle = "green";
	context.fillRect(bird.x, bird.y, bird.width, bird.height);
	
	birdimg = new Image();
	birdimg.src = "https://www.pngall.com/wp-content/uploads/15/Flappy-Bird-PNG-Photos.png"
	birdimg.onload = function() {
	context.drawImage(birdimg, bird.x, bird.y, bird.width, bird.height);
	
	}

	toppipeimg = new Image();
	toppipeimg.src = "https://scuba.cs.uchicago.edu/summer2023/flappybird/top.png"

 	bottompipeimg = new Image();
	bottompipeimg.src = "https://www.nicepng.com/png/full/38-388476_flappy-bird-pipes-png-bottle.png"

	requestAnimationFrame(update);
	setInterval(placepipes, 1500);

} 

function update() {
	requestAnimationFrame(update);
	context.clearRect(0, 0, board.width, board.height);

	//bird
	context.drawImage(birdimg, bird.x, bird.y, bird.width, bird.height);

	for (let i = 0; i < pipeArray.length; i++) {
		let pipe = pipeArray[i];
		pipe.x += velocityX;
		context.drawImage(pipe.img, pipe.x, pipe.y, pipe.width, pipe.height);
	}
}

function placepipes() {
	
	let randomPipeY = pipeY - pipeHeight/4 - Math.random()*(pipeHeight/2);

	let toppipe = {
		img : toppipeimg,
		x : pipeX,
		y : randomPipeY,
		width : pipeWidth,
		height : pipeHeight,
		passed : false
}

	pipeArray.push(toppipe);

}
