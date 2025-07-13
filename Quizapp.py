import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f0f0")

        # Questions, options, and answers
        self.questions = [
            "What is the capital of France?",
            "Which planet is known as the Red Planet?",
            "Who wrote 'Romeo and Juliet'?",
            "What is the boiling point of water?",
            "What is the largest mammal?",
            "What is the currency of Japan?",
            "Which element has the chemical symbol 'O'?",
            "What is the hardest natural substance on Earth?",
            "Who painted the Mona Lisa?",
            "What is the smallest prime number?"
        ]

        self.options = [
            ["Berlin", "Madrid", "Paris", "London"],
            ["Earth", "Mars", "Jupiter", "Venus"],
            ["William Shakespeare", "Charles Dickens", "Mark Twain", "Leo Tolstoy"],
            ["100°C", "90°C", "120°C", "80°C"],
            ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
            ["Yen", "Dollar", "Euro", "Pound"],
            ["Oxygen", "Gold", "Silver", "Hydrogen"],
            ["Diamond", "Ruby", "Sapphire", "Emerald"],
            ["Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Claude Monet"],
            ["1", "2", "3", "4"]
        ]

        self.answers = [2, 1, 0, 0, 1, 0, 0, 0, 0, 1]  # Correct options indexes

        self.current_question = 0
        self.score = 0

        # Question label
        self.lbl_question = tk.Label(root, text="Question", font=("Arial", 16), bg="#f0f0f0")
        self.lbl_question.pack(pady=20)

        # Options panel
        self.var = tk.IntVar()
        self.radio_options = []
        for i in range(4):
            radio = tk.Radiobutton(root, text="", variable=self.var, value=i, font=("Arial", 14), bg="#f0f0f0")
            radio.pack(anchor="w", padx=20, pady=5)
            self.radio_options.append(radio)

        # Next button
        self.btn_next = tk.Button(root, text="Next", command=self.next_question, bg="#4CAF50", fg="white", font=("Arial", 14))
        self.btn_next.pack(pady=20)

        self.load_question()

    def load_question(self):
        self.lbl_question.config(text=f"Q{self.current_question + 1}: {self.questions[self.current_question]}")
        for i, option in enumerate(self.options[self.current_question]):
            self.radio_options[i].config(text=option)
        self.var.set(-1)  # Reset selection

        if self.current_question == len(self.questions) - 1:
            self.btn_next.config(text="Submit")

    def next_question(self):
        if self.var.get() == -1:
            messagebox.showwarning("Warning", "Please select an answer.")
            return

        if self.var.get() == self.answers[self.current_question]:
            self.score += 1

        self.current_question += 1
        if self.current_question < len(self.questions):
            self.load_question()
        else:
            self.show_result()

    def show_result(self):
        messagebox.showinfo("Result", f"Your score: {self.score}/{len(self.questions)}")
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
