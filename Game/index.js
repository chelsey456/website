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

window.onload = function () {
	board = document.getElementById("board");
	board.height = boardHeight;
	board.width = boardWidth;
	context = board.getContext("2d");

	context.fillstyle = "green";
	context.fillrect(bird.x, bird.y, bird.width, bird.height);
	
	birdimg = new Image();
	birdimg.src = "https://www.pngall.com/wp-content/uploads/15/Flappy-Bird-PNG-Photos.png"
}
