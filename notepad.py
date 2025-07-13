import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Notepad")
        self.root.geometry("800x600")
        
        # Create text area with scrollbar
        self.text_area = scrolledtext.ScrolledText(root, undo=True)
        self.text_area.pack(fill="both", expand=True)
        
        # Create menu bar
        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)
        
        # File menu
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file, accelerator="Ctrl+N")
        file_menu.add_command(label="Open", command=self.open_file, accelerator="Ctrl+O")
        file_menu.add_command(label="Save", command=self.save_file, accelerator="Ctrl+S")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        self.menu_bar.add_cascade(label="File", menu=file_menu)
        
        # Edit menu
        edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        edit_menu.add_command(label="Undo", command=self.text_area.edit_undo, accelerator="Ctrl+Z")
        edit_menu.add_command(label="Redo", command=self.text_area.edit_redo, accelerator="Ctrl+Y")
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut", command=self.cut, accelerator="Ctrl+X")
        edit_menu.add_command(label="Copy", command=self.copy, accelerator="Ctrl+C")
        edit_menu.add_command(label="Paste", command=self.paste, accelerator="Ctrl+V")
        edit_menu.add_command(label="Select All", command=self.select_all, accelerator="Ctrl+A")
        self.menu_bar.add_cascade(label="Edit", menu=edit_menu)
        
        # Help menu
        help_menu = tk.Menu(self.menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.about)
        self.menu_bar.add_cascade(label="Help", menu=help_menu)
        
        # Keyboard shortcuts
        self.text_area.bind('<Control-n>', lambda e: self.new_file())
        self.text_area.bind('<Control-o>', lambda e: self.open_file())
        self.text_area.bind('<Control-s>', lambda e: self.save_file())
        self.text_area.bind('<Control-a>', lambda e: self.select_all())

    def new_file(self):
        self.text_area.delete("1.0", tk.END)
        
    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as file:
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert("1.0", file.read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.text_area.get("1.0", tk.END))
    
    def cut(self):
        self.text_area.event_generate("<<Cut>>")
    
    def copy(self):
        self.text_area.event_generate("<<Copy>>")
    
    def paste(self):
        self.text_area.event_generate("<<Paste>>")
    
    def select_all(self):
        self.text_area.tag_add('sel', '1.0', tk.END)
    
    def about(self):
        messagebox.showinfo("About", "Simple Notepad\nCreated with Python Tkinter")

if __name__ == "__main__":
    root = tk.Tk()
    app = Notepad(root)
    root.mainloop()
