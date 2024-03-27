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
    }
    #addEventListeners(){
        this.canvas.onmousedown = (evt)=>{
            
        }
    }
}