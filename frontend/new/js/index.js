// form input
// TODO add custom graphs option 
const inputForm = document.getElementById('userInputForm');
inputForm.addEventListener('submit', function (event) {
  try {
    // stop default form action (client-side)
    event.preventDefault();
    var radios = document.getElementsByName('Radio');
    // find and record check radio value
    for (var i = 0, length = radios.length; i < length; i++) {
      if (radios[i].checked) {
        type = radios[i].value
        break
      }
    }
    var graph = document.getElementById('graph').value;
    var nodes = document.getElementById('nodes').value;
    var algorithms = document.getElementById('algorithms').value;
    userInput = [type, graph, nodes, algorithms]
    console.log(userInput)
  } catch (error) {
    window.alert(error);
  }
});

const graphDescDict = {
  None: "<h6 class=\"card-subtitle mb-2 text-muted text-center\">Choose an example graph to see description</h6>",
  Cycle: "<h5 class=\"card-title\">Cycle Graph</h5><p class=\"card-text\">A cycle graph or circular graph is a graph that consists of a single cycle, or in other words, some number of vertices (at least 3, if the graph is simple) connected in a closed chain</p><a href=\"https://www.google.com/search?q=Cycle+Graph\" class=\"card-link\" target=\"_blank\" rel=\"noreferrer noopener\">Google</a>",
  Star: "<h5 class=\"card-title\">Star Graph</h5><p class=\"card-text\">Star graph is a special type of graph in which n-1 vertices have degree 1 and a single vertex have degree n – 1.</p><a href=\"https://www.google.com/search?q=Star+Graph\" class=\"card-link\" target=\"_blank\" rel=\"noreferrer noopener\">Google</a>",
  Path: "<h5 class=\"card-title\">Path Graph</h5><p class=\"card-text\">The path graph is a tree with two nodes of vertex degree 1, and the other nodes of vertex degree 2.</p><a href=\"https://www.google.com/search?q=Path+Graph\" class=\"card-link\" target=\"_blank\" rel=\"noreferrer noopener\">Google</a>",
  Tree: "<h5 class=\"card-title\">Tree Graph</h5><p class=\"card-text\">A tree is an undirected graph in which any two vertices are connected by exactly one path, or equivalently a connected acyclic undirected graph.</p><a href=\"https://www.google.com/search?q=Tree+Graph\" class=\"card-link\" target=\"_blank\" rel=\"noreferrer noopener\">Google</a>",
  Complete: "<h5 class=\"card-title\">Complete Graph</h5><p class=\"card-text\">A complete graph is a simple undirected graph in which every pair of distinct vertices is connected by a unique edge</p><a href=\"https://www.google.com/search?q=Complete+Graph\" class=\"card-link\" target=\"_blank\" rel=\"noreferrer noopener\">Google</a>",
  Bipartite: "<h5 class=\"card-title\">Bipartite Graph</h5><p class=\"card-text\">A bipartite graph (or bigraph) is a graph whose vertices can be divided into two disjoint and independent sets U and V such that every edge connects a vertex in U to one in V.</p><a href=\"https://www.google.com/search?q=Bipartite+Graph\" class=\"card-link\" target=\"_blank\" rel=\"noreferrer noopener\">Google</a>",
  Hypercubes: "<h5 class=\"card-title\">Hypercubes Graph</h5><p class=\"card-text\">The hypercube graph Q<sub>n</sub> is the graph formed from the vertices and edges of an n-dimensional hypercube</p>.<a href=\"https://www.google.com/search?q=Hypercube+Graph\" class=\"card-link\" target=\"_blank\" rel=\"noreferrer noopener\">Google</a>",
  Petersen: "<h5 class=\"card-title\">Petersen Graph</h5><p class=\"card-text\">The Petersen graph is an undirected graph with 10 vertices and 15 edges. It can be described as pentagon with a connected star inside.</p><a href=\"https://www.google.com/search?q=Petersen+Graph\" class=\"card-link\" target=\"_blank\ rel=\"noreferrer noopener\">Google</a>",
}

