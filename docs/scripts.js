String.prototype.toPersianDigits = function () {
  var id = ["۰", "۱", "۲", "۳", "۴", "۵", "۶", "۷", "۸", "۹"];
  return this.replace(/[0-9]/g, function (w) {
    return id[+w];
  });
};

var canvas = document.querySelector("#canvas");
var ctx = canvas.getContext("2d");
var isDrawing = false;
var timeout = null;

// Set default white background
ctx.fillStyle = "white";
ctx.fillRect(0, 0, canvas.width, canvas.height);

canvas.addEventListener("mousedown", startDrawing);
canvas.addEventListener("touchstart", startDrawing);

function startDrawing(e) {
  e.preventDefault();
  clearCanvas();
  hidePrediction();
  isDrawing = true;
  if (e.type === "mousedown") {
    canvas.addEventListener("mousemove", draw);
    canvas.addEventListener("mouseup", stopDrawing);
  } else if (e.type === "touchstart") {
    canvas.addEventListener("touchmove", draw);
    canvas.addEventListener("touchend", stopDrawing);
  }
  var rect = canvas.getBoundingClientRect();
  var x, y;
  if (
    e.type === "mousedown" ||
    e.type === "mousemove" ||
    e.type === "mouseup"
  ) {
    x = e.clientX - rect.left;
    y = e.clientY - rect.top;
  } else if (
    e.type === "touchstart" ||
    e.type === "touchmove" ||
    e.type === "touchend"
  ) {
    var touch = e.touches[0] || e.changedTouches[0];
    x = touch.clientX - rect.left * (canvas.width / rect.width);
    y = touch.clientY - rect.top * (canvas.height / rect.height);
  }
  ctx.beginPath();
  ctx.fillStyle = "#FFFFFF"; // Set background color to white
  ctx.fillRect(0, 0, canvas.width, canvas.height); // Fill canvas with white background
  ctx.moveTo(x, y);
}

function clearCanvas() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
}

function draw(e) {
  if (!isDrawing) return;
  var rect = canvas.getBoundingClientRect();
  var x, y;
  if (e.type === "mousemove") {
    x = e.clientX - rect.left;
    y = e.clientY - rect.top;
  } else if (e.type === "touchmove") {
    var touch = e.touches[0] || e.changedTouches[0];
    x = touch.clientX - rect.left * (canvas.width / rect.width);
    y = touch.clientY - rect.top * (canvas.height / rect.height);
  }
  ctx.lineWidth = 10;
  ctx.lineJoin = "round";
  ctx.lineCap = "round";
  ctx.strokeStyle = "#000000";
  ctx.lineTo(x, y);
  ctx.stroke();
}

function stopDrawing() {
  isDrawing = false;
  if (timeout) {
    clearTimeout(timeout);
  }
  startPredictTimer();
  canvas.removeEventListener("mousemove", draw);
  canvas.removeEventListener("touchmove", draw);
  canvas.removeEventListener("mouseup", stopDrawing);
  canvas.removeEventListener("touchend", stopDrawing);
}

function hidePrediction() {
  $("#prediction-text").css("visibility", "hidden");
  $("#prediction").css("visibility", "hidden");
}

function showPrediction() {
  $("#prediction-text").css("visibility", "visible");
  $("#prediction").css("visibility", "visible");
}

function startPredictTimer() {
  timeout = setTimeout(predict, 1000); // 1-second delay
}

function predict() {
  var dataURL = canvas.toDataURL();
  $.ajax({
    type: "POST",
    url: "https://digitz-hta5bnf4gyebg2a6.uaenorth-01.azurewebsites.net/predict/",
    data: dataURL,
    success: function (result) {
      console.log("Result:", result); // Log the result for debugging
      if (typeof result === "string") {
        var persianResult = result.toPersianDigits(); // Convert prediction to Persian digits
        $("#prediction").html(persianResult); // Show the prediction number
        showPrediction(); // Display the prediction
      } else {
        console.error("Result is not a string:", result);
      }
    },
  });
}
