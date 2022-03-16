// construct a Singly Linked List Class

class Node {
    constructor(value){ //def __init__()
        this.value = value
        this.next = null
    }
}
class SLList{
    constructor(){
        this.head = null //On creation of empty list we set .head to null
        return this
    }
    
    addToFront(value) {
        if(this.head === null) this.head = new Node(value) // sets head to a new node if no head node
        else{
            let newNode = new Node(value)
            newNode.next = this.head
            this.head = newNode
        }
        return this
    }
    
    addToBack(value) {
        let currentNode = this.head
        while(currentNode.next != null){
            currentNode = currentNode.next;
        }
        currentNode.next = new Node(value);
        return this
    }

    removeFromFront(){
        let oldHead = this.head
        this.head = this.head.next
        oldHead.next = null
        return this
    }

    removeFromBack(){
        let currentNode = this.head
        if(this.head.next === null){
            this.head = null
        }

        let prevNode = null
        while(currentNode.next != null){
            prevNode = currentNode
            currentNode = currentNode.next;
        }
        
        prevNode.next = null
        return this
    }
    
    contains(value){
        let currentNode = this.head
        while(currentNode != null){
            if(currentNode.value === value) return true
            currentNode = currentNode.next
        }
        return false
    }
    
// find the location of the lowest value in the list, and move that value to the front
    moveMinToFront(){
        if(this.head == null || this.head.next == null){
            return this
        }
        let currentNode = this.head
        let beforeSmallest = null
        let curSmallest = this.head
        let afterSmallest = this.head.next

        while(currentNode.next != null){
            if(curSmallest.value > currentNode.next.value){
                beforeSmallest = currentNode
                curSmallest = currentNode.next
                afterSmallest = currentNode.next.next
            }
            currentNode = currentNode.next;
        }

        if(curSmallest == this.head){
            console.log("Already the head!");
            return this;
        }    
        beforeSmallest.next = afterSmallest;
        curSmallest.next = this.head
        this.head = curSmallest
        return this;
        }
// find the location of the highest value in the list, and move that value to the back
    moveMaxToBack(){
        if(this.head == null || this.head.next == null){
            return this
        }
        let currentNode = this.head
        let beforeBiggest = null
        let curBiggest = this.head
        let afterBiggest = this.head.next

        while(currentNode.next != null){
            if(curBiggest.value < currentNode.next.value){
                beforeBiggest = currentNode
                curBiggest = currentNode.next
                afterBiggest = currentNode.next.next
            }
            currentNode = currentNode.next;
        }
        if(curBiggest === currentNode) {
            console.log("Already at the end");
            return this
        }
        if(afterBiggest) beforeBiggest.next = afterBiggest;
        currentNode.next = curBiggest
        curBiggest.next = null
        return this;
    }

    insertMiddle(value){
        let currentNode = this.head
        let counter = 1
        let temp = null
        while(currentNode.next != null){
            currentNode = currentNode.next
            counter ++
        }
        counter = Math.trunc(counter / 2)
        currentNode = this.head
        while(counter > 1){
            currentNode = currentNode.next
            counter--
        }        
        temp = currentNode.next
        currentNode.next = new Node(value)
        newNode.next = temp

        return this
        
    }

    printList(){
        let currentNode = this.head
        let str = ""
        while(currentNode != null){
            str += `${currentNode.value} -> `
            currentNode = currentNode.next
        }
        console.log(str);
        return this
    }

    nodesToList(){
        let newArr = [];
        let currentNode = this.head;
        while(currentNode != null){
            newArr.push(currentNode.value)
            currentNode = currentNode.next
        }
        console.log(newArr);
        return this
    }
    
    print(){
        let result = "";
        let runner = this.head;
        while(runner != null){
            result += `👉 ${runner.value} ⇶ `; 
            runner = runner.next;
        }
        console.log(result.slice(0, result.length - 3));
    }
}

sF = new SLList().addToFront(10).addToFront(9).addToFront(8).addToFront(7).addToFront(6).addToFront(5)
lF = new SLList().addToFront(5).addToFront(6).addToFront(7).addToFront(8).addToFront(9).addToFront(10)
mL = new SLList().addToFront(2).addToFront(5).addToFront(7).addToFront(7).addToFront(9).addToFront(6)

console.log("=".repeat(60),"\n\n" + "=".repeat(60))

sF.print()
sF.moveMinToFront()
sF.moveMaxToBack()
sF.print()

console.log("=".repeat(60),"\n\n" + "=".repeat(60))

lF.print()
lF.moveMinToFront()
lF.moveMaxToBack()
lF.print()

console.log("=".repeat(60),"\n\n" + "=".repeat(60))

mL.print()
mL.moveMinToFront()
mL.moveMaxToBack()
mL.print()

console.log("=".repeat(60),"\n\n" + "=".repeat(60))
