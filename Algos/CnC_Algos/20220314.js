// Sum Arrays Easy Peasy Lemon Squeezy 

// Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.

// Examples
// Input: [1, 5.2, 4, 0, -1]
// Output: 9.2

// Input: []
// Output:0

// Input: [-2.398]
// Output: -2.398

// Assumptions
// - You can assume that you are only given numbers.
// - You cannot assume the size of the array.
// - You can assume that you do get an array and if the array is empty, return 0.

// What We're Testing
// We're testing basic loops and math operations. This is for beginners who are just learning loops and math operations.
// Advanced users may find this extremely easy and can easily write this in one line.

function sumArray(arr) {
    if(arr.length === 0){return 0}
    else if(arr.length === 1){return arr[0]}
    else{
        var sum = 0
        for (const value of arr) {sum += value}
        return sum
    }
}

console.log(sumArray([1, 5.2, 4, 0, -1]))
console.log(sumArray([]))
console.log(sumArray([-2.398]))
