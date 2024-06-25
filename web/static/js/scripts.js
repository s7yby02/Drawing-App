class Sketchpad {
    constructor(element, size = 400){
        this.canvas = document.createElement("canvas");
        this.canvas.width = size;
        this.canvas.height = size;
        this.canvas.style=`
            box-shadow: 0px 0px 10px 2px black;
        `;

        element.appendChild(this.canvas);

        this.paths = [];
        this.isDrawing = false;
        this.len =  this.paths.length;
        this.#addEventListeners();
        this.ctx = this.canvas.getContext('2d');
        this.clrs = false;
        // Set the fill style to white and fill the canvas
        this.#fillCanvas(this.ctx);
    }
    #fillCanvas(ctx){
        ctx.fillStyle = 'white';
        ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
    }
    #addEventListeners(){
        ///////Mouse events listeners////////
        this.canvas.onmousedown = (evt) =>{
            const point = this.#getPoint(evt);
            // console.log(point);
            const path = [];
            path.push(point);
            this.paths.push(path);
            this.len++;
            this.isDrawing = true;
        }
        this.canvas.onmousemove = (evt) =>{
            if(this.isDrawing){
                const point = this.#getPoint(evt);
                const lastPath = this.paths[this.len - 1];
                lastPath.push(point);
                // this.clrs = false;
                this.#draw(this.ctx ,lastPath);
            }
        }
        document.onmouseup = () =>{
            this.isDrawing = false;            
            // const lastPath = this.paths[this.len - 1];
            // console.log('last path: ', lastPath);
            // console.log('paths: ', this.paths);
        }
        ///////Touch events listeners////////
        this.canvas.ontouchstart = (evt)=>{
            const loc = evt.touches[0];
            this.canvas.onmousedown(loc);
        }
        this.canvas.ontouchmove = (evt)=>{
            const loc = evt.touches[0];
            this.canvas.onmousemove(loc);
        }
        document.ontouchend = ()=>{
            this.canvas.onmouseup();
        }
    }
    #getPoint(evt){
        const rect = this.canvas.getBoundingClientRect();// give the position of the canvas relative to the viewport
        return [Math.floor(evt.clientX - rect.left), Math.floor(evt.clientY - rect.top)];
    }
    #draw(ctx, path){
        if(this.clrs){
            ctx.strokeStyle = this.#getRandomColor();
        }else{
            ctx.strokeStyle = "black";
        }
        // console.log("colorstyle after #draw() method: ", ctx.strokeStyle);
        ctx.lineWidth = 3;
        ctx.lineCap="round";
        ctx.lineJoin="round";
        ctx.beginPath();
        for(let i =1; i< path.length; i++){
            const from = path[i - 1];
            const to = path[i];
            ctx.moveTo(from[0], from[1]);
            ctx.lineTo(to[0], to[1]);
        }
        ctx.stroke();
    }
    undo(){
        if(this.len ){    
            this.paths.pop();
            this.len--;
            this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
            this.#fillCanvas(this.ctx);
            for(let path of this.paths){
                this.#draw(this.ctx, path);
            }
            // console.log("paths after pop:", this.paths);
        }else{console.log("nothing to undo");}
    }
    clear(){
        this.paths = [];
        this.len = 0;
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
        this.#fillCanvas(this.ctx);
        // console.log("paths after clear:", this.paths);
    }
    #getRandomColor() {
        const r = Math.floor(Math.random() * 256);  // Random between 0-255
        const g = Math.floor(Math.random() * 256);  // Random between 0-255
        const b = Math.floor(Math.random() * 256);  // Random between 0-255
        return 'rgb(' + r + ',' + g + ',' + b + ')';  // Collect all to a string
    }
    colorize(){
        if(this.len){
            this.clrs = !this.clrs;
            this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
            this.#fillCanvas(this.ctx);
            for(let path of this.paths){
                this.#draw(this.ctx, path);
            }
        }
        // console.log("colorstryke after colorize() method",this.ctx.strokeStyle);
    }
}