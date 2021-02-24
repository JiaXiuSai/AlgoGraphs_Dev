// form input and parsing
const inputForm = document.getElementById('userInputForm');
inputForm.addEventListener('submit', function (event) {
  try {
    // stop default form action (client-side)
    event.preventDefault();

    if (document.getElementById("typeToggle").checked) {
      type = "SG";
    } else {
      type = "DG";
    }
    var graph = document.getElementById('graph').value;
    var nodes = document.getElementById("nodes").value;
    var algorithms = document.getElementById('algorithms').value;
    var source = document.getElementById("source").value;
    var destination = document.getElementById('destination').value;
    var error_nodes = document.getElementById('error-nodes');
    var error_graphs = document.getElementById('error-graphs');
    var error_source = document.getElementById('error-source');
    var error_destination = document.getElementById('error-destination');

    if (graph == 'Custom') {
      var matrix = [];
      for (var m = 0; m < nodes; m++) {
        matrix[m] = [];
        for (var n = 0; n < nodes; n++) {
          matrix[m][n] = 0;
        }
      }
      for (var i = 0; i + 1 < nodes; i++) {
        for (var j = i + 1; j < nodes; j++) {
          var z = 10 * i + j;
          if (document.getElementById(z).checked) {
            x = z.toString();
            if (x.length == 1) {
              var a = parseInt(x);
              if (matrix[0][a] == 0) {
                matrix[0][a] = 1;
                matrix[a][0] = 1;
              } else {
                matrix[0][a] = 0;
                matrix[a][0] = 0;
              }
            } else {
              var a = parseInt(x.charAt(0));
              var b = parseInt(x.charAt(1));
              if (matrix[a][b] == 0) {
                matrix[a][b] = 1;
                matrix[b][a] = 1;
              } else {
                matrix[a][b] = 0;
                matrix[b][a] = 0;
              }
            }
          }
        }
      }
      graph = matrix;
    }
    if (isNaN(nodes)) {
      if (graph == 'Hypercubes') {
        error_nodes.innerHTML = "Must be 1, 2 ,4 or 8 nodes.";
      } else {
        error_nodes.innerHTML = "Must be between 1 to 10 nodes";
      }
      error_nodes.classList.add("d-block");
      return
    } else {
      if (graph == 'Hypercubes' && (nodes != '1' || nodes != '2' || nodes != '4' || nodes != '8')) {
        error_nodes.innerHTML = "Must be 1, 2 ,4 or 8 nodes.";
        error_nodes.classList.add("d-block");
        return
      }
    }
    if (graph == 'None') {
      error_graphs.classList.add("d-block");
      return
    }
    if (algorithms == 'SP') {
      if (nodes == 1) {
        error_nodes.innerHTML = "Must be more than 1 for dijkstra's algorithm.";
        error_nodes.classList.add("d-block");
        return
      }
      if (isNaN(source) || source > nodes) {
        error_source.innerHTML = "Source node must be between 1 and " + nodes + ".";
        error_source.classList.add("d-block");
        return
      }
      if (isNaN(destination) || destination > nodes) {
        error_destination.innerHTML = "Destination node must be between 1 and " + nodes + ".";
        error_destination.classList.add("d-block");
        return
      }
      if (source == destination) {
        error_destination.innerHTML = "Destination node cannot be the same as Source node.";
        error_destination.classList.add("d-block");
        return
      }
    }
    userInput = [type, graph, nodes, source, destination, algorithms]
    error_nodes.classList.remove("d-block");
    error_graphs.classList.remove("d-block");
    error_source.classList.remove("d-block");
    error_destination.classList.remove("d-block");
    console.log(userInput)
  } catch (error) {
    window.alert(error);
  }
});


// button control functions for increasing number of nodes nodes
function upNodes(max) {
  if ('Hypercubes' == document.getElementById("graph").value) {
    if (document.getElementById("nodes").value > 3) {
      document.getElementById("nodes").value = 8
    } else if (document.getElementById("nodes").value > 1) {
      document.getElementById("nodes").value = 4
    } else {
      document.getElementById("nodes").value = 2
    }
  } else {
    document.getElementById("nodes").value = parseInt(document.getElementById("nodes").value) + 1;
    if (document.getElementById("nodes").value >= parseInt(max)) {
      document.getElementById("nodes").value = max;
    }
    if (document.getElementById("nodes").value == "NaN") {
      document.getElementById("nodes").value = max;
    }
    if (document.getElementById('graph').value == "Custom") {
      graphDesc.innerHTML = "Select Edges ";
      var gr = createGrid(document.getElementById("nodes").value);
      document.getElementById('grid').appendChild(gr);
    }
  }
}


