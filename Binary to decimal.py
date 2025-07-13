import tkinter as tk
from tkinter import messagebox

class BinaryDecimalConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("BitWise Converter")
        self.root.geometry("600x500")
        
        # Create header
        header_frame = tk.Frame(self.root, bg="#4682B4", bd=5)
        header_frame.pack(fill=tk.X)
        
        title_label = tk.Label(header_frame, text="BITWISE CONVERTER", bg="#4682B4", fg="white", font=("Arial", 26))
        title_label.pack(pady=15)
        
        # Create content frame
        content_frame = tk.Frame(self.root, bg="#F0F0F0", bd=5)
        content_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        
        # Binary to Decimal Section
        self.binary_input = tk.Entry(content_frame, font=("Arial", 14), bd=2)
        self.binary_input.grid(row=0, column=0, padx=10, pady=10)
        
        bin_to_dec_btn = tk.Button(content_frame, text="Convert to Decimal", command=self.convert_bin_to_dec, bg="#6495ED", fg="white", font=("Arial", 14))
        bin_to_dec_btn.grid(row=1, column=0, padx=10, pady=10)
        
        self.decimal_output = tk.Label(content_frame, text="Decimal: ", font=("Arial", 14))
        self.decimal_output.grid(row=2, column=0, padx=10, pady=10)
        
        # Decimal to Binary Section
        self.decimal_input = tk.Entry(content_frame, font=("Arial", 14), bd=2)
        self.decimal_input.grid(row=3, column=0, padx=10, pady=10)
        
        dec_to_bin_btn = tk.Button(content_frame, text="Convert to Binary", command=self.convert_dec_to_bin, bg="#6495ED", fg="white", font=("Arial", 14))
        dec_to_bin_btn.grid(row=4, column=0, padx=10, pady=10)
        
        self.binary_output = tk.Label(content_frame, text="Binary: ", font=("Arial", 14))
        self.binary_output.grid(row=5, column=0, padx=10, pady=10)
        
        # Clear Button
        clear_btn = tk.Button(content_frame, text="Clear All", command=self.clear_all, bg="#DC3545", fg="white", font=("Arial", 14))
        clear_btn.grid(row=6, column=0, padx=10, pady=20)
        
    def convert_bin_to_dec(self):
        binary_str = self.binary_input.get()
        if all(bit in '01' for bit in binary_str):
            decimal = int(binary_str, 2)
            self.decimal_output.config(text=f"Decimal: {decimal}")
        else:
            messagebox.showerror("Error", "Invalid binary number! Only 0s and 1s allowed.")
    
    def convert_dec_to_bin(self):
        try:
            decimal = int(self.decimal_input.get())
            if decimal < 0:
                raise ValueError
            binary_str = bin(decimal)[2:]  # Remove the '0b' prefix
            self.binary_output.config(text=f"Binary: {binary_str}")
        except ValueError:
            messagebox.showerror("Error", "Invalid decimal number! Only positive integers allowed.")
    
    def clear_all(self):
        self.binary_input.delete(0, tk.END)
        self.decimal_input.delete(0, tk.END)
        self.binary_output.config(text="Binary: ")
        self.decimal_output.config(text="Decimal: ")

if __name__ == "__main__":
    root = tk.Tk()
    app = BinaryDecimalConverter(root)
    root.mainloop()
