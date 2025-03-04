# Custom Stack Implementation

## Overview
This repository contains an implementation of a custom stack data structure that supports the following operations in **O(1) time complexity**:
- `push(x)`: Adds an element to the stack.
- `pop()`: Removes the top element from the stack.
- `top()`: Retrieves the top element of the stack without removing it.
- `getMin()`: Returns the minimum element in the stack.
- `getMax()`: Returns the maximum element in the stack.

This implementation is written in **Python** and follows the constraints given in the IEEE-CS enrollments Easy CC Task.

## Author
- **Divyam Agrawal**
- **24BIT0423**

## Implementation Details
The implementation uses three stacks:
- `stack`: Stores all pushed elements.
- `min_stack`: Tracks the minimum element at each stage.
- `max_stack`: Tracks the maximum element at each stage.

### Code Structure
```python
class TheStackOfAllTime:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.max_stack = []
```
- The `min_stack` ensures that `getMin()` always returns the current minimum in **O(1)**.
- The `max_stack` ensures that `getMax()` always returns the current maximum in **O(1)**.

### Example Usage
```python
stack = TheStackOfAllTime()
stack.push(5)
stack.push(2)
stack.push(8)
stack.push(1)
print("Top:", stack.top())  # Output: 1
print("Min:", stack.getMin())  # Output: 1
print("Max:", stack.getMax())  # Output: 8
stack.pop()
print("Min after pop:", stack.getMin())  # Output: 2
print("Max after pop:", stack.getMax())  # Output: 8
print("Top after pop:", stack.top())  # Output: 8
```

## How to Run
1. Clone the repository:
   ```sh
   git clone https://github.com/ludicrouslytrue/custom-stack.git
   ```
2. Navigate to the project directory:
   ```sh
   cd custom-stack
   ```
3. Run the Python file:
   ```sh
   python stack.py
   ```
