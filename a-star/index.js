const canvas = document.getElementById("main-canvas");
const canvasContext = canvas.getContext("2d");

const boxSize = 10;
const width = 1000;
const cols = width / boxSize;
const height = 800;
const rows = height / boxSize;

class Node {
    constructor(i, j) {
        this.i = i;
        this.j = j;
        this.f = 0;
        this.g = 0;
        this.h = 0;
        this.neighbors = [];
        this.previous = undefined;
        this.visitable = true;

        if(Math.random() < 0.3) {
            this.visitable = false;
        }
    }

    show(color) {
        if(this.visitable) {
            canvasContext.fillStyle = color;
            canvasContext.fillRect(this.i * boxSize, this.j * boxSize, boxSize, boxSize);
            canvasContext.fillStyle = "rgb(0, 0, 0)";
            canvasContext.strokeRect(this.i * boxSize, this.j * boxSize, boxSize, boxSize);
        }
        else {
            canvasContext.fillStyle = "rgb(0, 0, 0,)";
            canvasContext.fillRect(this.i * boxSize, this.j * boxSize, boxSize, boxSize);
        }
    }

    addNeighbors(grid) {
        let i = this.i;
        let j = this.j;
        if(i < cols - 1) {
            this.neighbors.push(grid[i + 1][j]);
        }
        if(i > 0) {
            this.neighbors.push(grid[i - 1][j]);
        }
        if(j < rows - 1) {
            this.neighbors.push(grid[i][j + 1]);
        }
        if(j > 0) {
            this.neighbors.push(grid[i][j - 1]);
        }
    }
}

const grid = new Array(cols);
function generateGrid() {
    for(let i = 0; i < grid.length; i++) {
        grid[i] = new Array(rows);
    }

    for(let i = 0; i < cols; i++) {
        for(let j = 0; j < rows; j++) {
            grid[i][j] = new Node(i, j);
        }
    }

    for(let i = 0; i < cols; i++) {
        for(let j = 0; j < rows; j++) {
            grid[i][j].addNeighbors(grid);
        }
    }
}

function removeFromArray(arr, item) {
    let index = arr.indexOf(item);
    if(index !== -1) {
        arr.splice(index, 1);
    }
}

function heuristic(a, b) {
    let i1 = a.i;
    let j1 = a.j;
    let i2 = b.i;
    let j2 = b.j;
    return Math.sqrt(((i2 - i1) * 2) - ((j2 - j1) * 2));
}

const closedSet = [];
const openSet = [];
var start;
var end;

function setup() {
    generateGrid();
    start = grid[0][0];
    end = grid[cols - 1][rows - 1];
    openSet.push(start);
}

function draw() {
    if(openSet.length > 0) {
        let lowestIndex = 0;
        for(let i = 0; i < openSet.length; i++) {
            let node = openSet[i];
            if(node.f < openSet[lowestIndex].f) {
                lowestIndex = i;
            }
        }

        const current = openSet[lowestIndex];
        if(current === end) {
            let path = [];
            let temp = current;
            while(temp.previous) {
                path.push(temp.previous);
                temp = temp.previous;
            }

            for(let i = 0; i < path.length; i++) {
                path[i].show("rgb(0, 0, 255)");
            }
            return;
        }

        removeFromArray(openSet, current);
        closedSet.push(current);

        let neighbors = current.neighbors;
        for(let i = 0; i < neighbors.length; i++) {
            let neighbor = neighbors[i];
            if(!closedSet.includes(neighbor) && neighbor.visitable) {
                let g = current.g + 1;
                if(openSet.includes(neighbor)) {
                    if(g < neighbor.g) {
                        neighbor.g = g;
                    }
                }
                else {
                    neighbor.g = g;
                    openSet.push(neighbor);
                }
                neighbor.h = heuristic(neighbor, end);
                neighbor.f = neighbor.g + neighbor.h;
                neighbor.previous = current;
            }
        }
    }

    for(let i = 0; i < cols; i++) {
        for(let j = 0; j < rows; j++) {
            let node = grid[i][j];
            node.show("rgb(255, 255, 255)");
        }
    }

    for(let i = 0; i < openSet.length; i++) {
        let node = openSet[i];
        node.show("rgb(0, 255, 0)");
    }

    for(let i = 0; i < closedSet.length; i++) {
        let node = closedSet[i];
        node.show("rgb(255, 0, 0)");
    }
}

setup();
setInterval(draw, 10);