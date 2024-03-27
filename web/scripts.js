class Sketchpad {
    constructor(element, size = 400){
        this.canvas = document.createElement("canvas");
        this.canvas.width = size;
        this.canvas.height = size;
        this.canvas.style=`
            background-color: white;
            box-shadow: 0px 0px 10px 2px black;
        `;
        element.appendChild(this.canvas);

        this.#addEventListeners();
        this.paths = [];
        this.isDrawing = false;
        this.len =  this.paths.length;
    }
    #addEventListeners(){
        this.canvas.onmousedown = (evt)=>{
            const point = this.#getPoint(evt);
            // console.log(point);
            const path = [];  
            path.push(point);
            this.paths.push(path);
            this.len++;
            this.isDrawing = true;
            // console.log(this.paths, this.paths.length);
        }
        this.canvas.onmousemove = (evt) =>{
            if(this.isDrawing){
                const point = this.#getPoint(evt);
                const lastPath = this.paths[this.len - 1];
                lastPath.push(point);
            }
        }
        this.canvas.onmouseup = () =>{
            this.isDrawing = false;            
            // const lastPath = this.paths[this.len - 1];
            // console.log('last path: ', lastPath);
            // console.log('paths: ', this.paths);
        }
    }
    #getPoint(evt){
        const rect = this.canvas.getBoundingClientRect();// give the position of the canvas relative to the viewport
        return [Math.floor(evt.clientX - rect.left), Math.floor(evt.clientY - rect.top)];
    }
    
}