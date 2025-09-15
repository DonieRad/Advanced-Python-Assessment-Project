# Advanced-Python-Assessment-Project
This repository contains my solutions for a university **Programming and Algorithms** assessment.   The tasks cover **object-oriented programming, data structures, and algorithms** in Python.

Each task is implemented in a single script (`task1.py … task5.py`) with comments for clarity.

## Tasks Overview

### Task 1 – Student Class
- Defines a `Student` class with attributes for name and scores.
- Includes a method to **evaluate performance** (Excellent / Satisfactory / Needs Improvement) based on average score.  
*Demonstrates class design and conditional logic.*

---

### Task 2 – Inheritance with Appliances
- Base class: `Appliance` (brand, power rating).  
- Subclasses:
  - `Light_bulb` → On/Off state with toggle method (`switch()`), supports `bool()` conversion.  
  - `Fan` → Adjustable speed levels, cycles through with `switch()`.  
*Demonstrates class inheritance, method overriding, and dunder methods.*

---

### Task 3 – Heap Numbers
- Defines a `Heap_numbers` class with:  
  - **Heapify**: Convert a list into a max-heap.  
  - **Heapsort**: Sort values in ascending order.  
  - **Remove method**: Delete numbers greater than `x`.  
- Includes integer validation utility.  
*Demonstrates heaps, sorting algorithms, recursion, and data validation.*

---

### Task 4 – Binary Search Tree & Traversal
- Defines `Node` and `Search_tree` classes.  
- Supports **insertion** (rejects duplicates) and **in-order traversal**.  
- In-order traversal prints `True/False` depending on whether node values are even.  
*Demonstrates tree data structures, recursion, and traversal methods.*

---

### Task 5 – Weighted Graph
- Defines a `Weight_graph` class with:  
  - **Vertices and edges** using adjacency lists.  
  - Method to compute the **average edge weight** from a vertex.  
  - Overloaded `**` operator to raise all edge weights to a power.  
*Demonstrates graph data structures, operator overloading, and weighted edges.*

---

This assessment allowed me to:

Practice object-oriented design (classes, inheritance, operator overloading).
Implement and test fundamental data structures (heap, binary search tree, graph).
Apply algorithms (heapsort, traversal).
Strengthen my ability to write clean, well-documented code.
