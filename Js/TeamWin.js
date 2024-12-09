let csk=prompt("Enter Team A score");
let rcb=prompt("Enter Team B score");

if(csk>=(2*rcb) && csk>=50 ){
    alert("csk wins");
}
else if(rcb>=(2*csk) && rcb>=50){
    alert("rcb wins")
}
else{
    alert("Time waste hua")
}