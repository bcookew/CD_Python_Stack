// Write a function that, given a sorted array and a value, determines whether the value is found within the array through 
// recursively searching, and returns the index. Binary Search works by checking whether the value given is greater than or 
// less than a midway point, which is why the given array must be sorted. 
// Also, even though there's only an array and value given, you can add additional parameters to your function.
// Return -1 if the number is not in the array


// val = 9
// arr = [1,2,3,5,7,9,10 ,11,13,14,15,56,78]

// [1,2,3,5,7,9,10      |        11,13,14,15,56,78] <----- 9 is less than halfway so now you can search the left side only
// [1,2,3,5,       |        7,9,10] <------  9 is greater than halfway so you can search the right side only
// [7,      |       9,10] <------ depending on where you split,9 is greater than halfway
// [9,     |      10] <------ whittle down to 1 or 2 items to check and solve!

// Our function did not return the required result. It worked for true/false but not for returning the correct index number.
function recursive_binary_search(arr, num, counter=Math.trunc(arr.length/2)) {
    console.log(arr);        
    if(arr.length === 1 && arr[0] != num){
        console.log("line 19");
        return -1
    }

    midpoint = Math.trunc(arr.length/2)
    
    if(arr[midpoint] === num){
        console.log("Line 26", counter);
        return midpoint
    }

    else if(arr[midpoint] > num){
        console.log("Line 30");
        counter -= midpoint
        return recursive_binary_search(arr.slice(0,midpoint),num, counter)
    }

    else if(arr[midpoint] < num){
        console.log("Line 34");
        counter += midpoint
        return recursive_binary_search(arr.slice(midpoint,arr.length),num, counter)
    }
}

let val = 9
let arr = [1,2,3,5,7,9,10,11,13,14,15,56,78]
//         0 1 2 3 4 5  6  7  8  9 10 11 12
// console.log(recursive_binary_search(arr,val))

function binarySearch(array, value, index=0, is_greater=0){
    if(is_greater == 0){
        var index = Math.floor(array.length/2)
    }
    if(is_greater == 1){
        index = Math.floor((index/2)+(index))
    }
    if(is_greater == 2){
        index = Math.floor(index/2)
    }
    
    if(index == 0 && array[index] > value){
        return false
    }
    if(index == array.length-1 && array[index] < value){
        return false
    }
    
    if(array[index] == value){
        return index
    }
    
    if(array[index] < value){
        return binarySearch(array, value, index, 1)
    }
    if(array[index] > value){
        return binarySearch(array, value, index, 2)
    }

}

console.log(binarySearch(arr, val))