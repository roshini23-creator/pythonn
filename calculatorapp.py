import tkinter as tk
from tkinter import font

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("350x550")
        self.root.resizable(False, False)
        self.root.configure(bg="#2E3440")
        
        # Custom colors
        self.bg_color = "#2E3440"
        self.display_bg = "#3B4252"
        self.button_bg = "#434C5E"
        self.button_fg = "#ECEFF4"
        self.operator_bg = "#5E81AC"
        self.special_bg = "#BF616A"
        
        # Font settings
        self.display_font = font.Font(family='Helvetica', size=24)
        self.button_font = font.Font(family='Helvetica', size=16, weight='bold')
        
        self.create_widgets()
        self.bind_keys()
        
    def create_widgets(self):
        # Display frame
        display_frame = tk.Frame(self.root, height=100, bg=self.display_bg)
        display_frame.pack(expand=True, fill='both', padx=10, pady=(20, 10))
        
        # Display label
        self.display = tk.Label(
            display_frame,
            text="0",
            anchor='e',
            bg=self.display_bg,
            fg=self.button_fg,
            font=self.display_font,
            padx=10
        )
        self.display.pack(expand=True, fill='both')
        
        # Button frame
        button_frame = tk.Frame(self.root, bg=self.bg_color)
        button_frame.pack(expand=True, fill='both', padx=10, pady=(0, 10))
        
        # Button layout
        buttons = [
            ('C', '(', ')', '/'),
            ('7', '8', '9', '*'),
            ('4', '5', '6', '-'),
            ('1', '2', '3', '+'),
            ('±', '0', '.', '='),
            ('sin', 'cos', 'tan', '√')
        ]
        
        # Create buttons
        for i, row in enumerate(buttons):
            for j, char in enumerate(row):
                # Determine button color
                if char in ['C', '±']:
                    bg_color = self.special_bg
                elif char in ['+', '-', '*', '/', '=', '(', ')', 'sin', 'cos', 'tan', '√']:
                    bg_color = self.operator_bg
                else:
                    bg_color = self.button_bg
                
                # Create button
                button = tk.Button(
                    button_frame,
                    text=char,
                    bg=bg_color,
                    fg=self.button_fg,
                    font=self.button_font,
                    borderwidth=0,
                    activebackground="#4C566A",
                    activeforeground=self.button_fg,
                    relief='flat',
                    command=lambda x=char: self.on_button_click(x)
                )
                button.grid(
                    row=i, column=j,
                    sticky='nsew',
                    padx=2, pady=2,
                    ipadx=10, ipady=15
                )
                button_frame.grid_columnconfigure(j, weight=1)
            button_frame.grid_rowconfigure(i, weight=1)
    
    def bind_keys(self):
        self.root.bind("<Return>", lambda event: self.calculate())
        for char in '1234567890+-*/.()':
            self.root.bind(char, lambda event, c=event.char: self.on_button_click(c))
    
    def on_button_click(self, char):
        current = self.display['text']
        
        if char == 'C':
            self.display.config(text="0")
        elif char == '±':
            if current.startswith('-'):
                self.display.config(text=current[1:])
            else:
                self.display.config(text=f'-{current}')
        elif char == '=':
            self.calculate()
        elif char in ['sin', 'cos', 'tan', '√']:
            self.handle_functions(char)
        else:
            if current == '0' and char not in ['(', ')']:
                self.display.config(text=char)
            else:
                self.display.config(text=f'{current}{char}')
    
    def calculate(self):
        try:
            expression = self.display['text']
            
            # Replace special symbols with Python equivalents
            expression = expression.replace('√', 'math.sqrt')
            expression = expression.replace('sin', 'math.sin')
            expression = expression.replace('cos', 'math.cos')
            expression = expression.replace('tan', 'math.tan')
            
            # Add math module imports
            if any(f'math.{func}' in expression for func in ['sqrt', 'sin', 'cos', 'tan']):
                import math
            
            result = eval(expression)
            self.display.config(text=str(result))
        except Exception:
            self.display.config(text="Error")
    
    def handle_functions(self, func):
        current = self.display['text']
        
        if func == '√':
            self.display.config(text=f'√({current})')
        else:
            self.display.config(text=f'{func}({current})')

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
