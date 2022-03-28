class Node{
    constructor(value){
        this.value = value
        this.next = null
    }
}

// a queue operates on the principal of "First In, First Out" like waiting in line for something
class SLQueue{
    constructor() {
        this.head = null
        this.tail = null
        return this
    }


    // add a node with the given value to the queue
    // similar to SLL - add to back
    enqueue(value) {
        var newNode = new Node(value)
    
        if (this.head == null) {
            this.head = newNode
            return this
        }
    
        var runner = this.head
    
        while (runner.next != null) {
            runner = runner.next
        }
        runner.next = newNode
        return this
    }

    // remove and return the front value from the queue
    // similar to SLL - remove from front
    dequeue() {
        if (this.head == null) {
            return this
        }
        let temp = this.head; 
        this.head = this.head.next; 
        temp.next = null; 
        return temp.value
    }    

    //return true/false based on whether you find the given value in a queue
    // same as contains in SLL
    contains(value) {
        var contains = false; 
        if (this.head == null) {
            return false;
        }  
        var runner = this.head;     
        while (runner != null){
            if (runner.value == value) {
                contains = true;
                break
            }
            runner = runner.next; 
        }
        if (contains == true) {
            return true;
        }
        else {
            return false;
        }
    }

    // remove the minimum value in the queue (remember your edgecases and pointers!)
    removeMin() {
        if (this.head == null) {
            return this
        }
        let runner = this.head
        let temp = runner.value
        while (runner.next != null) {
            if (temp > runner.next.value) {
                temp = runner.next.value
            }
            runner = runner.next
        }
        runner = this.head
        while (runner.next.value != temp) {
            runner = runner.next
        }
        let temp2 = runner.next
        temp2 = null
        runner.next = runner.next.next
        return this
    }

    displayQueue() {
        let result = "head ";
        let runner = this.head;
        while(runner != null){
            result += `👉 ${runner.value} `;
            runner = runner.next;
        }
        result += "tail"
        console.log(result)
        return this
    }
}

