class Node {
  value;
  rest;

  constructor(value) {
    this.value = value;
    this.rest = null;
  }

  toString() {
    return {
      value: this.value, rest: this.rest ? this.rest.toString() : null
    };
  }
}


class List {
  #head;
  #length

  constructor() {
    this.#head = null;
    this.#length = 0;
  }

  get length() {
    return this.#length;
  }

  prepend(item) {
    const node = new Node(item);
    [node.rest, this.#head] = [this.#head, node];
    this.#length++;
    return this;
  }

  append(item) {
    const node = new Node(item);
    if (this.#head === null) {
      this.#head = node;
    } else {
      let currentNode = this.#head;
      while (currentNode.rest) {
        currentNode = currentNode.rest;
      }
      currentNode.rest = node;
    }
    this.#length++;
    return this;
  }

  at(n) {
    if (n >= this.#length || n < 0) {
      throw new RangeError('Out of Range index');
    }
    let currentNode = this.#head;
    let i = 0;
    while (i < n) {
      i++;
      currentNode = currentNode.rest;
    }
    return currentNode.value;
  }

  static fromArray(arr) {
    const list = new List();
    for (const item of arr) {
      list.append(item);
    }
    return list;
  }

  toArray() {
    const arr = [];
    let currentNode = this.#head;
    arr.push(currentNode.value);
    while (currentNode.rest) {
      currentNode = currentNode.rest;
      arr.push(currentNode.value);
    }
    return arr;
  }

  toString() {
    return JSON.stringify(this.#head.toString(), null, 2);
  }
}


const linkedList = List.fromArray('lexe'.split(''))

console.log(linkedList.toString());

linkedList.append('y').prepend('a');

console.log(linkedList.at(3));

console.log(linkedList.toString());

console.log(linkedList.toArray());
