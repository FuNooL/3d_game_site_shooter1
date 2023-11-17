from pyscript import document

canvas = document.getElementById("game-view")
ctx = canvas.getContext("2d")

ctx.fillStyle = "green"
ctx.fillRect(10, 10, 150, 100,)
