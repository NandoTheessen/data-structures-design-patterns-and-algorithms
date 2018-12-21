class Tree {
  constructor(root) {
    this.root = root;
  }
  bfs(value) {
    const queue = [this.root];
    while (queue) {
      const current = queue.shift();
      if (current.value === value) return true;
      if (current.left) queue.push(current.left);
      if (current.right) queue.push(current.right);
    }
    return false;
  }

  dfs(value) {
    const stack = [this.root];

    while (stack) {
      const current = stack.pop();
      if (current.value === value) return current;
      if (value >= current.value && current.right) {
        stack.push(current.right);
      } else if (value < current.value && current.left) {
        stack.push(current.left);
      }
    }
    return false;
  }

  insert(node) {
    let current = this.root;
    while (current) {
      if (node.value >= current.value) {
        if (!current.right) {
          current.right = node;
          return;
        } else {
          current = current.right;
        }
      } else {
        if (!current.left) {
          current.left = node;
          return;
        } else {
          current = current.left;
        }
      }
    }
  }
}

class Node {
  constructor(value, left = null, right = null) {
    this.value = value;
    this.left = left;
    this.right = right;
  }
}

const bst = new Tree(new Node(1));
bst.insert(new Node(2));
bst.insert(new Node(0));
bst.insert(new Node(3));
bst.insert(new Node(4));

console.log(bst.dfs(3));
