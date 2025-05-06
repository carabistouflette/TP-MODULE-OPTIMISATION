import sympy

def get_derivative(function_str, variable_str):
    try:
        # Define the symbolic variable
        variable = sympy.symbols(variable_str)

        # Parse the function string into a sympy expression
        # It's important to provide a local dictionary with the variable
        # to ensure the string is parsed correctly.
        local_dict = {variable_str: variable}
        function_expr = sympy.sympify(function_str, locals=local_dict)

        # Calculate the derivative
        derivative_expr = sympy.diff(function_expr, variable)

        return str(derivative_expr)
    except (sympy.SympifyError, TypeError) as e:
        return f"Error: Could not parse the function or differentiate. Details: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

if __name__ == "__main__":
    # Example usage
    func_str = input("Enter the function (e.g., x**3 + 2*x**2 - x + 5): ")
    var_str = input("Enter the variable to differentiate with respect to (e.g., x): ")

    if not func_str or not var_str:
        print("Function and variable cannot be empty.")
    else:
        derivative = get_derivative(func_str, var_str)
        print(f"The function is: f({var_str}) = {func_str}")
        print(f"The derivative f'({var_str}) is: {derivative}")

    # Some more examples:
    print("\n--- Additional Examples ---")
    functions_to_test = [
        ("sin(x)", "x"),
        ("cos(y**2)", "y"),
        ("exp(z*a)", "z"), # Differentiating with respect to z, a is a constant
        ("log(t)", "t"),
        ("x**2 * y + y**3", "x"),
        ("x**2 * y + y**3", "y"),
        ("1/x", "x"),
        ("sqrt(x)", "x")
    ]

    for func, var in functions_to_test:
        deriv = get_derivative(func, var)
        print(f"Function: f({var}) = {func}, Derivative f'({var}): {deriv}")