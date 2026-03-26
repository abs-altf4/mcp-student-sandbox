def average_ratios(numbers: list[float]) -> float:
    """
    Calculate the average of ratios (100 / each number).
    
    Args:
        numbers: List of non-zero numeric values
        
    Returns:
        Average of all ratios
        
    Raises:
        ValueError: If list is empty or contains zero values
        TypeError: If input is not a list of numbers
    """
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    # Validate no zeros exist in input
    if any(num == 0 for num in numbers):
        raise ValueError("Input list contains zero value(s) - division by zero not allowed")
    
    total = 0
    for number in numbers:
        total += 100 / number
    
    return total / len(numbers)


# Test cases
if __name__ == "__main__":
    # Test valid input
    try:
        result = average_ratios([10, 5, 2])
        print(f"Success with [10, 5, 2]: {result:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    
    # Test with zero - will raise ValueError
    try:
        result = average_ratios([10, 5, 0])
        print(f"Success with [10, 5, 0]: {result:.2f}")
    except ValueError as e:
        print(f"Error with [10, 5, 0]: {e}")
    
    # Test empty list
    try:
        result = average_ratios([])
        print(f"Success with []: {result:.2f}")
    except ValueError as e:
        print(f"Error with []: {e}")
