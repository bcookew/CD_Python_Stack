function parensValid(strIn) {
    var opening = 0
    var closing = 0
    for(char of strIn){
        if(char === "("){
            opening += 1;
        }
        else {
            closing += 1
        }
    }
    if(opening === closing){
        return true;
    }
    else{
        return false;
    }
}

console.log(parensValid("(())()()(((())))")); 



function parenCheck(str) {
    let newArr = [];
    for (let i=0;i<str.length;i++) {
        switch (str[i]) {
            case '(':
                newArr.push(str[i]);
                break;
            case ')':
                if (newArr[newArr.length - 1] === '(') {
                    newArr.pop();
                    break;
                } else {
                    newArr.push(str[i]);
                    break;
                }
        }
    }
    if (newArr.length != 0) {
        return false;
    } else {
        return true;
    }
}

console.log(parenCheck("(())()()(((())))")); 