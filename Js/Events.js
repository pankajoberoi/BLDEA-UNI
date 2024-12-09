// function doSomething(){
//     alert("Khanna khilao bichare ko fir")
// }

// let button=document.getElementById('btn')

// button.onclick = () => { 
//     alert("bahar fenk isko")
// }
// button.onclick = () => {
//     console.log("button clicked")
// }



let button=document.getElementById('btn')

function one(){
    alert("Langar thodi hai")
}
function two(){
    console.log("button click")
}

button.addEventListener('click',one);
button.addEventListener('click',two);
// addEventListener(event,function)


