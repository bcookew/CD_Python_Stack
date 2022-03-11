// Given a dollar amount with change (an integer w/decimal) convert to change. Make sure to count the largest denomination first!

// Example: 3.21 --> 12 quarters, 2 dimes, 1 penny

// function convertCoinChange(money) {
//     // declare variables for different denominations (quarter, dime, nickel, penny)
//     q = 0 // each variable holds the count of each coin
//     d = 0
//     n = 0
//     p = 0 

//     // multiply input by 100 : 3.21 == 321
    
//     // take new number (321) and divide by 25 to get the number of quarters
//     // make sure to round down to get a whole number
//     // subtract the (# of quarters * 25) from the overall input # and then check the next denomination
//     // repeat for different denominations
//     // print and then return the data you collected
// }

function generateCoinChange(input) {
    console.log(`Money Recieved: $${input}`);
    var change = {"Quarters":0,"Dimes":0,"Nickels":0,"Pennies":0};
    var centsStarting = input * 100;
    // var centsStarting = Math.round(input * 100);
    console.log(input, centsStarting);
    
    change["Quarters"] = Math.floor(centsStarting/25)
    remainder = centsStarting%25;
    
    change["Dimes"] = Math.floor(remainder/10);
    remainder = remainder%10;
    
    change["Nickels"] = Math.floor(remainder/5);
    remainder = remainder%5;
    
    change["Pennies"] = remainder;
    
    for (const key in change) {
        console.log(`${key}: ${change[key]}`);
    }
    // console.log(change);
    return change
}

generateCoinChange(3.21)
generateCoinChange(1.40)
generateCoinChange(20.40)