// const arr = [5,2,8,7,6]

//task is to double every element of the array
//1.visit every element
//2.u will perform an action on it

// const output=arr.map(double)

// function double(x){
//     return x*2;
// }

// console.log(arr)
// console.log(output)

// function addbonus (salary){
//     salary=salary+1000;
//     return salary;
// }

// (salary)=>{
//     salary=salary+1000;
//     return salary;
// }

// (salary) => salary+=1000;

// const dividedOutput=arr.map((y) => y/2);
// console.log(dividedOutput)

// ==================================================
// filter

// const arr=[5,1,2,6,9];

// function isOdd(x){
//     return (x%2) != 0;
// }

// function greater(x){
//     return x>4;
// }

// const output=arr.filter(greater)

// console.log(output)

// ===========================================================
// reduce
                         
// const arr = [2, 5, 6, 1, 8];  

// let sum = 0;
// for (let i = 0; i < arr.length; i++) {
//   sum = sum + arr[i];
// }

// console.log(sum)

// const output=arr.reduce((acc,curr)=>{
//     acc=acc+curr;
//     return acc;
// },0)

// console.log(output)

                                         
const arr = [2, 5, 6, 1, 8];

const output=arr.reduce((max,curr)=>{
    if(curr>max){
        max=curr
    }
    return max;
},0)

console.log(output)




