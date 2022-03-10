// isPalindrome(str) -> input is a single string (str). function returns true if
// the input is a palindrome and false otherwise.
// a palindrome is a word or phrase that is the same forwards or backwards
// for this example, capitalization and other punctuation matter
// "racecar" is a palindrome
// "tacocat"
// "raCecar" is not (a capital C is not the same as a lowercase c)
// "raceCar"
// "race car" is not (the space doesn't match up with the E on the opposite side)
// "rac ecar"

function isPalindrome(str) {
    for(var i = 0; i < str.length/2; i++){
        if(str[i] != str[str.length-1-i]){
            return false;
        }
    }
    return true;
}


// console.log(isPalindrome("racecar")); // return true
// console.log(isPalindrome("raceecar")); // return true
// console.log(isPalindrome("raceeeeeeeeeeeeecar")); // return true
// console.log(isPalindrome("tacocat")); // return true
// console.log(isPalindrome("race car")); // return false
// console.log(isPalindrome("e racecar e")); // return true
// console.log(isPalindrome("")); // return true
// console.log(isPalindrome("a")); // return true
// console.log(isPalindrome("123454321")); // return true
// console.log(isPalindrome("1234 4321")); // return true
// console.log(isPalindrome("znmz")); // return false

// longestPalindrome(str) -> input is a string
// output is the longest palindrome contained within that string
// if you find multiple palindromes of the same length, return the first one
// that you find
// "ehjgkkgeh" -> "gkkg"
// "ehjg kkgeh" -> "kk"
// "qwertttreqwerewy" -> "ertttre"
// "qwerttttttreqwerewy" -> "erttttttre"
// "abacabd" -> "bacab"
// "abacaed" -> "aba"
// "abcde" -> "a" (every character is effectively its own palindrome) or maybe "e"
// "a" -> "a" (lol)
// "I like to drive the racecar extremely fast" -> "e racecar e"
// "racecar" -> "racecar" (no need to use the previous function if you don't want to)

function longestPalindrome(str) {
    var longestPal = "";
    longestPal += str[0]
    for(var start = 0; start < str.length; start++){
        for(var end = str.length-1; end >= start; end--){
            if(str[start]===str[end]){
                var slice = str.slice(start, end+1); //creating the new string through a slice
                var pal = isPalindrome(slice); // creating a boolean variable from the return of isPal
                if(pal && slice.length > longestPal.length){ //if bool is True and pal is longer than currently held
                    longestPal = slice; // replace with new slice
                }
            }
        }   
    }
    return longestPal
}

// function longestPalindrome(str) {
//     var longestPal = "";
//     for(var i = 0; i < str.length; i++){

//     }
// }

console.log(longestPalindrome("I like to drive the racecar extremely fast")) //"e racecar e"
console.log(longestPalindrome("I like to drive the raceecar extremely fast")) //"e raceecar e"
console.log(longestPalindrome("I like to drive the raceeecar extremely fast")) //"e raceeecar e"
console.log(longestPalindrome("ehjg kkgeh"));// -> "kk"
console.log(longestPalindrome("qwertttreqwerewy"));// -> "ertttre"
console.log(longestPalindrome("ehjgkkgeh"));// -> "gkkg"
console.log(longestPalindrome("qwerttttttreqwerewy"));// -> "erttttttre"
console.log(longestPalindrome("abacabd"));// -> "bacab"
console.log(longestPalindrome("abacaed"));// -> "aba"
console.log(longestPalindrome("abcde"));// -> "a" (every character is effectively its own palindrome) or maybe "e"
console.log(longestPalindrome("a"));// -> "a" (lol)
console.log(longestPalindrome("racecar"));// -> "racecar"



// Instructor Ryan M code example

function longestPalindrome(input) {
    if (input.length == 0) {
        return "";
    }

    // if input length is 1
    if (input.length == 1) {
        return input;
    }

    let result = input[0]; //just in case we find nothing but a single,
    // character, like an input of "abcdefghijklmnop"

    for (var i = 0; i < input.length; i++) {
        var left = 0;
        var right = 0;
        //determine if we have a string of idential characters in the middle
        //i.e. a trivial palindrome, such as: "tttttt"
        // in the string "qwerttttttreqwerewy"
        while (input[i + 1 + right] == input[i]) {
            right++;
        }


        //now check for non-trivial palindromes
        while (input[i - 1 - left] == input[i + 1 + right]) {
            if (input[i - 1 - left] === undefined && input[i + 1 + right] === undefined) {
                //special case here - if the next character to the left and to the
                // right are undefined, we have the entire string -
                // the entire string is a palindrome! we can just return the input
                return input;
            }
            left++;
            right++;
        }
        //we have a potential longest palindrome -
        //check it against the current longest
        potential = input.slice(i - left, i + right + 1);
        console.log(potential);
        if (potential.length > result.length) {
            result = potential;
        }
    }

    return result;
}

console.log(longestPalindrome("I like aca to drive tt e the raceeeeecar extremely faaast eeeeeeeeeeeeeeeeeeeeeeee")) //"e racecar e"