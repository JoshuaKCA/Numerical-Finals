import sympy as sp

def calculate_secant_method(x1, x0, user_input, iterations):
    x = sp.symbols('x')
    
    # Function Evaluation
    function = sp.sympify(user_input)
    print(f"Stored function: {function}")

    for i in range(iterations):
        # x1 function value
        ans_x1 = function.subs(x, x1)
        num_ans_x1 = ans_x1.evalf()
        print(f"x1 function = {round(num_ans_x1, 6)}")

        # x0 function value
        ans_x0 = function.subs(x, x0)
        num_ans_x0 = ans_x0.evalf()
        print(f"x0 function = {round(num_ans_x0, 6)}")

        # Print x0 and x1 value
        print(f"x0: {x0}, x1: {x1}")

        # Formula for Secant Method
        formula = x0 - (num_ans_x0 * (x1 - x0)) / (num_ans_x1 - num_ans_x0)
        temp = sp.sympify(round(formula, 6))
        print(f"Iteration {i+1} value: {temp}")

        # Update x0 and x1 for next iteration
        x0, x1 = x1, temp

    return x1

# Example usage (for testing purposes)
if __name__ == "__main__":
    x1 = float(input("Please enter the value of x_1: "))
    x0 = float(input("Please enter the value of x0: "))
    user_input = input("Please enter the value of the function: ")
    iterations = int(input("Please input how many iterations to be done: "))
    result = calculate_secant_method(x1, x0, user_input, iterations)
    print(f"Final result: {result}")