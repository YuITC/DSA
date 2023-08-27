### 1. Definition
- An <b>Array</b> is a linear data structure that stores data in contiguous locations in RAM.
- Advantages:
    - Instantly read any value of array using indexes.
- Disadvantages:
    - A <b>Static Array</b> has a fixed size.
      - A <b>Dynamic Array</b> solved this issue by allocating a new space that have the size double from the old array.

### 2. Operation time
| Operation         | Big-O Time |
|-------------------|:----------:|
| r/w i-th element  | O(1)       |
| insert/remove end | O(1)       |
| insert middle     | O(n)       |
| remove middle     | O(n)       |
