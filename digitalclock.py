import tkinter as tk
from tkinter import font
import time
from datetime import datetime

class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock")
        self.root.geometry("500x200")
        self.root.configure(bg="black")

        # Create a font for the time and date
        self.time_font = font.Font(family="Arial", size=60, weight="bold")
        self.date_font = font.Font(family="Arial", size=20)

        # Create a label to display the time
        self.time_label = tk.Label(root, font=self.time_font, bg="black", fg="red")
        self.time_label.pack(pady=20)

        # Create a label to display the date
        self.date_label = tk.Label(root, font=self.date_font, bg="black", fg="white")
        self.date_label.pack(pady=10)

        # Start the clock
        self.update_time_and_date()

    def update_time_and_date(self):
        # Get the current time and format it
        current_time = datetime.now().strftime("%H:%M:%S")
        # Get the current date and format it
        current_date = datetime.now().strftime("%a, %b %d, %Y")

        # Update the time and date labels
        self.time_label.config(text=current_time)
        self.date_label.config(text=current_date)

        # Call this method again after 1000 milliseconds (1 second)
        self.root.after(1000, self.update_time_and_date)

if __name__ == "__main__":
    root = tk.Tk()
    clock = DigitalClock(root)
    root.mainloop()
