# dnd_map_gen_wfc_AI/Logic/Index.py

> Language: python | Size: 822 bytes

## Model qwen3:8b

### 1. **Purpose Summary**  
The `Index` class in `Index.py` serves as a central registry for managing **rules between patterns** in a **Walkable Finite State (WFC)** algorithm. It enables defining valid transitions between patterns based on spatial relationships (e.g., adjacent tiles) and provides a mechanism to validate whether a pattern can follow another at a specific relative position. This is critical for procedural map generation in games like D&D, where patterns represent tile configurations and transitions enforce spatial coherence.

---

### 2. **Key Functions/Classes and Collaboration**  
**Core Components:**  
- **`Index` class**:  
  - **`__init__`**: Initializes the rule registry by creating a nested dictionary structure (`self.data`) where keys are `Pattern` objects, and values are dictionaries mapping directions to lists of allowed next patterns.  
  - **`add_rule`**: Registers a transition rule between two patterns at a specific relative position (e.g., "right" or "up").  
  - **`check_possibility`**: Validates if a `check_pattern` can follow a `pattern` at a given relative position by checking the pre-registered rules.  

**Collaboration:**  
- **`Pattern` class** (from `Logic.Pattern`): Represents tile configurations and acts as keys in the `self.data` dictionary.  
- **`Directions` class** (from `Logic.directions`): Generates directional tuples (e.g., `(0, 1)` for right) based on the output size, which defines the spatial relationships between patterns.  

**Data Structure**:  
- `self.data` is a nested dictionary:  
  ```python
  {
      pattern1: {
          direction1: [next_pattern1, next_pattern2, ...],
          direction2: [...],
          ...
      },
      pattern2: {...},
      ...
  }
  ```

---

### 3. **External Dependencies or APIs Used**  
- **`Pattern` class**: Represents tile configurations and is used as keys in the rule registry.  
- **`Directions` class**: Provides directional tuples (e.g., `(dx, dy)`) to define spatial relationships between patterns.  
- **`typing.List`**: For type hints in function parameters (e.g., `List[Pattern]`).  

---

### 4. **Extension Ideas, Pitfalls, or TODOs**  
**Extension Ideas:**  
- **Add Rule Prioritization**: Allow weighted rules for probabilistic transitions (e.g., certain patterns are more likely to follow others).  
- **Support for Multi-Directional Rules**: Extend `add_rule` to handle complex spatial relationships (e.g., diagonal adjacency).  
- **Dynamic Rule Updates**: Enable runtime modification of rules for adaptive map generation.  

**Pitfalls to Watch For:**  
- **Direction Handling**: Ensure `Directions` correctly maps relative positions to coordinate deltas (e.g., `(0, 1)` for right, `(1, 0)` for down).  
- **Data Structure Consistency**: Avoid mismatches between `Pattern` objects and their registered rules (e.g., typos in `Pattern` names).  
- **Edge Cases**: Handle cases where a pattern has no valid transitions (e.g., isolated tiles) during map generation.  

**TODOs:**  
- **Test `check_possibility` with Lists**: Verify that the logic correctly handles lists of patterns (e.g., `pattern = pattern[0]` in `check_possibility`).  
- **Add Error Handling**: Raise exceptions for invalid relative positions or missing rules.  
- **Optimize Lookup**: Use `frozenset` or `tuple` keys for `self.data` to improve performance for large rule sets.  

--- 

This implementation forms the backbone of a WFC-based procedural map generator, enabling spatially coherent tile pattern transitions.

## Detected Imports

- from typing import List
- from Logic.Pattern import Pattern
- from Logic.directions import Directions
