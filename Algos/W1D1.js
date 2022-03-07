// Acronym
function acronym(str1) {
    var newStr = "";
    for(var i = 0; i < str1.length; i++){
        if(i === 0){
            newStr += str1[i].toUpperCase();
        }
        if(str1[i-1] === " " && i > 0){
            newStr += str1[i].toUpperCase() //Check if correct method
        }
    }
    return newStr;
}


console.log(acronym("orange juice is better than milk"));
console.log(acronym("there's no free lunch - gotta pay yer way"));

// Reverse String

function revStr(strOld, space) {
    var newStr = "";
    for (var i = strOld.length-1; i >= 0; i--) {
        if(space){
            newStr += strOld[i];
        }    
        else{
            if(strOld[i] != " "){
                newStr += strOld[i];
            }
        }
    }
    return newStr;
}

console.log(revStr("Orange juice is better than milk", true));
console.log(revStr("Orange juice is better than milk", false));
console.log(revStr("creatures of the night", true));
console.log(revStr("creatures of the night", false));