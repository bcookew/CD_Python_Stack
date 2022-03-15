// ####################################################
// ALGO CHALLENGE DAY #12 @everyone 
// 👇🏻 
// #A Needle in the Haystack
// Can you find the needle in the haystack?

// Write a function findNeedle() that takes an array full of junk but containing one "needle"
// After your function finds the needle it should return a message (as a string) that says:
// "found the needle at position " plus the index it found the needle, so:

// find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk'])
// should return "found the needle at position 5" (in COBOL "found the needle at position 6")



function find_needle(arr) {
    if(arr.length === 0) return "Hey! I can't search an empty array!"
    for(let i = 0; i < arr.length; i++){
        if(arr[i] === "needle")
        return `Found the needle at position ${i}!`
    }
    return 'Needle not found!'
}
console.log(find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk']))
console.log(find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'randomJunk']))
console.log(find_needle([]))
