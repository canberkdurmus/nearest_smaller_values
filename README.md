# Nearest Smaller Values
Advanced Data Structures Project: A Python implementation to use cartesian trees to solve all nearest smaller values problem

Detailed description for the problem can be found here: J. Shun and G. E. Blelloch, "A simple parallel cartesian tree algorithm and its application to parallel suffix tree construction", ACM Transactions on Parallel Computing (TOPC), 2014.

Input data is in the data.txt file and seperated by ' ,' (one whitespace and a comma)

Input Example (data.txt):
```
0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15
```

Execution:
```
python3 main.py
```

Output Example:
```
Array:  [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
Nearest Left Smaller Values:  - 0 0 4 0 2 2 6 0 1 1 5 1 3 3 7 
Nearest Right Smaller Values: - 4 2 2 1 6 1 1 - 5 3 3 - 7 - - 
```
