# dnd_map_gen_wfc_AI/Logic/PatternLogic.py

> Language: python | Size: 2656 bytes

## Model qwen3:8b

### 1. **Purpose Summary**  
The `PatternLogic` class is designed to generate and analyze patterns for use in a **Wave Function Collapse (WFC)** algorithm. Its primary purpose is to:  
- **Extract all possible rotations** of N×N pixel blocks from a grid.  
- **Calculate probability weights** for each unique pattern (including its rotations) to guide the WFC algorithm's stochastic generation of consistent, tileable maps.  
- **Convert raw pixel data** into reusable `Pattern` objects with associated weights and probabilities.  

This logic is critical for ensuring that generated maps maintain structural coherence while allowing for rotational variations of patterns.

---

### 2. **Key Functions/Classes and Collaboration**  
**Key Components:**  
- **`get_all_rotations(pixelMatrix)`**:  
  - **Purpose**: Generate all 4 rotations (0°, 90°, 180°, 270°) of a given N×N pixel matrix.  
  - **Collaboration**: Used by `calculate_patterns_weights_probability` to handle rotational symmetry in pattern analysis.  

- **`calculate_patterns_weights_probability(N, input_size, pixels)`**:  
  - **Purpose**:  
    1. Extract all N×N pixel blocks from the input grid.  
    2. Generate their rotations and count occurrences (weights).  
    3. Compute probabilities for each unique pattern.  
    4. Convert raw pixel data into `Pattern` objects with weights/probabilities.  
  - **Collaboration**: Relies on `get_all_rotations` to handle rotations and uses the `Pattern` class to encapsulate patterns for WFC.  

**Collaboration Flow**:  
- `calculate_patterns_weights_probability` processes the input grid, uses `get_all_rotations` to generate rotations, and aggregates statistics.  
- The resulting `Pattern` objects are used by the WFC algorithm to enforce consistency across the generated map.  

---

### 3. **External Dependencies or APIs Used**  
- **`matplotlib.pyplot`**:  
  - **Usage**: Not directly used in the provided code, but imported. Likely for visualization of patterns or debugging.  
- **`math`**:  
  - **Usage**: For mathematical operations (e.g., rotations, size calculations).  
- **`Pattern` class (from `Logic.Pattern`)**:  
  - **Purpose**: Represents a pattern with its rotations, weights, and probabilities.  
  - **Collaboration**: The `calculate_patterns_weights_probability` method converts raw pixel data into `Pattern` objects.  

---

### 4. **Extension Ideas, Pitfalls, or TODOs**  
**Extension Ideas**:  
- **Add Flipping Symmetry**: Support horizontal/vertical flips in addition to rotations for more pattern variations.  
- **Optimize for Large Grids**: Implement spatial partitioning or parallel processing to handle large input sizes efficiently.  
- **Integrate with WFC Algorithm**: Directly tie the `Pattern` objects to WFC's propagation logic for real-time constraint enforcement.  

**Pitfalls**:  
- **Memory Usage**: Storing all unique patterns (especially for large grids) could consume significant memory. Consider pruning rare patterns.  
- **Rotation Overlap**: Ensure that rotations are uniquely identified to avoid double-counting patterns.  
- **Edge Cases**: Handle non-square grids or irregular input sizes gracefully.  

**TODOs**:  
- **Implement Flipping Logic**: Extend `get_all_rotations` to include horizontal/vertical flips.  
- **Add Visualization**: Use `matplotlib` to plot patterns and their probabilities for debugging.  
- **Refactor for Efficiency**: Replace nested loops with vectorized operations or NumPy for faster processing.  

--- 

This code forms the foundation for generating rotationally consistent patterns in a WFC-based procedural map generator, balancing flexibility and structural integrity.

## Detected Imports

- import matplotlib.pyplot as plt
- import math
- from Logic.Pattern import Pattern
