class Tree {
  constructor(root) {
    this.root = root;
  }
  bfs = value => {
    const queue = [this.root];
    while (queue) {
      const current = queue.shift();
      if (current.value === value) return true;
      if (current.left) queue.push(current.left);
      if (current.right) queue.push(current.right);
    }
    return false;
  };

  dfs = value => {
    const stack = [];
    stack.push(this.root);
    while (stack) {
      const current = stack.pop();
      if (current.value === value) return current;
      if (current.left) stack.push(current.left);
      if (current.right) stack.push(current.right);
    }
    return false;
  };
}

class Node {
  constructor(value, left = null, right = null) {
    this.value = value;
    this.left = left;
    this.right = right;
  }
}
