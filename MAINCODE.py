import customtkinter
import sympy as sp

# logic_BCKP.py content
def calculate_secant_method(x1, x0, user_input, iterations):
    x = sp.symbols('x')
    
    # Function Evaluation
    function = sp.sympify(user_input)
    print(f"Stored function: {function}")
    
    # x1 function value
    ans_x1 = function.subs(x, x1)
    num_ans_x1 = ans_x1.evalf()
    print(f"x1 function = {round(num_ans_x1, 6)}")

    # x0 function value
    ans_x0 = function.subs(x, x0)
    num_ans_x0 = ans_x0.evalf()
    print(f"x0 function = {round(num_ans_x0, 6)}")

    # print x0 and x1 value
    print(f"x0: {x0}, x1: {x1}")

    # formula for Secant Method
    formula = x0 - (num_ans_x0 * (x1 - x0)) / (num_ans_x1 - num_ans_x0)
    temp = sp.sympify(round(formula, 6))
    print(f"First value: {temp}")

    # New x0 value
    ans_x0 = function.subs(x, x0)
    num_ans_x0 = ans_x0.evalf()

    # New x1 value
    x1 = temp
    ans_x1 = function.subs(x, x1)
    num_ans_x1 = ans_x1.evalf()
    
    # formula for Secant Method
    formula = x0 - (num_ans_x0 * (x1 - x0)) / (num_ans_x1 - num_ans_x0)
    print(formula)
    temp = sp.sympify(round(formula, 6)) 

    # Print values
    print(f"x0 value = {x0}")
    print(f"x1 value = {x1}")
    print(f"x0 function = {round(num_ans_x0, 6)}")
    print(f"x1 function = {round(num_ans_x1, 6)}")
    print(f"Next value: {temp}")

    for i in range(iterations - 1):
        # New x0 value
        x0 = x1
        ans_x0 = function.subs(x, x0)
        num_ans_x0 = ans_x0.evalf()
        
        # New x1 value
        x1 = temp
        ans_x1 = function.subs(x, x1)
        num_ans_x1 = ans_x1.evalf()
        
        # formula for Secant Method
        formula = x0 - (num_ans_x0 * (x1 - x0)) / (num_ans_x1 - num_ans_x0)
        temp = sp.sympify(round(formula, 6))
        
        # Print values
        print(f"Iteration {i+2}:")
        print(f"x0 value = {x0}")
        print(f"x1 value = {x1}")
        print(f"x0 function = {round(num_ans_x0, 6)}")
        print(f"x1 function = {round(num_ans_x1, 6)}")
        print(f"Next value: {temp}")

    return x1

# MAINCODE.py content
root = customtkinter.CTk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        # configure window
        self.geometry("640x480")
        self._max_height = (screen_height)
        self._max_width = (screen_width)
        self.title("GUI Test")
        
        # set grid
        self.grid_rowconfigure((0,1,2,3,4,5,6), weight=0) 
        self.grid_columnconfigure((0), weight=1)
        
        # set widgets
        self.label = customtkinter.CTkLabel(self, text="Input the values for the Secant Method", font=("Arial", 20))
        self.label.grid(row=0, column=0, pady=50, sticky="n")
        self.entry_x1 = customtkinter.CTkEntry(self, placeholder_text="Enter the value of x1", font=("Arial", 15))
        self.entry_x1.grid(row=1, column=0, pady=10, padx=200, sticky="ew")
        self.entry_x0 = customtkinter.CTkEntry(self, placeholder_text="Enter the value of x0", font=("Arial", 15))
        self.entry_x0.grid(row=2, column=0, pady=10, padx=200, sticky="ew")
        self.entry_function = customtkinter.CTkEntry(self, placeholder_text="Enter the function", font=("Arial", 15))
        self.entry_function.grid(row=3, column=0, pady=10, padx=200, sticky="ew")
        self.entry_iterations = customtkinter.CTkEntry(self, placeholder_text="Number of iterations to be done", font=("Arial", 15))
        self.entry_iterations.grid(row=4, column=0, pady=10, padx=200, sticky="ew")
        self.button = customtkinter.CTkButton(self, text="Calculate", font=("Arial", 15), command=self.get_input)
        self.button.grid(row=6, column=0, pady=10, padx=200, sticky="ew")
        
    def get_input(self):
        x1 = float(self.entry_x1.get())
        x0 = float(self.entry_x0.get())
        user_input = self.entry_function.get()
        iterations = int(self.entry_iterations.get())
        
        # Create a top-level window to display the iterations
        self.top_level = customtkinter.CTkToplevel(self)
        self.top_level.title("Iterations")
        self.textbox = customtkinter.CTkTextbox(self.top_level, width=600, height=400)
        self.textbox.pack(pady=20, padx=20)
        self.textbox.configure(state="disabled")  # Make the textbox read-only
        
        def update_callback(message):
            self.textbox.configure(state="normal")
            self.textbox.insert(customtkinter.END, message)
            self.textbox.see(customtkinter.END)
            self.textbox.configure(state="disabled")
        
        # Redirect print statements to the top-level window
        import sys
        class PrintRedirector:
            def __init__(self, callback):
                self.callback = callback
            def write(self, message):
                if message.strip():  # Avoid printing empty lines
                    self.callback(message + '\n')
            def flush(self):
                pass
        
        sys.stdout = PrintRedirector(update_callback)
        
        # Use the imported function to calculate the result
        result = calculate_secant_method(x1, x0, user_input, iterations)
        update_callback(f"Result: {result}\n")
        
        # Restore the original stdout
        sys.stdout = sys.__stdout__
        
if __name__ == "__main__":
    app = App()
    app.mainloop()