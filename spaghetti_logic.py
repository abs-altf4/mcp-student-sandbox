# Configuration Constants
PRICE_MULTIPLIER = 1.15
LOG_FILE_PATH = "log.txt"


def calculate_adjusted_values(values: list[float], multiplier: float) -> list[float]:
    """
    Apply multiplier to each value in the list.
    
    Args:
        values: List of numeric values to adjust
        multiplier: Factor to multiply each value by
        
    Returns:
        List of adjusted values
    """
    return [value * multiplier for value in values]


def format_value_for_display(value: float) -> str:
    """
    Format a single value for console display.
    
    Args:
        value: The value to format
        
    Returns:
        Formatted string representation of the value
    """
    return f"Total: {value:.2f}"


def display_results(values: list[float]) -> None:
    """
    Display all calculated values to console.
    
    Args:
        values: List of values to display
    """
    for value in values:
        formatted_output = format_value_for_display(value)
        print(formatted_output)


def save_results_to_log(values: list[float], log_file: str = LOG_FILE_PATH) -> None:
    """
    Append results to log file.
    
    Args:
        values: List of values to log
        log_file: Path to log file (default: LOG_FILE_PATH)
    """
    with open(log_file, "a") as f:
        f.write(str(values) + "\n")


def process_data(data: list[float]) -> list[float]:
    """
    Process data: calculate adjusted values, display, and log results.
    
    This is the main orchestrator function that coordinates:
    1. Calculation of adjusted values
    2. Display of results
    3. Logging to file
    
    Args:
        data: List of values to process
        
    Returns:
        List of adjusted values
    """
    adjusted_values = calculate_adjusted_values(data, PRICE_MULTIPLIER)
    display_results(adjusted_values)
    save_results_to_log(adjusted_values)
    return adjusted_values
