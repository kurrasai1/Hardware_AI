# Challenge #17: Sorting on a Systolic Array

**Author:** MEGHA SAI SUMANTH KURRA  
**Course:** ECE 410/510 Spring 2025  
**Instructor:** Prof. Christof Teuscher

## 🎯 Objective
Implement bubble sort using a 1D systolic array model and analyze performance over increasing problem sizes.

## 💡 Approach
- Each processing element (PE) holds one value
- Adjacent PEs compare and exchange values to perform bubble sort
- N elements → N PEs, N-1 iterations

## 📊 Visualization
The benchmark plots execution time vs array size using matplotlib.

## 🚀 How to Run
```bash
python systolic_sort.py
