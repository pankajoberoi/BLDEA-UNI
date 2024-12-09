

// console.log("Hello world")//output


// console.log("Jai shree ram")

// let var const=========================================

// let firstName="Pankaj";

// console.log(firstName)

// firstName = "Jhumruu"
// console.log(firstName)


// const PI = 3.14;

// PI=2.13;

// console.log(PI);

// let last_Name="Oberoi"
// console.log(last_Name);

//Data TYPES================================================
// 1.Numbers
// 2.Strings
// 3.Boolean
// 4.undefined
// 5.NULL


// let name1;
// console.log(name1);


// let x=10;
// console.log("x ki value in number" + x);

// x="Pankaj"
// console.log("X ki value in string " + x);



// ==============================================================
// typeof

// console.log(typeof(true))
// console.log(typeof("Kalpana"))
// console.log(typeof(23))
// console.log(typeof(21.2))
// console.log(typeof(undefined))
// console.log(typeof(null))

// +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
// Basic Operators

// Mathematical operator => +,-,*,/,%
//assignement  operator =>  =, +=,-=,*=,/=,%=
 //comparison => ==,===,>=,<=,!=

// console.log(4/2);questionent

// console.log(5%2);remainder


// let a=5;

// let b=10;

// b+=a;

// b=b+a;

// console.log(b);


// console.log("5" === 5);


// let currentYear =2024

// console.log(currentYear+=10 < (currentYear+=25))
//operator precedence
// true -> lakshmi,vishal,soumya
// false -> shaheen,kalpana
// 2025 -> vijay,akhilesh



// ===============================================
// Strings , string templates /template litrals


// const name="Pankaj"
// const job="Trainer"
// const birthyear=2000
// const year=2024;



// const profile= "I am " + name + " my job is " + job + " i am " + (2024-2000) + " years old"

// console.log(profile)

// const profile = `I am ${name} my job is ${job} i am ${year-birthyear} years old`

// console.log(profile)

// let table=prompt("Which table you want to print");

// for(let i=1;i<=10;i++){
//     console.log(table + " x " + i + " = " + (table*i));
// }


let user1=prompt("Enter a number btw 1 to 100")

if(user1>1 && user1<100){
    alert("User2 please guess the number btw 1 to 100")
    let user2;
    let guess=0;
    do{
        user2=prompt("guess a number!");
        if(user2>user1){
            alert("Entered number is greater than original")
        }
        else if(user2<user1){
            alert("Entered number is smaller than original")
        }
        guess++;
    }while(user1!=user2)

    alert("You guess it !!! It took "+ guess + " guesses to guess the number")

}
else{
    alert("Enter a valid number")
}




