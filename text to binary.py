import tkinter as tk
from tkinter import messagebox, scrolledtext

class BinaryTextConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Binary ↔ Text Converter")
        self.root.geometry("700x800")
        
        # Create main frame with gradient background
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create header
        header_frame = tk.Frame(self.main_frame, bg="#6495ED")
        header_frame.pack(fill=tk.X, pady=20)
        
        title_label = tk.Label(header_frame, text="BINARY ↔ TEXT CONVERTER", font=("Segoe UI", 28), bg="#6495ED", fg="white")
        title_label.pack()
        
        # Create content frame
        content_frame = tk.Frame(self.main_frame, bg="#FFFFFF")
        content_frame.pack(pady=20, padx=30, fill=tk.BOTH, expand=True)
        
        # Binary to Text Section
        bin_to_text_label = tk.Label(content_frame, text="Binary to Text", font=("Segoe UI", 18), fg="#4682B4")
        bin_to_text_label.grid(row=0, column=0, pady=10)
        
        self.binary_input = scrolledtext.ScrolledText(content_frame, height=3, width=30, font=("Consolas", 14))
        self.binary_input.grid(row=1, column=0, padx=10, pady=10)
        
        bin_convert_btn = tk.Button(content_frame, text="Convert to Text", command=self.convert_bin_to_text, bg="#2ECC71", fg="white", font=("Segoe UI", 14))
        bin_convert_btn.grid(row=2, column=0, pady=10)
        
        self.text_output = scrolledtext.ScrolledText(content_frame, height=3, width=30, font=("Segoe UI", 14), bg="#F0F0F0", state='disabled')
        self.text_output.grid(row=3, column=0, padx=10, pady=10)
        
        # Text to Binary Section
        text_to_bin_label = tk.Label(content_frame, text="Text to Binary", font=("Segoe UI", 18), fg="#4682B4")
        text_to_bin_label.grid(row=4, column=0, pady=10)
        
        self.text_input = scrolledtext.ScrolledText(content_frame, height=3, width=30, font=("Segoe UI", 14))
        self.text_input.grid(row=5, column=0, padx=10, pady=10)
        
        text_convert_btn = tk.Button(content_frame, text="Convert to Binary", command=self.convert_text_to_bin, bg="#9B59B6", fg="white", font=("Segoe UI", 14))
        text_convert_btn.grid(row=6, column=0, pady=10)
        
        self.binary_output = scrolledtext.ScrolledText(content_frame, height=3, width=30, font=("Consolas", 14), bg="#F0F0F0", state='disabled')
        self.binary_output.grid(row=7, column=0, padx=10, pady=10)
        
        # Clear Button
        clear_btn = tk.Button(content_frame, text="Clear All", command=self.clear_all, bg="#E74C3C", fg="white", font=("Segoe UI", 14))
        clear_btn.grid(row=8, column=0, pady=20)
        
    def convert_bin_to_text(self):
        binary_str = self.binary_input.get("1.0", tk.END).replace(" ", "").strip()
        if all(bit in '01' for bit in binary_str):
            text = ""
            for i in range(0, len(binary_str), 8):
                byte_str = binary_str[i:i+8]
                if len(byte_str) == 8:
                    text += chr(int(byte_str, 2))
            self.text_output.config(state='normal')
            self.text_output.delete("1.0", tk.END)
            self.text_output.insert(tk.END, text)
            self.text_output.config(state='disabled')
        else:
            messagebox.showerror("Error", "Invalid binary input!")

    def convert_text_to_bin(self):
        text = self.text_input.get("1.0", tk.END).strip()
        binary = ''.join(format(ord(c), '08b') for c in text)
        self.binary_output.config(state='normal')
        self.binary_output.delete("1.0", tk.END)
        self.binary_output.insert(tk.END, binary)
        self.binary_output.config(state='disabled')

    def clear_all(self):
        self.binary_input.delete("1.0", tk.END)
        self.text_output.config(state='normal')
        self.text_output.delete("1.0", tk.END)
        self.text_output.config(state='disabled')
        self.text_input.delete("1.0", tk.END)
        self.binary_output.config(state='normal')
        self.binary_output.delete("1.0", tk.END)
        self.binary_output.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = BinaryTextConverter(root)
    root.mainloop()
