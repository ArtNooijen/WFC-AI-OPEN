# dnd_map_gen_wfc_AI/Logic/Index.py

> Language: python | Size: 822 bytes

## Model qwen3:8b

### 1. **Purpose Summary**  
The `Index` class in `Index.py` serves as a central manager for defining and validating **pattern transition rules** in a **Walkable Finite State (WFC)** algorithm. It enables the creation of a rulebook that maps how patterns (e.g., tile types in a dungeon map) can transition to other patterns based on relative positions. This is critical for procedural content generation, such as dungeon maps, where patterns must adhere to spatial constraints while maintaining coherence.

---

### 2. **Key Functions/Classes and Collaboration**  
**Core Components:**  
- **`Index` class**:  
  - **`__init__`**: Initializes the rulebook by creating a nested dictionary structure (`self.data`) to store transition rules. It uses `Directions` to determine valid relative positions based on the output size.  
  - **`add_rule`**: Adds a transition rule between two patterns at a specific relative position (e.g., "right" or "up").  
  - **`check_possibility`**: Validates whether a pattern can transition to another at a given relative position, ensuring compatibility with the rulebook.  

**Collaboration:**  
- **`Pattern` class** (from `Logic.Pattern`): Represents individual patterns (e.g., tile types) and is used as keys in the rulebook.  
- **`Directions` class** (from `Logic.directions`): Provides relative position vectors (e.g., `(0, 1)` for "down") based on the output size, which defines the grid dimensions.  

**Data Structure**:  
- `self.data` is a nested dictionary:  
  ```python
  {
      pattern1: {
          (relative_pos1): [next_pattern1, next_pattern2, ...],
          (relative_pos2): [...],
          ...
      },
      pattern2: {...},
      ...
  }
  ```  
  This structure allows efficient lookup of valid transitions during WFC algorithm execution.

---

### 3. **External Dependencies or APIs Used**  
- **`Pattern` class**: Defines the structure of individual patterns (e.g., tile types) and their properties.  
- **`Directions` class**: Generates relative position vectors (e.g., for grid-based movement) based on the output size.  
- **`typing.List`**: Ensures type hints for lists of patterns and relative positions.  

---

### 4. **Extension Ideas, Pitfalls, or TODOs**  
**Extension Ideas:**  
- **Support for Multi-Step Transitions**: Allow rules to define sequences of patterns (e.g., "pattern A → pattern B → pattern C") for more complex spatial logic.  
- **Weighted Transitions**: Add probabilities or weights to transitions for varied map generation.  
- **Dynamic Direction Handling**: Allow `Directions` to adapt to non-uniform grid sizes (e.g., irregular maps).  

**Pitfalls to Watch For:**  
- **Direction Calculation Errors**: Ensure `Directions` correctly computes relative positions for all grid sizes.  
- **Rule Conflicts**: Avoid contradictory rules (e.g., a pattern transitioning to two incompatible patterns at the same position).  
- **Performance**: For large pattern sets, nested dictionaries may become inefficient; consider optimizing with hash maps or sparse matrices.  

**TODOs:**  
- Add error handling for invalid relative positions in `add_rule`.  
- Implement a method to serialize/deserialize the rulebook for persistence.  
- Add support for checking all possible transitions for a pattern (e.g., `get_all_possible_transitions`).  
- Validate that `check_possibility` handles edge cases (e.g., empty lists, nested pattern lists).  

--- 

This implementation is foundational for WFC-based procedural generation, enabling flexible and rule-driven map creation while maintaining spatial coherence.

## Detected Imports

- from typing import List
- from Logic.Pattern import Pattern
- from Logic.directions import Directions
