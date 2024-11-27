import customtkinter
from MainLogic import calculate_secant_method  # Ensure this matches the exact file name

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
        self.grid_rowconfigure((0,1,2,3,4,5), weight=0) 
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
        self.button.grid(row=5, column=0, pady=10, padx=200, sticky="ew")
        
    def get_input(self):
        x1 = float(self.entry_x1.get())
        x0 = float(self.entry_x0.get())
        user_input = self.entry_function.get()
        iterations = int(self.entry_iterations.get())
        
        # Use the imported function to calculate the result
        result = calculate_secant_method(x1, x0, user_input, iterations)
        print(f"Result: {result}")
        
if __name__ == "__main__":
    app = App()
    app.mainloop()