// 1 5 7 11 15 ? 17
//  4 2 4  4  

// 1 + (2 * 2), 5 + 2, 7 + (2 * 2), 11, 11 + 4, 15 

//   6    12    18    26    32    38
// 1    5     7    11    15  ? 17
  
// 5 

// 7

// 11

// 15

// ?

// 17


function divisors(num1,num2,curGreatInput=1,divInput=1){
    let div = divInput
    var curGreat = curGreatInput
    if(div <= num1 || div <= num2){
        if (num1%div === 0 && num2%div === 0){
            curGreat = div;
        } 
        div++
        curGreat = divisors(num1,num2,curGreat,div)

    }
    return curGreat
}

console.log(divisors(10,5))
console.log(divisors(30,45))
console.log(divisors(80,160))


/////////////////////////////////////
///////Instructors Solution//////////
/////////////////////////////////////

function recursiveGreatestCommonFactor(num1,num2){
    // console.log(num1 + " " + num2)
    if (num1 > num2) {
        return recursiveGreatestCommonFactor(num1-num2, num2);
    } else if (num2 > num1) {
        return recursiveGreatestCommonFactor(num1, num2-num1);
    } else {
        return num1
    }
}

console.log(recursiveGreatestCommonFactor(10,5))
console.log(recursiveGreatestCommonFactor(30,45))
console.log(recursiveGreatestCommonFactor(80,160))




// for(let i = 1; i<= num1; i++){
//     if(num1%i === 0) divs.push(i);
// }
// let output = `${num1} --> ${divs.length} (${divs.join(", ")})`;
// return output;