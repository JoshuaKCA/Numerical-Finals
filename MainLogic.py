import sympy as sp
i = 0
x = sp.symbols('x')

x1 = float(input("Please enter the value of x_1: "))
x0 = float(input("Please enter the value of x0: "))
user_input = input("Please enter the value of the function: ")
iteration = int(input("Please input how many iterations to be done: "))

#Function Evaluation
function = sp.sympify(user_input)
print(f"Stored function: {function}")

#x1 function value
ans_x1 = function.subs(x, x1)
num_ans_x1 = ans_x1.evalf()
print(f"x1 function = {round(num_ans_x1, 6)}")

#x0 function value
ans_x0 = function.subs(x, x0)
num_ans_x0 = ans_x0.evalf()
print(f"x0 function = {round(num_ans_x0, 6)}")

#print x0 and x1 value
print(f"x0: {x0}, x1: {x1}")

#formula for Secant Method
formula = x0 - (num_ans_x0 * (x1-x0))/(num_ans_x1 - num_ans_x0)
temp = (sp.sympify(round(formula, 6)))
print(f"First value: {temp}")

#Pause
input("Please press enter to continue...")

#New x0 value
ans_x0 = function.subs(x, x0)
num_ans_x0 = ans_x0.evalf()

#New x1 value
x1 = temp
ans_x1 = function.subs(x, x1)
num_ans_x1 = ans_x1.evalf()
 
#formula for Secant Method
formula = x0 - (num_ans_x0 * (x1-x0))/(num_ans_x1 - num_ans_x0)
print(formula)
temp = (sp.sympify(round(formula, 6))) 

#Print values
print(f"x0 value = {x0}")
print(f"x1 value = {x1}")
print(f"x0 function = {round(num_ans_x0, 6)}")
print(f"x1 function = {round(num_ans_x1, 6)}")
print(f"Next value: {temp}")

#Pause
input("Please press enter to continue...")

#Setup for iterations
while i < iteration - 2:
    #New x0 value
    x0 = x1
    ans_x0 = function.subs(x, x0)
    num_ans_x0 = ans_x0.evalf()
    
    #New x1 value
    x1 = temp
    ans_x1 = function.subs(x, x1)
    num_ans_x1 = ans_x1.evalf()
    
    #formula for Secant Method
    formula = x0 - (num_ans_x0 * (x1-x0))/(num_ans_x1 - num_ans_x0)
    temp = (sp.sympify(round(formula, 6))) 
    
    #Print values
    print(f"x0 value = {x0}")
    print(f"x1 value = {x1}")
    print(f"x0 function = {round(num_ans_x0, 6)}")
    print(f"x1 function = {round(num_ans_x1, 6)}")
    print(f"Next Value: {temp}")
    
    #Pause
    input("Please press enter to continue...")
    i += 1