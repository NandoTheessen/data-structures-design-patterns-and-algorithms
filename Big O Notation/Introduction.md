# Big O

## Time Complexity:

#### Big O, Big Theta and Big Omega

**Big O**:

- describes the increase in time complexity compared to the input
- worst case time complexity
- describes the upper bound for runtime

**Big Omega**:

- best case time complexity
- describes the lower bound for runtime

**Big theta**:

- gives the expected runtime
- describes the tigh bound for runtime

In the industry big O tends to be used like big theta.

## Space Complexity

- Space complexity matters to an algorithm just as much as time does
- parellel concept to time complexity
  - f.e. an array w/ _n_ elements needs _n_ memory
  - even stack space for recursive calls counts
    - this only counts for recursive calls, as resolved function calls are no
      longer on the call stack!

example for O(n) space _and_ time complexity:

```javascript
function sum(n) {
  if (n <= 0) return 0;
  return n + sum(n - 1);
}
```

To traverse the whole range of n, _n_ in time and space complexity is needed
