def greater_of_three(a : int, b : int, c : int) -> int:
    """Return the greatest of three numbers."""
    return max(a, b, c)

if __name__ == "__main__":
    # Example usage
    num1 = 10
    num2 = 20
    num3 = 15
    greatest_number = greater_of_three(num1, num2, num3)
    print(f"The greatest number among {num1}, {num2}, and {num3} is: {greatest_number}")