// button control functions for decreasing number of nodes nodes
function downNodes(min) {
  if ('Hypercubes' == document.getElementById("graph").value) {
    if (document.getElementById("nodes").value > 8) {
      document.getElementById("nodes").value = 8
    } else if (document.getElementById("nodes").value > 4) {
      document.getElementById("nodes").value = 4
    } else if (document.getElementById("nodes").value > 2) {
      document.getElementById("nodes").value = 2
    } else {
      document.getElementById("nodes").value = 1
    }
  } else {
    document.getElementById("nodes").value = parseInt(document.getElementById("nodes").value) - 1;
    if (document.getElementById("nodes").value <= parseInt(min)) {
      document.getElementById("nodes").value = min;
    }
    if (document.getElementById("nodes").value == "NaN") {
      document.getElementById("nodes").value = min;
    }
    if (document.getElementById('graph').value == "Custom") {
      graphDesc.innerHTML = "Select Edges ";
      var gr = createGrid(document.getElementById("nodes").value);
      document.getElementById('grid').appendChild(gr);
    }
  }
}


const graphDescDict = {
  None: "<h6 class=\"card-subtitle mb-2 text-muted text-center\">Choose an example graph to see description</h6>",
  Cycle: "<h5 class=\"card-title\">Cycle Graph</h5><p class=\"card-text\">A cycle graph or circular graph is a graph that consists of a single cycle, or in other words, some number of vertices (at least 3, if the graph is simple) connected in a closed chain</p><a href=\"https://www.google.com/search?q=Cycle+Graph\" class=\"card-link\" target=\"_blank\" rel=\"noreferrer noopener\">Google</a>",
  Star: "<h5 class=\"card-title\">Star Graph</h5><p class=\"card-text\">Star graph is a special type of graph in which n-1 vertices have degree 1 and a single vertex have degree n – 1.</p><a href=\"https://www.google.com/search?q=Star+Graph\" class=\"card-link\" target=\"_blank\" rel=\"noreferrer noopener\">Google</a>",
  Path: "<h5 class=\"card-title\">Path Graph</h5><p class=\"card-text\">The path graph is a tree with two nodes of vertex degree 1, and the other nodes of vertex degree 2.</p><a href=\"https://www.google.com/search?q=Path+Graph\" class=\"card-link\" target=\"_blank\" rel=\"noreferrer noopener\">Google</a>",
  Tree: "<h5 class=\"card-title\">Tree Graph</h5><p class=\"card-text\">A tree is an undirected graph in which any two vertices are connected by exactly one path, or equivalently a connected acyclic undirected graph.</p><a href=\"https://www.google.com/search?q=Tree+Graph\" class=\"card-link\" target=\"_blank\" rel=\"noreferrer noopener\">Google</a>",
  Complete: "<h5 class=\"card-title\">Complete Graph</h5><p class=\"card-text\">A complete graph is a simple undirected graph in which every pair of distinct vertices is connected by a unique edge</p><a href=\"https://www.google.com/search?q=Complete+Graph\" class=\"card-link\" target=\"_blank\" rel=\"noreferrer noopener\">Google</a>",
  Bipartite: "<h5 class=\"card-title\">Bipartite Graph</h5><p class=\"card-text\">A bipartite graph (or bigraph) is a graph whose vertices can be divided into two disjoint and independent sets U and V such that every edge connects a vertex in U to one in V.</p><a href=\"https://www.google.com/search?q=Bipartite+Graph\" class=\"card-link\" target=\"_blank\" rel=\"noreferrer noopener\">Google</a>",
  Hypercubes: "<h5 class=\"card-title\">Hypercubes Graph</h5><p class=\"card-text\">The hypercube graph Q<sub>n</sub> is the graph formed from the vertices and edges of an n-dimensional hypercube.</p><a href=\"https://www.google.com/search?q=Hypercube+Graph\" class=\"card-link\" target=\"_blank\" rel=\"noreferrer noopener\">Google</a>",
  Petersen: "<h5 class=\"card-title\">Petersen Graph</h5><p class=\"card-text\">The Petersen graph is an undirected graph with 10 vertices and 15 edges. It can be described as pentagon with a connected star inside.</p><a href=\"https://www.google.com/search?q=Petersen+Graph\" class=\"card-link\" target=\"_blank\ rel=\"noreferrer noopener\">Google</a>",
}


