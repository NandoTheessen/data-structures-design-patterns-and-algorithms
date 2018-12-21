# Amortized Time

- Concept of the relation between worst case of an action and the
  likelyhood of it happening
  - example automatically resizing an array to 2N once it is filled
    - takes O(1) for insertion unless array is full, then takes O(n)
    - for arrays the amortized time for insertion still is O(1)
