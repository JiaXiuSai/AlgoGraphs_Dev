// TODO: Form validation
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
    var graph = document.getElementById('graph').value;
    var nodes = document.getElementById('nodes').value;
    var algorithms = document.getElementById('algorithms').value;
    userInput = [graph, graph, nodes, algorithms]
    alert(userInput)
  } catch (error) {
    window.alert(error);
  }
});
const graphDescDict = {
  None: "Select an example graph to see description",
  Cycle: "A cycle graph or circular graph is a graph that consists of a single cycle, or in other words, some number of vertices (at least 3, if the graph is simple) connected in a closed chain",
  Star: "Star graph is a special type of graph in which n-1 vertices have degree 1 and a single vertex have degree n – 1.",
  Path: "The path graph is a tree with two nodes of vertex degree 1, and the other. nodes of vertex degree 2.",
  Tree: "A tree is an undirected graph in which any two vertices are connected by exactly one path, or equivalently a connected acyclic undirected graph.",
  Complete: "A complete graph is a simple undirected graph in which every pair of distinct vertices is connected by a unique edge",
  Bipartite: "A bipartite graph (or bigraph) is a graph whose vertices can be divided into two disjoint and independent sets U and V such that every edge connects a vertex in U to one in V.",
  Hypercubes: "The hypercube graph Q<sub>n</sub> is the graph formed from the vertices and edges of an n-dimensional hypercube.",
  Petersen: "The Petersen graph is an undirected graph with 10 vertices and 15 edges.",
  Custom: "CUSTOM TODO"
}

function changeGraph() {
  var graph = document.getElementById('graph').value;
  var graphDesc = document.getElementById('graphDesc');
  graphDesc.innerHTML = graphDescDict[graph];
}

const algoDescDict = {
  None: "Select an example algorithm to see description",
  BFS: "Breadth-first search is a graph traversal algorithm that starts traversing the graph from root node and explores all the neighbouring nodes. Then, it selects the nearest node and explores all the unexplored nodes. The algorithm follows the same process for each of the nearest nodes until it finds the goal.",
  DFS: "Depth-first search is a graph traversal algorithm that starts traversing the graph from the root node and explores as far as possible along each branch before backtracking. So the basic idea is to start from the root or any arbitrary node and mark the node and move to the adjacent unmarked node and continue this loop until there is no unmarked adjacent node. Then backtrack and check for other unmarked nodes and traverse them.",
  SP: "Djikstra's algorithm solves the problem of finding the shortest path from a point in a graph (the source) to a destination. Using this, one can find the shortest paths from a given source to all points in a graph at the same time, hence this problem is sometimes called the single-source shortest paths problem. The graph representing all the paths from one vertex to all the others must be a spanning tree - it must include all vertices. There will also be no cycles as a cycle would define more than one path from the selected vertex to at least one other vertex. The steps for implementing Dijkstra’s algorithm are as follows: <ol><li>Mark your selected initial node with a current distance of 0 and the rest with infinity.</li><li> Set the non-visited node with the smallest current distance as the current node C.</li><li> For each neighbour N of your current node C: add the current distance of C with the weight of the edge connecting C-N.</li><li> If it's smaller than the current distance of N, set it as the new current distance of N. Mark the current node C as visited.</li><li>If there are non-visited nodes, go to step 2.</li></ol>",
  MST: "Kruskal's algorithm to find the minimum cost spanning tree uses the greedy approach. This algorithm treats the graph as a forest and every node it has as an individual tree. A tree connects to another only and only if, it has the least cost among all available options and does not violate MST properties. The steps for implementing Kruskal's algorithm are as follows:<ol><li> Sort all the edges from low weight to high.</li><li> Take the edge with the lowest weight and add it to the spanning tree.</li><li> If adding the edge created a cycle, then reject this edge.</li><li> Keep adding edges until we reach all vertices.</li><ol>",
  CD: "To decide if directed or not"
}

function changeAlgo() {
  var algorithms = document.getElementById('algorithms').value;
  var algoDesc = document.getElementById('algoDesc');
  algoDesc.innerHTML = algoDescDict[algorithms];
}

var x = false
const play = "<svg width=\"2em\" height=\"2em\" viewBox=\"0 0 16 16\" class=\"bi bi-play\" fill=\"currentColor\"><path fill-rule=\"evenodd\" d=\"M10.804 8L5 4.633v6.734L10.804 8zm.792-.696a.802.802 0 0 1 0 1.392l-6.363 3.692C4.713 12.69 4 12.345 4 11.692V4.308c0-.653.713-.998 1.233-.696l6.363 3.692z\"/></svg>"
const pause = "<svg width=\"2em\" height=\"2em\" viewBox=\"0 0 16 16\" class=\"bi bi-pause\" fill=\"currentColor\"><path fill-rule=\"evenodd\" d=\"M6 3.5a.5.5 0 0 1 .5.5v8a.5.5 0 0 1-1 0V4a.5.5 0 0 1 .5-.5zm4 0a.5.5 0 0 1 .5.5v8a.5.5 0 0 1-1 0V4a.5.5 0 0 1 .5-.5z\"/></svg>"
const spinner = "<div class=\"spinner-border\" role=\"status\"><span class=\"sr-only\">Loading...</span></div>"
const startCycle = document.getElementById('startCycle');

startCycle.addEventListener('click', function () {
  if (!x) {
    startCycle.innerHTML = spinner
    x = !x
    startCycle.disabled = true
    setTimeout(function () {
      startCycle.disabled = false;
      startCycle.innerHTML = pause;
    }, 1000);
  } else {
    startCycle.innerHTML = play
    x = !x
  }
});

var imgNumber = 0;
var path = ["Figure_1.png", "Figure_2.png",
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