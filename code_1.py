def calculate_larger(a : int,b : int) -> int:
    """
    This function takes two integers and returns the larger one.
    If both are equal, it returns either one.
    """
    if a > b:
        return a
    else:
        return b
    
    
if __name__ == "__main__":
    # Example usage
    num1 = 10
    num2 = 20
    larger_number = calculate_larger(num1, num2)
    print(f"The larger number between {num1} and {num2} is: {larger_number}")