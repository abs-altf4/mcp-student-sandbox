# Mystery Module Documentation

## Overview

The `mystery_module.py` file contains a mathematical utility function that solves quadratic equations using the **Quadratic Formula**.

## Module Contents

### Function: `fn_x(a, b, c)`

**Purpose:** Solves quadratic equations of the form `ax² + bx + c = 0`

#### Parameters:
- `a` (float): Coefficient of x² term (must not be 0)
- `b` (float): Coefficient of x term
- `c` (float): Constant term

#### Returns:
- `tuple[float, float]`: Two solutions (roots) of the equation
- `None`: If the discriminant is negative (no real solutions)

## Mathematical Background

The function implements the **Quadratic Formula**:

$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

Where:
- **Discriminant** ($\Delta$) = $b^2 - 4ac$
  - If $\Delta > 0$: Two distinct real solutions
  - If $\Delta = 0$: One repeated real solution
  - If $\Delta < 0$: No real solutions (returns `None`)

## Usage Examples

### Example 1: Standard Quadratic Equation
```python
from mystery_module import fn_x

# Solve: x² - 5x + 6 = 0
# Expected roots: x = 2, x = 3
result = fn_x(1, -5, 6)
print(result)  # Output: (3.0, 2.0)
```

### Example 2: Equation with No Real Solutions
```python
from mystery_module import fn_x

# Solve: x² + 1 = 0 (or x² + 0x + 1 = 0)
# This has no real solutions
result = fn_x(1, 0, 1)
print(result)  # Output: None
```

### Example 3: Equation with Repeated Root
```python
from mystery_module import fn_x

# Solve: x² - 2x + 1 = 0
# Expected root: x = 1 (repeated)
result = fn_x(1, -2, 1)
print(result)  # Output: (1.0, 1.0)
```

## Implementation Details

```python
import math

def fn_x(a, b, c):
    d = b**2 - 4*a*c                    # Calculate discriminant
    if d < 0: 
        return None                      # No real solutions
    return ((-b + math.sqrt(d))/(2*a),   # First root (x1)
            (-b - math.sqrt(d))/(2*a))   # Second root (x2)
```

## Edge Cases

| Case | Input | Output | Notes |
|------|-------|--------|-------|
| No real solutions | `fn_x(1, 0, 1)` | `None` | Discriminant is negative |
| Repeated root | `fn_x(1, -2, 1)` | `(1.0, 1.0)` | Discriminant equals zero |
| Standard case | `fn_x(1, -5, 6)` | `(3.0, 2.0)` | Discriminant is positive |
| Negative coefficient | `fn_x(-1, 5, -6)` | `(-2.0, -3.0)` | Works with negative `a` |

## Limitations

⚠️ **Important Considerations:**

1. **Floating-point Precision**: Due to floating-point arithmetic, results may have minor precision errors
2. **Zero Coefficient**: Does not validate if `a = 0` (would cause division by zero)
3. **Complex Numbers**: Cannot handle complex roots when discriminant is negative
4. **Poor Naming**: Function name `fn_x` is not descriptive; use `solve_quadratic()` instead

## Recommendations for Improvement

### 1. Better Function Naming
```python
def solve_quadratic(a, b, c):
    """Solve quadratic equation ax² + bx + c = 0"""
    ...
```

### 2. Input Validation
```python
def solve_quadratic(a, b, c):
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero")
    ...
```

### 3. Enhanced Return Type
```python
from typing import Optional, Tuple

def solve_quadratic(a: float, b: float, c: float) -> Optional[Tuple[float, float]]:
    """
    Solve quadratic equation ax² + bx + c = 0
    
    Returns:
        Tuple of two roots if real solutions exist, None otherwise
    """
    ...
```

### 4. Comprehensive Docstring
```python
def solve_quadratic(a: float, b: float, c: float) -> Optional[Tuple[float, float]]:
    """
    Solve quadratic equation of the form ax² + bx + c = 0.
    
    Args:
        a: Coefficient of x² (must not be 0)
        b: Coefficient of x
        c: Constant term
        
    Returns:
        Tuple of two roots if discriminant >= 0, None if no real solutions
        
    Raises:
        ValueError: If coefficient 'a' is zero
        
    Examples:
        >>> solve_quadratic(1, -5, 6)
        (3.0, 2.0)
        >>> solve_quadratic(1, 0, 1)
        None
    """
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero")
    
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None
    
    sqrt_discriminant = math.sqrt(discriminant)
    return (
        (-b + sqrt_discriminant) / (2*a),
        (-b - sqrt_discriminant) / (2*a)
    )
```

## Testing

### Unit Tests Recommended
```python
import unittest
from mystery_module import fn_x

class TestQuadraticSolver(unittest.TestCase):
    def test_two_distinct_roots(self):
        self.assertEqual(fn_x(1, -5, 6), (3.0, 2.0))
    
    def test_no_real_solutions(self):
        self.assertIsNone(fn_x(1, 0, 1))
    
    def test_repeated_root(self):
        self.assertEqual(fn_x(1, -2, 1), (1.0, 1.0))
```

## Related Resources

- [Quadratic Equation - Wikipedia](https://en.wikipedia.org/wiki/Quadratic_equation)
- [Quadratic Formula - Khan Academy](https://www.khanacademy.org/)
- [Python math module documentation](https://docs.python.org/3/library/math.html)

## License

This module is part of the CENG302 student sandbox project.

---

**Last Updated:** March 26, 2026  
**Status:** Documented and Ready for Enhancement