// function for changing graphs
function changeGraph() {
  var graph = document.getElementById('graph').value;
  var graphDesc = document.getElementById('graphDesc');
  if (graph == "Petersen") {
    document.getElementById("nodes").value = "10";
    document.getElementById("up").disabled = true;
    document.getElementById("down").disabled = true;
    document.getElementById("nodes").disabled = true;
  } else if (graph == "Hypercubes") {
    if (document.getElementById("nodes").value > 7) {
      document.getElementById("nodes").value = 8
    } else if (document.getElementById("nodes").value > 3) {
      document.getElementById("nodes").value = 4
    } else {
      document.getElementById("nodes").value = 1
    }
    document.getElementById("up").disabled = false;
    document.getElementById("down").disabled = false;
    document.getElementById("nodes").disabled = false;
  } else {
    if (document.getElementById("nodes").value >= 10) {
      document.getElementById("nodes").value = 10;
    }
    document.getElementById("up").disabled = false;
    document.getElementById("down").disabled = false;
    document.getElementById("nodes").disabled = false;
  }
  if (graph == "Custom") {
    graphDesc.innerHTML = "Select Edges ";
    var gr = createGrid(document.getElementById("nodes").value);
    document.getElementById('grid').appendChild(gr);
  } else {
    graphDesc.innerHTML = graphDescDict[graph];
    document.getElementById('grid').innerHTML = "";
  }
}


const algoDescDict = {
  None: "<h6 class=\"card-subtitle mb-2 text-muted text-center\">Select an example algorithm to see description</h6>",
  BFS: "<h5 class=\"card-title\">Breadth-first search</h5><p class=\"card-text\">Breadth-first search is a graph traversal algorithm that starts traversing the graph from root node and explores all the neighbouring nodes. Then, it selects the nearest node and explores all the unexplored nodes. The algorithm follows the same process for each of the nearest nodes until it finds the goal.</p><a href=\"https://www.google.com/search?q=Breath+First+Search\" class=\"card-link\" target=\"_blank\" rel=\"noreferrer noopener\">Google</a>",
  DFS: "<h5 class=\"card-title\">Depth-first search</h5><p class=\"card-text\">Depth-first search is a graph traversal algorithm that starts traversing the graph from the root node and explores as far as possible along each branch before backtracking. So the basic idea is to start from the root or any arbitrary node and mark the node and move to the adjacent unmarked node and continue this loop until there is no unmarked adjacent node. Then backtrack and check for other unmarked nodes and traverse them.</p><a href=\"https://www.google.com/search?q=Depth+First+Search\" class=\"card-link\" target=\"_blank\" rel=\"noreferrer noopener\">Google</a>",
  SP: "<h5 class=\"card-title\">Dijkstra's algorithm</h5><p class=\"card-text\">Dijkstra's algorithm solves the problem of finding the shortest path from a point in a graph (the source) to a destination. The graph representing all the paths from one vertex to all the others must be a spanning tree - it must include all vertices. There will also be no cycles as a cycle would define more than one path from the selected vertex to at least one other vertex. The steps for implementing Dijkstra’s algorithm are as follows: <ol><li>Mark your selected initial node with a current distance of 0 and the rest with infinity.</li><li> Set the non-visited node with the smallest current distance as the current node C.</li><li> For each neighbour N of your current node C: add the current distance of C with the weight of the edge connecting C-N.</li><li> If it's smaller than the current distance of N, set it as the new current distance of N. Mark the current node C as visited.</li><li>If there are non-visited nodes, go to step 2.</li></ol><a href=\"https://www.google.com/search?q=Dijkstra+algorithm\" class=\"card-link\" target=\"_blank\" rel=\"noreferrer noopener\">Google</a>",
  CD: "<h5 class=\"card-title\">Cycle Detection</h5><p class=\"card-text\">Run a DFS from every unvisited node. Depth First Traversal can be used to detect a cycle in a Graph. DFS for a connected graph produces a tree. There is a cycle in a graph only if there is a back edge present in the graph. A back edge is an edge that is joining a node to itself (self-loop) or one of its ancestor in the tree produced by DFS. To find the back edge to any of its ancestor keep a visited array and if there is a back edge to any visited node then there is a loop and return true.</h6>"

}

