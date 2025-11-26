# dnd_map_gen_wfc_AI/Logic/PatternLogic.py

> Language: python | Size: 2656 bytes

## Model qwen3:8b

### 1. **Purpose Summary**  
The `PatternLogic` class in `PatternLogic.py` is designed to generate and analyze **rotational patterns** for use in a **Walkable Finite State (WFC)** algorithm. Its primary purpose is to:  
- Extract all unique **N×N pixel patterns** from a given matrix, including their **rotational variants** (90°, 180°, 270°).  
- Calculate **weight probabilities** for each unique pattern to guide the WFC algorithm's stochastic generation of maps.  
- Convert raw pattern data into reusable `Pattern` objects for further processing.  

---

### 2. **Key Functions/Classes and Collaboration**  
**Key Components:**  
- **`Pattern` class** (from `Logic.Pattern`): Represents a unique pattern with its rotations and probabilities.  
- **`PatternLogic` class**: Central logic for pattern extraction and analysis.  

**Key Functions:**  
- **`get_all_rotations(pixelMatrix)`**:  
  - Generates all 4 rotational variants of a square matrix (0°, 90°, 180°, 270°).  
  - Returns tuples of rotated matrices for comparison.  

- **`calculate_patterns_weights_propability(N, input_size, pixels)`**:  
  - Iterates over the input matrix to extract **N×N sub-patterns**.  
  - For each pattern, computes its **rotational variants** and counts their occurrences.  
  - Calculates **weights** (frequency) and **probabilities** for each unique pattern.  
  - Converts raw patterns into `Pattern` objects for downstream use.  

**Collaboration Flow:**  
1. `get_all_rotations` generates rotational variants of a pattern.  
2. `calculate_patterns_weights_propability` uses these rotations to count occurrences and compute probabilities.  
3. Results are stored as `Pattern` objects, which are likely used in the WFC algorithm to guide tile placement.  

---

### 3. **External Dependencies or APIs Used**  
- **`matplotlib.pyplot`**: Not directly used in the provided code, but imported. May be for future visualization of patterns.  
- **`math`**: Used for mathematical operations (e.g., rotations, matrix manipulations).  
- **`Pattern` class** (from `Logic.Pattern`): Stores pattern data (rotations, weights, probabilities) for reuse.  

---

### 4. **Extension Ideas, Pitfalls, or TODOs**  
**Extension Ideas:**  
- **Add flipping symmetry** (horizontal/vertical flips) to account for more pattern variations.  
- **Optimize memory usage**: Current code stores all patterns as tuples, which may be inefficient for large matrices. Consider using hashable structures or compression.  
- **Support non-square matrices**: The current rotation logic assumes square matrices. Extend to handle rectangular inputs.  
- **Integrate with WFC algorithm**: Use the generated patterns and probabilities to implement the WFC tile generation logic.  

**Pitfalls:**  
- **Rotation logic errors**: The current rotation code may have edge cases (e.g., empty matrices, non-square inputs) that need validation.  
- **Performance issues**: For large input sizes, the nested loops and duplicate-checking may be slow. Consider using sets or hash maps for faster deduplication.  
- **Probability normalization**: Ensure the probability calculation handles edge cases (e.g., zero-weight patterns).  

**TODOs:**  
- Implement the actual WFC algorithm using the generated patterns.  
- Add visualization with `matplotlib` to display patterns and their probabilities.  
- Validate rotation logic for edge cases (e.g., 1×1 matrices, empty inputs).  
- Optimize the `patterns_without_duplicates` step using more efficient data structures (e.g., `set`).

## Detected Imports

- import matplotlib.pyplot as plt
- import math
- from Logic.Pattern import Pattern
