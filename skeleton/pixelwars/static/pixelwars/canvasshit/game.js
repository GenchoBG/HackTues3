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
var width = 0;
//cursor= none;
//style.cursor.size =  1px
//var cur=new Image();
//cur.src="zemia.jpg";
var iRub = false;
var br = 0;


/*jQuery*/

$(document).ready(function () {
    $("#Nuke").click(function () {
        Nuke();
    });
});


var color1, color2;
$(function () {
    $("button").click(function () {
        color1 = $(this).val();

    });
    $("#colorPicker").click(function () {
        color1 = $("#myColor").val();
        $("#colorPicker").css("background-color", color1);
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

$("#width_setter").change(function (e) {
    width = parseInt($(this).val()) - 1;
    console.log(width);
});

window.addEventListener("mouseup", function (args) {
    mishkaX = args.clientX - canvas.offsetLeft;
    mishkaY = args.clientY - canvas.offsetTop;
    clicked = false;
}, false);
window.addEventListener("mousemove", function (args) {
    mishkaX = args.clientX - canvas.offsetLeft;
    mishkaY = args.clientY - canvas.offsetTop;
    if (mishkaX <= canvas.width && mishkaY <= canvas.height && mishkaX >= 0 && mishkaY >= 0) {
        if (clicked) {
            if (canvas.width - mishkaX >= width * 20 && mishkaY >= width * 20 && canvas.height - mishkaY >= width * 20 && mishkaX >= width * 20 || mishkaX >= width * 20 && mishkaY >= width * 20 && canvas.heigth - mishkaY >= width * 20) {

                for (var k = -width; k < width + 1; k++) {
                    for (var j = -width; j < width + 1; j++) {
                        image[Math.floor(mishkaX / 20) + k][Math.floor(mishkaY / 20) + j] = 1;
                    }
                }
            } else {
                if (canvas.width - mishkaX <= width * 20) {

                    for (var k = -width; k < canvas.width + 1; k++) {
                        for (var j = -width; j < width + 1; j++) {
                            image[Math.floor(mishkaX / 20) + k][Math.floor(mishkaY / 20) + j] = 1;
                        }
                    }

                } else if (canvas.height - mishkaY <= width * 20) {

                    for (var k = -width; k < width + 1; k++) {
                        for (var j = -width; j <= canvas.height; j++) {
                            image[Math.floor(mishkaX / 20) + k][Math.floor(mishkaY / 20) + j] = 1;
                        }
                    }
                } else if (mishkaX <= width * 20) {

                    for (var k = 0; k < width + 1; k++) {
                        for (var j = -width; j <= width + 1; j++) {
                            image[Math.floor(mishkaX / 20) + k][Math.floor(mishkaY / 20) + j] = 1;
                        }
                    }

                } else if (mishkaY <= width * 20) {

                    for (var k = -width; k < width + 1; k++) {
                        for (var j = 0; j <= width + 1; j++) {
                            image[Math.floor(mishkaX / 20) + k][Math.floor(mishkaY / 20) + j] = 1;
                        }
                    }
                }
            }

        }
    }


}, false);

var arr = document.getElementsByClassName('eraser_size');
window.addEventListener("mousedown", function (args) {
    mishkaX = args.clientX - canvas.offsetLeft;
    mishkaY = args.clientY - canvas.offsetTop;
    // check if the cursor is in canvas
    if (mishkaX <= canvas.width && mishkaY <= canvas.height && mishkaX >= 0 && mishkaY >= 0) {
        // check if the drawing mode is in canvas(not outside the array) ->
        // canvas.width=500; canvas.height=500; width=arr[i].value*20;
        if (canvas.width - mishkaX >= width * 20 && mishkaY <= width * 20 && canvas.height - mishkaY >= width * 20 && mishkaX >= width * 20 || mishkaX >= width * 20 && mishkaY >= width * 20 && canvas.heigth - mishkaY >= width * 20) {
            console.log("bad width: " + width);
            for (var k = -width; k < width + 1; k++) {
                for (var j = -width; j < width + 1; j++) {
                    image[Math.floor(mishkaX / 20) + k][Math.floor(mishkaY / 20) + j] = 1;
                }
            }

        } else {


            if (canvas.width - mishkaX <= width * 20) {

                for (var k = -width; k < canvas.width + 1; k++) {
                    for (var j = -width; j < width + 1; j++) {
                        image[Math.floor(mishkaX / 20) + k][Math.floor(mishkaY / 20) + j] = 1;
                    }
                }

            } else if (canvas.height - mishkaY <= width * 20) {

                for (var k = -width; k < width + 1; k++) {
                    for (var j = -width; j <= canvas.height; j++) {
                        image[Math.floor(mishkaX / 20) + k][Math.floor(mishkaY / 20) + j] = 1;
                    }
                }
            } else if (mishkaX <= width * 20) {

                for (var k = 0; k < width + 1; k++) {
                    for (var j = -width; j <= width + 1; j++) {
                        image[Math.floor(mishkaX / 20) + k][Math.floor(mishkaY / 20) + j] = 1;
                    }
                }

            } else if (mishkaY <= width * 20) {

                for (var k = -width; k < width + 1; k++) {
                    for (var j = 0; j <= width + 1; j++) {
                        image[Math.floor(mishkaX / 20) + k][Math.floor(mishkaY / 20) + j] = 1;
                    }
                }
            }
        }

        clicked = true;
    } else {
        console.log("Not appropriate cursor movement!");
    }
}, false);


$("#myForm").submit(function (e) {
    e.preventDefault();
    //console.log($(this).attr("action"));
    //console.log(canvas.toDataURL("image/png"));

    $.ajax({
        url: "submit/",
        method: 'post',
        data: {
            'drawing': canvas.toDataURL("image/png")
        }
    }).then(function (response) {
        console.log(response);
        window.location = response["url"];
    })
});

function update() {
    setTimeout(update, 10);	//kolko chesto da se dviji
}

function clear() {
    for (var i = 0; i < 25; i++) {
        for (var j = 0; j < 25; j++) {
            image[i][j] = 1;
            color1 = 'white';
        }
    }
}


function Nuke() {

    for (var i = 0; i < 25; i++) {
        for (var j = 0; j < 25; j++) {
            image[i][j] = 1;
        }
    }
    console.log(color1)
}
function draw() {	//specialna funkcia v koqto shte pishem koda za risuvane. Shte bude vikana, kogato ni se risuva

    context.clearRect(0, 0, 0, 0);    //NEBAR!
    context.globalAlpha = 1;

    if (br == 0) {
        context.fillStyle = "#FFFFFF";//izbor na cvqt
        context.fillRect(0, 0, canvas.width, canvas.height);
        br++;
    }


    for (var i = -1; i < canvas.width; i += 20) {

        context.fillStyle = "#000000";//izbor na cvqt
        context.fillRect(i, 0, 2, canvas.height)                             //NEBAR! k
    }

    for (var i = -1; i < canvas.height; i += 20) {

        context.fillStyle = "#000000";//izbor na cvqt
        context.fillRect(0, i, canvas.width, 2)                             //NEBAR! k
    }

    for (var i = 0; i < 25; i += 1) {
        for (var j = 0; j < 25; j += 1) {
            if (image[i][j] == 1) {
                context.fillStyle = color1;
                context.fillRect((i * 20) - 1, (j * 20) - 1, 22, 22);
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





