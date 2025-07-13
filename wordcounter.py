import tkinter as tk
from tkinter import scrolledtext

class WordCounter:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Counter")
        self.root.geometry("400x300")

        # Create a frame
        frame = tk.Frame(self.root, bg="#f0f0f0")
        frame.pack(pady=10)

        # Create a scrolled text area for input
        self.text_area = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=40, height=10, bg="#ffffff", fg="#000000")
        self.text_area.pack(padx=10, pady=10)

        # Create a button to count words
        self.count_button = tk.Button(frame, text="Count Words", command=self.count_words, bg="#4CAF50", fg="#ffffff")
        self.count_button.pack(pady=5)

        # Create a label to display the word count
        self.word_count_label = tk.Label(frame, text="Word Count: 0", bg="#f0f0f0", fg="#000000", font=("Arial", 14))
        self.word_count_label.pack(pady=5)

    def count_words(self):
        text = self.text_area.get("1.0", tk.END).strip()
        if not text:
            self.word_count_label.config(text="Word Count: 0")
        else:
            words = text.split()
            self.word_count_label.config(text=f"Word Count: {len(words)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = WordCounter(root)
    root.mainloop()
