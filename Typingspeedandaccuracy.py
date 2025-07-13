import tkinter as tk
from tkinter import messagebox
import time

class TypingTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Test")
        self.root.geometry("800x700")
        self.root.configure(bg="#CCEEFF")

        self.text_to_type = (
            "This is a longer text for you to practice your typing skills. "
            "The quick brown fox jumps over the lazy dog. "
            "Typing practice helps improve your speed and accuracy. "
            "Consistent practice and focus can lead to significant improvements over time. "
            "Remember to keep your posture correct and hands relaxed while typing."
        )

        self.timer_running = False
        self.start_time = None
        self.word_count = 0
        self.correct_word_count = 0
        self.mistakes_count = 0

        self.create_widgets()

    def create_widgets(self):
        # Text area for the text to type
        self.text_area = tk.Text(self.root, height=10, width=80, bg="#D3D3D3", fg="blue", font=("Arial", 14))
        self.text_area.insert(tk.END, self.text_to_type)
        self.text_area.config(state=tk.DISABLED)
        self.text_area.pack(pady=10)

        # Input area for user input
        self.input_area = tk.Text(self.root, height=5, width=80, bg="white", fg="black", font=("Arial", 14))
        self.input_area.pack(pady=10)
        self.input_area.bind("<KeyRelease>", self.check_input)

        # Control panel
        self.control_frame = tk.Frame(self.root, bg="#003366")
        self.control_frame.pack(pady=10)

        self.start_button = tk.Button(self.control_frame, text="Start", command=self.start_test, bg="green", fg="white")
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(self.control_frame, text="Stop", command=self.stop_test, bg="red", fg="white", state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT, padx=10)

        self.clear_button = tk.Button(self.control_frame, text="Clear", command=self.clear_test, bg="yellow", fg="black", state=tk.DISABLED)
        self.clear_button.pack(side=tk.LEFT, padx=10)

        # Labels for timer and statistics
        self.timer_label = tk.Label(self.control_frame, text="Time: 0.0s", bg="#003366", fg="white")
        self.timer_label.pack(side=tk.LEFT, padx=10)

        self.word_count_label = tk.Label(self.control_frame, text="Words: 0", bg="#003366", fg="white")
        self.word_count_label.pack(side=tk.LEFT, padx=10)

        self.correct_words_label = tk.Label(self.control_frame, text="Correct: 0", bg="#003366", fg="white")
        self.correct_words_label.pack(side=tk.LEFT, padx=10)

        self.mistakes_label = tk.Label(self.control_frame, text="Mistakes: 0", bg="#003366", fg="white")
        self.mistakes_label.pack(side=tk.LEFT, padx=10)

        self.speed_label = tk.Label(self.control_frame, text="Speed: 0 WPM", bg="#003366", fg="white")
        self.speed_label.pack(side=tk.LEFT, padx=10)

    def start_test(self):
        self.input_area.config(state=tk.NORMAL)
        self.input_area.delete(1.0, tk.END)
        self.input_area.focus()
        self.timer_running = True
        self.start_time = time.time()
        self.update_timer()
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.clear_button.config(state=tk.NORMAL)

    def stop_test(self):
        self.timer_running = False
        self.calculate_speed()
        self.input_area.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.DISABLED)
        messagebox.showinfo("Typing Test", f"Your time: {self.timer_label['text']}")

    def clear_test(self):
        self.input_area.config(state=tk.DISABLED)
        self.input_area.delete(1.0, tk.END)
        self.timer_running = False
        self.start_time = None
        self.word_count = 0
        self.correct_word_count = 0
        self.mistakes_count = 0
        self.timer_label.config(text="Time: 0.0s")
        self.word_count_label.config(text="Words: 0")
        self.correct_words_label.config(text="Correct: 0")
        self.mistakes_label.config(text="Mistakes: 0")
        self.speed_label.config(text="Speed: 0 WPM")
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.clear_button.config(state=tk.DISABLED)

    def update_timer(self):
        if self.timer_running:
            elapsed_time = time.time() - self.start_time
            self.timer_label.config(text=f"Time: {elapsed_time:.1f}s")
            self.root.after(100, self.update_timer)

    def check_input(self, event):
        input_text = self.input_area.get(1.0, tk.END).strip()
        text_words = self.text_to_type.split()
        input_words = input_text.split()

        self.word_count = len(input_words)
        self.correct_word_count = 0
        self.mistakes_count = 0

        for i in range(len(input_words)):
            if i < len(text_words) and input_words[i] == text_words[i]:
                self.correct_word_count += 1
            else:
                self.mistakes_count += 1

        self.word_count_label.config(text=f"Words: {self.word_count}")
        self.correct_words_label.config(text=f"Correct: {self.correct_word_count}")
        self.mistakes_label.config(text=f"Mistakes: {self.mistakes_count}")

        if input_text == self.text_to_type:
            self.stop_test()

    def calculate_speed(self):
        elapsed_time = time.time() - self.start_time
        minutes = elapsed_time / 60.0
        wpm = self.word_count / minutes if minutes > 0 else 0
        self.speed_label.config(text=f"Speed: {int(wpm)} WPM")

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingTest(root)
    root.mainloop()
