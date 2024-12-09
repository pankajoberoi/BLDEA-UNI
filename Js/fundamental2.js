// console.log("Pankaj")

// function logger(){
//     console.log("hello functions")
// }

// logger();


// ============================================
// function fruitProcessor(apple,oranges)
// {
//     const juice=`Juice with ${apple} apples and ${oranges} oranges`
//     return juice;
// }


//  let glass=fruitProcessor(2,3);

// console.log("In Glass " + glass)



// function isPrime (num){
//     let flag=0;
//     for(let i=2;i<num;i++){
//         if(num%i==0){
//             flag++;
//             break;
//         }
//     }
//     if(flag==0){
//         return " its a prime number";
//     }
//     else {
//         return " not Prime number";
//     }
// }

// let number=[20,7,17,24,23];//prime elements only
// //          0  1  2  3  4

// //       1          5
// for(let i=0;i<number.length;i++){//traversing
//    console.log(number[i] + isPrime(number[i])); 
// }

// ===============================================
// Working with objects

let currentYear=2024
let birthyear=2000

let profile = {
    Name : "Pankaj",
    jobProfile:"Trainer",
    exp:3,
    Age:(currentYear-birthyear),
    state:"Punjab",
    jobStatus:true
}

console.log(profile)
console.log(profile.jobProfile)






