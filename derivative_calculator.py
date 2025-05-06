import sympy

def get_derivative(function_str, variable_str):
    try:
        variable = sympy.symbols(variable_str)

        local_dict = {variable_str: variable}
        function_expr = sympy.sympify(function_str, locals=local_dict)

        derivative_expr = sympy.diff(function_expr, variable)

        return str(derivative_expr)
    except (sympy.SympifyError, TypeError) as e:
        return f"Error: Could not parse the function or differentiate. Details: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"
