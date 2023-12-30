// Linked List Algorithms

// Define a Node class for the linked list
class Node {
    constructor(data) {
      this.data = data;
      this.next = null;
    }
  }
  
  // Define a LinkedList class
  class LinkedList {
    constructor() {
      this.head = null;
    }
  
    // Add a new node at the end of the linked list
    append(data) {
      const newNode = new Node(data);
  
      if (!this.head) {
        this.head = newNode;
      } else {
        let current = this.head;
        while (current.next) {
          current = current.next;
        }
        current.next = newNode;
      }
    }
  
    // Display the linked list
    display() {
      let current = this.head;
      while (current) {
        console.log(current.data);
        current = current.next;
      }
    }
  }
  
  module.exports = LinkedList;

// Array Algorithms

// Reverse an array
function reverseArray(arr) {
    return arr.reverse();
  }
  
  // Find the maximum value in an array
  function findMaxValue(arr) {
    return Math.max(...arr);
  }
  
  // Find the minimum value in an array
  function findMinValue(arr) {
    return Math.min(...arr);
  }
  
  // Calculate the sum of all elements in an array
  function calculateSum(arr) {
    return arr.reduce((sum, current) => sum + current, 0);
  }
  
  module.exports = {
    reverseArray,
    findMaxValue,
    findMinValue,
    calculateSum
  };
  