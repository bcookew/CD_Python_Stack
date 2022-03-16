// ####################################################

// :graduation: ALGO CHALLENGE DAY #13 @everyone 

// 👇🏻 
// #Count the divisors of a number

// Count the number of divisors of a positive integer n.

// Random tests go up ton = 500000.

// Examples (input --> output)
// 4 --> 3 (1, 2, 4)
// 5 --> 2 (1, 5)
// 12 --> 6 (1, 2, 3, 4, 6, 12)
// 30 --> 8 (1, 2, 3, 5, 6, 10, 15, 30)

function divisors(n){
    let divs = [];
    if(n % 2 === 1){
        for(let i = 1; i<= n; i += 2){
            if (n%i === 0) divs.push(i);
        }
    }
    else{
        for(let i = 1; i<= n; i++){
            if(n%i === 0) divs.push(i);
        }
    }
    let output = `${n} --> ${divs.length} (${divs.join(", ")})`;
    return output;
}
console.log(divisors(499999))
console.log(divisors(500000))