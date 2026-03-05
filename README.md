# A2SV - Algorithm & Data Structure Solutions

A curated collection of algorithm and data structure problem solutions in Python (and some C++), organized by topic. Problems are sourced from LeetCode, HackerRank, and other competitive programming platforms.

## Topics Covered

| Topic | Description |
|---|---|
| [Sorting](./Sorting/) | Classic sorting algorithms + LeetCode problems |
| [Searching](./Searching/) | Linear, binary, interpolation, and hashing |
| [Linked List](./LinkedList/) | Traversal, reversal, merging, and manipulation |
| [Stack](./Stack/) | Stack-based problems and implementations |
| [Monotonic Stack](./MonotonicStack/) | Next greater element, car fleet, temperature problems |
| [Two Pointer](./TwoPointer/) | Two-sum variants, palindrome, sliding window |
| [Window Sliding](./WindowSliding/) | Subarray sums, max subarray, trapping rain water |
| [Prefix Sum](./PrefixSum/) | Range queries, subarray sums, matrix block sums |
| [Recursion](./Recursion/) | Fibonacci, power, Tower of Hanoi, game theory |
| [Math](./Math/) | FizzBuzz, Domino, grading utilities |

---

## Sorting Algorithms Reference

### Stability

| Algorithm | Stable |
|---|---|
| Bubble Sort | Yes |
| Insertion Sort | Yes |
| Merge Sort | Yes |
| Selection Sort | No |
| Heap Sort | No |
| Quick Sort | No |

### In-Place vs. Not In-Place

| Algorithm | In-Place |
|---|---|
| Bubble Sort | Yes |
| Insertion Sort | Yes |
| Selection Sort | Yes |
| Heap Sort | Yes |
| Merge Sort | No |
| Quick Sort | No |

---

## Searching Algorithms Reference

| Algorithm | Time Complexity | Notes |
|---|---|---|
| Linear Search | O(n) | Works on unsorted data |
| Ordered Linear | O(n) | Early exit on sorted data |
| Binary Search | O(log n) | Requires sorted data |
| Interpolation | O(log log n) avg | Best for uniformly distributed data |
| Hashing | O(1) avg | Hash map based lookup |

---

## Repository Structure

```
A2SV/
    Sorting/          # Sorting algorithms and problems
    Searching/        # Searching algorithms
    LinkedList/       # Linked list problems
    Stack/            # Stack-based problems
    MonotonicStack/   # Monotonic stack problems
    TwoPointer/       # Two pointer technique
    WindowSliding/    # Sliding window technique
    PrefixSum/        # Prefix sum technique
    Recursion/        # Recursive problem solving
    Math/             # Math-based problems
    hashing.py        # Standalone hashing demo
```

---

## Languages Used

**Python 3** primary language for all solutions
**C++** used in select Two Pointer problems (`houseRobber.cpp`, `minWindowSubstring.cpp`)
