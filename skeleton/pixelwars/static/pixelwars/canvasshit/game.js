var requestAnimationFrame = window.requestAnimationFrame ||
    window.mozRequestAnimationFrame ||
    window.webkitRequestAnimationFrame ||
    window.msRequestAnimationFrame ||
    function (callback) {
        setTimeout(callback, 1000 / 30);
    };

var canvas = document.getElementById("canvas-id");
canvas.width = 500;
canvas.height = 500;
var context = canvas.getContext("2d");
//cursor= none;
//style.cursor.size =  1px
//var cur=new Image();
//cur.src="zemia.jpg";
var iRub = false;
var br = 0;


/*jQuery*/


var color1;
$(function () {
    $("button").click(function () {
        color1 = $(this).val();
    });
    $("#colorPicker").click(function(){
        color1 = $("#myColor").val();
        $("#colorPicker").css("background-color", color1)
    });

});

var image = [];
for (var i = 0; i < 25; i++) {
    image[i] = [];
    for (var j = 0; j < 25; j++) {
        image[i][j] = 0;
    }
}
var mishkaX, mishkaY, clicked = false;

window.addEventListener("mouseup", function (args) {
    mishkaX = args.clientX - canvas.offsetLeft;
    mishkaY = args.clientY - canvas.offsetTop;
    clicked = false;
}, false);
window.addEventListener("mousemove", function (args) {
    mishkaX = args.clientX - canvas.offsetLeft;
    mishkaY = args.clientY - canvas.offsetTop;
    if (mishkaX <= 500 && mishkaY <= 500) {
        if (clicked) {
            image[Math.floor(mishkaX / 20)][Math.floor(mishkaY / 20)] = 1;
        }
    }
}, false);
window.addEventListener("mousedown", function (args) {
    mishkaX = args.clientX - canvas.offsetLeft;
    mishkaY = args.clientY - canvas.offsetTop;
    image[Math.floor(mishkaX / 20)][Math.floor(mishkaY / 20)] = 1;
    clicked = true;
    console.log(args);
}, false);


function update() {
    if (color1 == "transparent") {
        canvas.style.cursor = "none";
        iRub = true;
    }
    else {
        canvas.style.cursor = "crosshair";
        iRub = false;
    }
    setTimeout(update, 10);	//kolko chesto da se dviji
}

function draw() {	//specialna funkcia v koqto shte pishem koda za risuvane. Shte bude vikana, kogato ni se risuva

    context.clearRect(0, 0, 0, 0);    //NEBAR!
    context.globalAlpha = 1;

    if (br == 0) {
        context.fillStyle = "#FFFFFF";//izbor na cvqt
        context.fillRect(0, 0, 500, 500);
        br++;
    }


    for (var i = -1; i < 500; i += 20) {

        context.fillStyle = "#000000";//izbor na cvqt
        context.fillRect(i, 0, 2, 500)                             //NEBAR! k
    }

    for (var i = -1; i < 500; i += 20) {

        context.fillStyle = "#000000";//izbor na cvqt
        context.fillRect(0, i, 500, 2)                             //NEBAR! k
    }

    for (var i = 0; i < 25; i += 1) {
        for (var j = 0; j < 25; j += 1) {
            if (image[i][j] == 1) {
                context.fillStyle = color1;
                context.fillRect((i * 20)-1, (j * 20)-1, 22, 22);
                image[i][j] = color1;
            }
        }
    }
    if (iRub) {
        context.drawImage(eraser.png, mishkaX, mishkaY, 5, 5);
    }

    requestAnimationFrame(draw);	//NEBAR!
}
update();	//purvo vikane. ne go zatrivai!
draw();	//purvo vikane. ne go zatrivai!