const algoBlankDict = {
  None: "<h6 class=\"card-subtitle mb-2 text-muted text-center\">Select an example algorithm to see code</h6>",
  BFS: "<i>G</i> = graph<br><i>root</i> = starting node<br>BFS(<i>G</i>, <i>root</i>)<br><br>let <i>Q</i> be a queue<br>label <i>root</i> as discovered<br><input><br><br><b>while</b> <i>Q</i>  is not empty <b>do</b><ol><i>v</i> = <i>Q</i>.dequeue()<br><b>if</b> <input> <b>then</b><ol><b>return</b> <i>v</i></ol><b>for all</b> edges from <i>v</i> to <i>w</i> <b>in</b> <i>G</i>.adjacent(<i>v</i>) <b>do</b><ol><b>if</b> <i>w</i> is not labeled as discovered <b>then</b><ol>label <i>w</i> as discovered<br><input></ol></ol></ol><br><button id='ansBtn' class='btn btn-outline-dark' onclick='toggle()'>See Answers</button>",
  DFS: "<i>G</i> = graph<br><i>v</i> = starting node<br>DFS(<i>G</i>, <i>v</i>)<br><br>label <i>v</i> as discovered<br><br><b>for all</b> <i>v</i> to <i>w</i> <b>in</b> <i>G</i>.adjacent(<i>v</i>) <b>do</b><ol><b>if</b> vertex <i>w</i> is not labeled as discovered <b>then</b><ol><input></ol></ol><br><button id='ansBtn' class='btn btn-outline-dark' onclick='toggle()'>See Answers</button>",
  SP: "<i>G</i> = graph<br><i>start</i> = starting node<br>Dijkstra(<i>G</i>, <i>start</i>)<br><br>let <i>Q</i> be a set of nodes<br><br><b>for each</b> vertex <i>v</i> in <i>G</i> <b>do</b><ol>distance[<i>v</i>] = infinity<br>prev[<i>v</i>] = undefined<br>add <i>v</i> to <i>Q</i></ol><input><br><br><b>while</b> <input> <b>do</b><ol><i>u</i> = vertex in <i>Q</i> with minimum distance[<i>u</i>]<br>remove <i>u</i> from <i>Q</i><br><b>for each</b> neighbor <i>v</i> of <i>u</i> <b>do</b><ol><i>compare</i> = <input><br><b>if</b> <i>compare</i> < distance[<i>v</i>] <b>do</b><ol>distance[<i>v</i>] = <i>compare</i><br>prev[<i>v</i>] = <i>u</i></ol></ol></ol><b>return</b> distance[], prev[]<br><br><br><button id='ansBtn' class='btn btn-outline-dark' onclick='toggle()'>See Answers</button>",
  CD: "<i>G</i> = graph<br><i>v</i> = any vertex in <i>G</i><br><br><b>if</b> <input> finds edge that points to <input> <b>then</b><ol><b>return</b> true</ol><br><button id='ansBtn' class='btn btn-outline-dark' onclick='toggle()'>See Answers</button>"
}

