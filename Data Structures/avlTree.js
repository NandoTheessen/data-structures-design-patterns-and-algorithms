class Tree {
  constructor() {
    this.root = null;
  }
  add(value) {
    if (!this.root) {
      this.root = new Node(value);
    } else {
      this.root.add(value);
    }
  }
  toJSON() {
    return JSON.stringify(this.root.serialize(), null, 4);
  }
  toObject() {
    return this.root.serialize();
  }
}

class Node {
  constructor(value = null, left = null, right = null) {
    this.left = left;
    this.right = right;
    this.value = value;
    this.height = 1;
  }
  add(value) {
    if (value < this.value) {
      // go left
      // if left, recursively call add on left node
      if (this.left) {
        this.left.add(value);
        // if not left, create left node
      } else {
        this.left = new Node(value);
      }
      // if no right or right height is smaller than left height
      // set height to left height + 1 (adds up this + child node)
      if (!this.right || this.right.height < this.left.height) {
        this.height = this.left.height + 1;
      }
    } else {
      // go right
      // if right, recursively call add on right node
      if (this.right) {
        this.right.add(value);
        // if not right, create right node
      } else {
        this.right = new Node(value);
      }
      // adapt height, counting this + childs height
      if (!this.left || this.right.height > this.left.height) {
        this.height = this.right.height + 1;
      }
    }
    // after adding the new node && correcting the height on all affected notes
    // balance the tree
    this.balance();
  }
  balance() {
    // take out heights if existing
    const rightHeight = this.right ? this.right.height : 0;
    const leftHeight = this.left ? this.left.height : 0;

    if (leftHeight > rightHeight + 1) {
      const leftRightHeight = this.left.right ? this.left.right.height : 0;
      const leftLeftHeight = this.left.left ? this.left.left.height : 0;

      // if leftheight is bigger than right height
      // check if a double rotation is needed

      if (leftRightHeight > leftLeftHeight) {
        this.left.rotateRR();
      }
      // if left > right, rotate left
      this.rotateLL();
    } else if (rightHeight > leftHeight + 1) {
      const rightRightHeight = this.right.right ? this.right.right.height : 0;
      const rightLeftHeight = this.right.left ? this.right.left.height : 0;

      // check if double rotation is needed!
      if (rightLeftHeight > rightRightHeight) {
        this.right.rotateLL();
      }
      // right > left, rotate right!
      this.rotateRR();
    }
  }
  rotateRR() {
    // rotate right
    // save value
    const valueBefore = this.value;
    // save left node
    const leftBefore = this.left;
    // swap root & right value
    this.value = this.right.value;
    // swap left & right node
    this.left = this.right;
    // swap next bigger node to the right node
    this.right = this.right.right;
    // swap next smaller leaf node to left left
    this.left.right = this.left.left;
    // Add back the old left
    this.left.left = leftBefore;
    // re-assign the old value
    this.left.value = valueBefore;
    // re-adjust height of left node
    this.left.updateInNewLocation();
    // re-adjust height of this node
    this.updateInNewLocation();
  }
  rotateLL() {
    const valueBefore = this.value;
    const rightBefore = this.right;
    this.value = this.left.value;
    this.right = this.left;
    this.left = this.left.left;
    this.right.left = this.right.right;
    this.right.right = rightBefore;
    this.right.value = valueBefore;
    this.right.updateInNewLocation();
    this.updateInNewLocation();
  }
  updateInNewLocation() {
    // set height to 1 if neither child exists
    if (!this.right && !this.left) {
      this.height = 1;
      // chose the bigger height out of both left and right child
    } else if (
      !this.right ||
      (this.left && this.right.height < this.left.height)
    ) {
      this.height = this.left.height + 1;
    } else {
      //if (!this.left || this.right.height > this.left.height)
      this.height = this.right.height + 1;
    }
  }
  serialize() {
    const ans = { value: this.value };
    ans.left = this.left === null ? null : this.left.serialize();
    ans.right = this.right === null ? null : this.right.serialize();
    ans.height = this.height;
    return ans;
  }
}