function changeGraph() {
  var graph = document.getElementById('graph').value;
  var graphDesc = document.getElementById('graphDesc');
  if (graph == "Custom") {
    graphDesc.innerHTML = "Choose number of nodes, then";
    var inputButton = document.createElement('button');
    inputButton.innerHTML = "Select Edges";
    inputButton.type = 'button'
    graphDesc.appendChild(inputButton);
    inputButton.onclick = function () {
      showGrid()
    };

    inputButton.addEventListener('click', function () {
      var gr = createGrid(document.getElementById("nodes").value);
      document.getElementById('grid').appendChild(gr);
    });
  } else {
    graphDesc.innerHTML = graphDescDict[graph];
  }
}

const algoDescDict = {
  None: "<h6 class=\"card-subtitle mb-2 text-muted text-center\">Select an example algorithm to see description</h6>",
  BFS: "<h5 class=\"card-title\">Breadth-first search</h5><p class=\"card-text\">Breadth-first search is a graph traversal algorithm that starts traversing the graph from root node and explores all the neighbouring nodes. Then, it selects the nearest node and explores all the unexplored nodes. The algorithm follows the same process for each of the nearest nodes until it finds the goal.</p><a href=\"https://www.google.com/search?q=Breath+First+Search\" class=\"card-link\" target=\"_blank\" rel=\"noreferrer noopener\">Google</a>",
  DFS: "<h5 class=\"card-title\">Depth-first search</h5><p class=\"card-text\">Depth-first search is a graph traversal algorithm that starts traversing the graph from the root node and explores as far as possible along each branch before backtracking. So the basic idea is to start from the root or any arbitrary node and mark the node and move to the adjacent unmarked node and continue this loop until there is no unmarked adjacent node. Then backtrack and check for other unmarked nodes and traverse them.</p><a href=\"https://www.google.com/search?q=Depth+First+Search\" class=\"card-link\" target=\"_blank\" rel=\"noreferrer noopener\">Google</a>",
  SP: "<h5 class=\"card-title\">Dijkstra's algorithm</h5><p class=\"card-text\">Dijkstra's algorithm solves the problem of finding the shortest path from a point in a graph (the source) to a destination. The graph representing all the paths from one vertex to all the others must be a spanning tree - it must include all vertices. There will also be no cycles as a cycle would define more than one path from the selected vertex to at least one other vertex. The steps for implementing Dijkstra’s algorithm are as follows: <ol><li>Mark your selected initial node with a current distance of 0 and the rest with infinity.</li><li> Set the non-visited node with the smallest current distance as the current node C.</li><li> For each neighbour N of your current node C: add the current distance of C with the weight of the edge connecting C-N.</li><li> If it's smaller than the current distance of N, set it as the new current distance of N. Mark the current node C as visited.</li><li>If there are non-visited nodes, go to step 2.</li></ol><a href=\"https://www.google.com/search?q=Dijkstra+algorithm\" class=\"card-link\" target=\"_blank\" rel=\"noreferrer noopener\">Google</a>",
  MST: "<h5 class=\"card-title\">Kruskal's algorithm</h5><p class=\"card-text\">Kruskal's algorithm to find the minimum cost spanning tree uses the greedy approach. This algorithm treats the graph as a forest and every node it has as an individual tree. A tree connects to another only and only if, it has the least cost among all available options and does not violate MST properties. The steps for implementing Kruskal's algorithm are as follows:<ol><li> Sort all the edges from low weight to high.</li><li> Take the edge with the lowest weight and add it to the spanning tree.</li><li> If adding the edge created a cycle, then reject this edge.</li><li> Keep adding edges until we reach all vertices.</li></ol></p><a href=\"https://www.google.com/search?q=Kruskal+algorithm\" class=\"card-link\" target=\"_blank\" rel=\"noreferrer noopener\">Google</a>",
  CD: "<h6 class=\"card-subtitle mb-2 text-muted text-center\" rel=\"noreferrer noopener\">To decide if directed or not</h6>"
}

function changeAlgo() {
  var algorithms = document.getElementById('algorithms').value;
  var algoDesc = document.getElementById('algoDesc');
  algoDesc.innerHTML = algoDescDict[algorithms];
}