const algoAnsDict = {
  None: "<h6 class=\"card-subtitle mb-2 text-muted text-center\">Select an example algorithm to see code</h6>",
  BFS: "<i>G</i> = graph<br><i>root</i> = starting node<br>BFS(<i>G</i>, <i>root</i>)<br><br>let <i>Q</i> be a queue<br>label <i>root</i> as discovered<br><i>Q</i>.enqueue(<i>root</i>)<br><br><b>while</b> <i>Q</i>  is not empty <b>do</b><ol><i>v</i> = <i>Q</i>.dequeue()<br><b>if</b> <i>v</i> is the goal <b>then</b><ol><b>return</b> <i>v</i></ol><b>for all</b> edges from <i>v</i> to <i>w</i> <b>in</b> <i>G</i>.adjacent(<i>v</i>) <b>do</b><ol><b>if</b> <i>w</i> is not labeled as discovered <b>then</b><ol>label <i>w</i> as discovered<br><i>Q</i>.enqueue(<i>w</i>)</ol></ol></ol><br><button id='ansBtn' class='btn btn-outline-dark' onclick='toggle()'>Hide Answers</button>",
  DFS: "<i>G</i> = graph<br><i>v</i> = starting node<br>DFS(<i>G</i>, <i>v</i>)<br><br>label <i>v</i> as discovered<br><br><b>for all</b> <i>v</i> to <i>w</i> <b>in</b> <i>G</i>.adjacent(<i>v</i>) <b>do</b><ol><b>if</b> vertex <i>w</i> is not labeled as discovered <b>then</b><ol>recursively call DFS(<i>G</i>, <i>w</i>)</ol></ol><br><button id='ansBtn' class='btn btn-outline-dark' onclick='toggle()'>Hide Answers</button>",
  SP: "<i>G</i> = graph<br><i>start</i> = starting node<br>Dijkstra(<i>G</i>, <i>start</i>)<br><br>let <i>Q</i> be a set of nodes<br><br><b>for each</b> vertex <i>v</i> in <i>G</i> <b>do</b><ol>distance[<i>v</i>] = infinity<br>prev[<i>v</i>] = undefined<br>add <i>v</i> to <i>Q</i></ol>distance[<i>start</i>] = 0<br><br><b>while</b> <i>Q</i> is not empty <b>do</b><ol><i>u</i> = vertex in <i>Q</i> with minimum distance[<i>u</i>]<br>remove <i>u</i> from <i>Q</i><br><b>for each</b> neighbor <i>v</i> of <i>u</i> <b>do</b><ol><i>compare</i> = distance[<i>u</i>] + length(<i>u</i>, <i>v</i>)<br><b>if</b> <i>compare</i> < distance[<i>v</i>] <b>do</b><ol>distance[<i>v</i>] = <i>compare</i><br>prev[<i>v</i>] = <i>u</i></ol></ol></ol><b>return</b> distance[], prev[]<br><br><br><button id='ansBtn' class='btn btn-outline-dark' onclick='toggle()'>Hide Answers</button>",
  CD: "<i>G</i> = graph<br><i>v</i> = any vertex in <i>G</i><br><br><b>if</b> DFS(<i>G</i>, <i>v</i>) finds edge that points to ancestor of current vertex <b>then</b><ol><b>return</b> true</ol><br><button id='ansBtn' class='btn btn-outline-dark' onclick='toggle()'>Hide Answers</button>"
}


// Function for changing algorithms
function changeAlgo() {
  var algorithms = document.getElementById('algorithms').value;
  var algoDesc = document.getElementById('algoDesc');
  if (document.getElementById("codeBtn").innerHTML == "Code") {
    algoDesc.innerHTML = algoDescDict[algorithms];
  } else {
    algoDesc.innerHTML = algoBlankDict[algorithms];
  }
  var source = document.getElementById('Dijkstra');
  if (algorithms == "SP") {
    source.style.display = '';
  } else {
    source.style.display = "none";
  }
}


// Reset for description boxes
function resetDesc() {
  graphDesc.innerHTML = graphDescDict["None"];
  document.getElementById('grid').innerHTML = "";
  algoDesc.innerHTML = algoDescDict["None"];
  document.getElementById("codeBtn").innerHTML = "Code";
}


// SLideshow functions
// TODO incorporate backend
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

speedSlider.addEventListener('click', function () {
  var scale = speedSlider.value
  speed = 2000 + (1 - scale) * 1500;
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
    }, speed / 2);
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
  gr.id = 'gtable'


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
      var column = document.createElement('td');
      var cbox = document.createElement('input');
      var z = 10 * i + j;
      cbox.type = 'checkbox';
      cbox.id = z;

      column.appendChild(cbox)
      row.appendChild(column);
    }
    gr.appendChild(row);
  }
  return gr;
}


function toggle() {
  var algorithms = document.getElementById('algorithms').value;
  var algoDesc = document.getElementById('algoDesc');
  if (document.getElementById("ansBtn").innerHTML == 'See Answers') {
    algoDesc.innerHTML = algoAnsDict[algorithms];
  } else {
    var algorithms = document.getElementById('algorithms').value;
    var algoDesc = document.getElementById('algoDesc');
    algoDesc.innerHTML = algoBlankDict[algorithms];
  }
}


function codeMode() {
  if (document.getElementById("codeBtn").innerHTML == "Code") {
    var algorithms = document.getElementById('algorithms').value;
    var algoDesc = document.getElementById('algoDesc');
    algoDesc.innerHTML = algoBlankDict[algorithms];
    document.getElementById("codeBtn").innerHTML = "Description";
  } else {
    var algorithms = document.getElementById('algorithms').value;
    var algoDesc = document.getElementById('algoDesc');
    algoDesc.innerHTML = algoDescDict[algorithms];
    document.getElementById("codeBtn").innerHTML = "Code";
  }
}