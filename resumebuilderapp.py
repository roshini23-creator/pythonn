import tkinter as tk
from tkinter import messagebox, scrolledtext

class ResumeBuilder:
    def __init__(self, root):
        self.root = root
        self.root.title("Creative Resume Builder")
        self.root.geometry("700x700")
        self.root.configure(bg="#FFFAF0")

        # Title
        title = tk.Label(root, text="Resume Builder", font=("SansSerif", 24, "bold"), bg="#FFFAF0")
        title.pack(pady=10)

        # Input Fields
        self.fields = {
            "Name": tk.StringVar(),
            "Email": tk.StringVar(),
            "Phone": tk.StringVar(),
            "Skills": tk.StringVar(),
            "Education": tk.StringVar(),
            "Experience": tk.StringVar(),
            "Projects": tk.StringVar(),
            "Certifications": tk.StringVar(),
            "References": tk.StringVar()
        }

        for field in self.fields:
            frame = tk.Frame(root, bg="#FFFAF0")
            label = tk.Label(frame, text=f"{field}:", bg="#FFFAF0", fg="#4682B4")
            entry = tk.Entry(frame, textvariable=self.fields[field], width=40)
            label.pack(side=tk.LEFT, padx=5, pady=5)
            entry.pack(side=tk.LEFT, padx=5, pady=5)
            frame.pack(pady=5)

        # Buttons
        button_frame = tk.Frame(root, bg="#FFFAF0")
        generate_btn = tk.Button(button_frame, text="Generate Resume", command=self.generate_resume, bg="#90EE90")
        save_btn = tk.Button(button_frame, text="Save as Text", command=self.save_resume, bg="#ADD8E6")
        reset_btn = tk.Button(button_frame, text="Reset", command=self.reset_fields, bg="#FFB6C1")
        
        generate_btn.pack(side=tk.LEFT, padx=10)
        save_btn.pack(side=tk.LEFT, padx=10)
        reset_btn.pack(side=tk.LEFT, padx=10)
        button_frame.pack(pady=10)

        # Preview Area
        self.preview_area = scrolledtext.ScrolledText(root, font=("Courier New", 12), width=80, height=15)
        self.preview_area.pack(pady=10)
        self.preview_area.config(state=tk.DISABLED)

    def generate_resume(self):
        resume = "==================== RESUME ====================\n"
        for field, value in self.fields.items():
            resume += f"{field}: {value.get()}\n"
        resume += "=================================================\n"
        self.preview_area.config(state=tk.NORMAL)
        self.preview_area.delete(1.0, tk.END)
        self.preview_area.insert(tk.END, resume)
        self.preview_area.config(state=tk.DISABLED)

    def save_resume(self):
        resume_text = self.preview_area.get(1.0, tk.END)
        if resume_text.strip() == "":
            messagebox.showwarning("Warning", "Please generate a resume before saving.")
            return
        with open("MyResume.txt", "w") as file:
            file.write(resume_text)
        messagebox.showinfo("Success", "Resume saved as MyResume.txt")

    def reset_fields(self):
        for field in self.fields:
            self.fields[field].set("")
        self.preview_area.config(state=tk.NORMAL)
        self.preview_area.delete(1.0, tk.END)
        self.preview_area.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = ResumeBuilder(root)
    root.mainloop()
