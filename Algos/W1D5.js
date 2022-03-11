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
    console.log(`\n\nMoney Recieved: $${input}\n`); //Display user input
    var denominations = {"Quarters":[25,0],"Dimes":[10,0],"Nickels":[5,0],"Pennies":[1,0]}; // Define denominations and counters

    var cents = Math.round(input * 100); // Convert dollars to cents

    for(denom in denominations){ // Iterate through denominations
        denominations[denom][1] = Math.floor(cents/denominations[denom][0]) // Update counter for denom
        cents = cents%denominations[denom][0]; // Update remaining cents to be converted to denom
    }

    console.log("Change given:"); 
    for (const denom in denominations) { // Iterate through denominations 
        console.log(`    ${denom}: ${denominations[denom][1]}`); // Print interpolation of denom key name and counter value
    }

    return denominations
}

generateCoinChange(3.21)
// generateCoinChange(1.40)
// generateCoinChange(20.40)

// function generateCoinChange(input) {
//     console.log(`Money Recieved: $${input}`);
//     var change = {"Quarters":0,"Dimes":0,"Nickels":0,"Pennies":0};
//     var money = Math.round(input * 100);
//     console.log(input, centsStarting);
    
//     change["Quarters"] = Math.floor(centsStarting/25)
//     remainder = centsStarting%25;
    
//     change["Dimes"] = Math.floor(remainder/10);
//     remainder = remainder%10;
    
//     change["Nickels"] = Math.floor(remainder/5);
//     remainder = remainder%5;
    
//     change["Pennies"] = remainder;
    
//     for (const key in change) {
//         console.log(`${key}: ${change[key]}`);
//     }
//     // console.log(change);
//     return change
// }

// generateCoinChange(3.21)
// generateCoinChange(1.40)
// generateCoinChange(20.40)