// form check and outputs userInput in a string
const inputForm = document.getElementById('userInputForm');
inputForm.addEventListener('submit', function (event) {
  try {
    // stop default form action (client-side)
    event.preventDefault();
    var radios = document.getElementsByName('Radio');
    // find and record check radio value
    for (var i = 0, length = radios.length; i < length; i++) {
      if (radios[i].checked) {
        graph = radios[i].value
        break
      }
    }
    // TODO: Implement some type of check to ensure the backend can compute it
    var example = document.getElementById('example').value;
    var nodes = document.getElementById('nodes').value;
    var algorithms = document.getElementById('algorithms').value;
    userInput = [graph, example, nodes, algorithms]
    alert(userInput)
  } catch (error) {
    window.alert(error);
  }
});

var x = false
const play = "<svg width=\"2em\" height=\"2em\" viewBox=\"0 0 16 16\" class=\"bi bi-play\" fill=\"currentColor\"><path fill-rule=\"evenodd\" d=\"M10.804 8L5 4.633v6.734L10.804 8zm.792-.696a.802.802 0 0 1 0 1.392l-6.363 3.692C4.713 12.69 4 12.345 4 11.692V4.308c0-.653.713-.998 1.233-.696l6.363 3.692z\"/></svg>"
const pause = "<svg width=\"2em\" height=\"2em\" viewBox=\"0 0 16 16\" class=\"bi bi-pause\" fill=\"currentColor\"><path fill-rule=\"evenodd\" d=\"M6 3.5a.5.5 0 0 1 .5.5v8a.5.5 0 0 1-1 0V4a.5.5 0 0 1 .5-.5zm4 0a.5.5 0 0 1 .5.5v8a.5.5 0 0 1-1 0V4a.5.5 0 0 1 .5-.5z\"/></svg>"
const spinner = "<div class=\"spinner-border\" role=\"status\"><span class=\"sr-only\">Loading...</span></div>"
const startCycle = document.getElementById('startCycle');

startCycle.addEventListener('click', function () {
  if (!x){
    startCycle.innerHTML = spinner
    x = !x
    startCycle.disabled = true
    setTimeout(function(){
      startCycle.disabled = false;
      startCycle.innerHTML = pause;
    },1000);
  }
  else{
    startCycle.innerHTML = play
    x = !x
  }
});

var imgNumber = 0;
var path = ["Figure_1.png","Figure_2.png",
  "Figure_3.png",
  "Figure_4.png"
];
var numberOfImg = path.length;
var timer = null;

function slide() {
  imgNumber = (imgNumber + 1) % path.length;
  console.log(imgNumber);
  document.getElementById("imgSlideshow").src = path[imgNumber];
  changeCounter(imgNumber + 1, numberOfImg);
}

function setTimer() {
  if (timer) {
    clearInterval(timer);
    timer = null;
  } else {
    timer = setInterval(slide, 2000);
  }
  return false;
}

function previousImage() {
  --imgNumber;
  if (imgNumber < 0) {
    imgNumber = numberOfImg - 1;
  }
  document.getElementById("imgSlideshow").src = path[imgNumber];
  changeCounter(imgNumber + 1, numberOfImg);
  return false;
}

function nextImage() {
  ++imgNumber;
  if (imgNumber > (numberOfImg - 1)) {
    imgNumber = 0;
  }
  document.getElementById("imgSlideshow").src = path[imgNumber];
  changeCounter(imgNumber + 1, numberOfImg);
  return false;
}

function changeCounter(cur, total) {
  document.getElementById("counter").innerHTML = cur + "/" + total;
}
document.getElementById("counter").innerHTML = 1 + "/" + path.length;