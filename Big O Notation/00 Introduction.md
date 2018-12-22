# Big O

## Time Complexity:

#### Big O, Big Theta and Big Omega

**Big O**:

- describes the increase in time complexity compared to the input
  - because of this, constants are dropped!
  - non-dominant terms are dropped as well
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

#### When to add or mulitply runtimes:

Suppose a two step algorithm, when do we multiply / add the runtimes??

- When doing consecutive work we add (f.e. 2 for loops that run after each other)

- When doing parallel work, we multiply (f.e. nested for loops iterating over 2 diff arrays)

## More complicated examples:

- Suppose an algorithm that takes in an array of strings, sorts the strings & then sorts the array.

  - to avoid confusion it's important to work with different variable names!!
  - give s to the longest string (worst case) & a to the length of the array

  - Sort every string work out to be O(a\*s log s), sorting the array takes another a log a

    - catch 22: for sorting an array of strings, we have to compare the strings!!
      - runtime is O(a\*s log a)

  - **this works out to be O(a\*s(log a + log s))**

- **General rules**
  - algorithms with multiple recursive calls have exponential runtime!
    - to an extend of O(branches \*\* depth) where branches are the number of simulteanous recursive calls
      and depth == N
    - For O(2\*\*n) we can use memoization to reach O(n) runtime!