// SLideshow functions
var x = false
var speed = 2000
var path = "assets\\img\\slideshow\\"
var imgNumber = 0;
var img = ["Figure_1.png",
  "Figure_2.png",
  "Figure_3.png",
  "Figure_4.png"
];
var numberOfImg = img.length;
const play = "<i class=\"fa fa-play\" aria-hidden=\"true\"></i>"
const pause = "<i class=\"fa fa-pause\" aria-hidden=\"true\"></i>"
const startCycle = document.getElementById('startCycle');
const sliderLabel = document.getElementById('sliderLabel');
const speedSlider = document.getElementById('speedSlider');

speedSlider.addEventListener('click', function (){
  var scale = speedSlider.value
  speed = 2000 + (1-scale)*1500;
  sliderLabel.innerHTML = "Speed(×" + scale + ")"
  if (timer) {
    clearInterval(timer);
    timer = setInterval(slide, speed);
  }
});

startCycle.addEventListener('click', function () {
  if (!x) {
    x = !x
    startCycle.innerHTML = pause;
    startCycle.disabled = true
    setTimeout(function () {
      startCycle.disabled = false;
      startCycle.innerHTML = pause;
    }, speed/2);
  } else {
    startCycle.innerHTML = play
    x = !x
  }
});


function slide() {
  imgNumber = (imgNumber + 1) % img.length;
  document.getElementById("imgSlideshow").src = path + img[imgNumber];
  changeCounter(imgNumber + 1, numberOfImg);
}

var timer = null;
function setTimer() {
  if (timer) {
    clearInterval(timer);
    timer = null;
  } else {
    timer = setInterval(slide, speed);
    console.log(speed)
  }
  return false;
}

function previousImage() {
  --imgNumber;
  if (imgNumber < 0) {
    imgNumber = numberOfImg - 1;
  }
  document.getElementById("imgSlideshow").src = path + img[imgNumber];
  changeCounter(imgNumber + 1, numberOfImg);
  return false;
}

function nextImage() {
  ++imgNumber;
  if (imgNumber > (numberOfImg - 1)) {
    imgNumber = 0;
  }
  document.getElementById("imgSlideshow").src = path + img[imgNumber];
  changeCounter(imgNumber + 1, numberOfImg);
  return false;
}

function changeCounter(cur, total) {
  document.getElementById("counter").innerHTML = cur + "/" + total;
}
document.getElementById("counter").innerHTML = 1 + "/" + img.length;


//Custom input functions
function showGrid() {
  document.getElementById("form-container*2").style.display = "block";
}

function closeGrid() {
  document.getElementById("form-container*2").style.display = "none";
}

function createGrid(nodes) {
  document.getElementById('grid').innerHTML = "";

  var gr = document.createElement('table');

  for (var i = 0; i < nodes; i++) {
    var row = document.createElement('tr');

    if (i == 0) {
      for (var k = 0; k - 1 < nodes; k++) {
        if (k == 0) {
          var column = document.createElement('td');
          var blank = document.createElement('P');
          blank.innerHTML = "";
          column.appendChild(blank)
          row.appendChild(column);
        } else {
          var column = document.createElement('td');
          var clabel = document.createElement('P');
          clabel.innerHTML = k;
          column.appendChild(clabel)
          row.appendChild(column);
        }
      }
      gr.appendChild(row);
      var row = document.createElement('tr');
    }

    var column = document.createElement('td');
    var rlabel = document.createElement('P');
    rlabel.innerHTML = i + 1;
    column.appendChild(rlabel)
    row.appendChild(column);

    for (var j = 0; j < i + 1; j++) {
      var column = document.createElement('td');
      var dcbox = document.createElement('input');
      dcbox.type = 'checkbox';
      dcbox.disabled = true;
      column.appendChild(dcbox)
      row.appendChild(column);
    }
    for (var j = i + 1; j < nodes; j++) {
      var column = document.createElement('td')
      var cbox = document.createElement('input');
      cbox.type = 'checkbox';
      column.appendChild(cbox)
      row.appendChild(column);
    }
    gr.appendChild(row);
  }
  return gr;
}