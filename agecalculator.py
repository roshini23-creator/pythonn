import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_age():
    # Get the input from the user
    birth_date_str = entry_birth_date.get()
    current_date_str = entry_current_date.get()
    
    try:
        # Convert the input strings to date objects
        birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")
        current_date = datetime.strptime(current_date_str, "%Y-%m-%d")
        
        # Calculate the difference between the current date and birth date
        age_timedelta = current_date - birth_date
        
        # Total days
        total_days = age_timedelta.days
        
        # Total weeks
        total_weeks = total_days // 7
        
        # Total months (approximation)
        total_months = (current_date.year - birth_date.year) * 12 + current_date.month - birth_date.month
        
        # Total years
        total_years = current_date.year - birth_date.year
        if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
            total_years -= 1
        
        # Total hours
        total_hours = total_days * 24 + current_date.hour
        
        # Total minutes
        total_minutes = total_hours * 60 + current_date.minute
        
        # Total seconds
        total_seconds = age_timedelta.total_seconds()
        
        # Display the result
        messagebox.showinfo("Age Calculator", 
                            f"From your birth date to the current date:\n"
                            f"Total years: {total_years} years\n"
                            f"Total days: {total_days} days\n"
                            f"Total weeks: {total_weeks} weeks\n"
                            f"Total months: {total_months} months\n"
                            f"Total hours: {total_hours} hours\n"
                            f"Total minutes: {total_minutes} minutes\n"
                            f"Total seconds: {int(total_seconds)} seconds")
    except ValueError:
        messagebox.showerror("Invalid Date", "Please enter valid dates in YYYY-MM-DD format.")

# Create the main window
root = tk.Tk()
root.title("Age Calculator")
root.config(bg="purple")


# Create and place the label and entry for birth date
label_birth_date = tk.Label(root, text="Enter your birth date (YYYY-MM-DD):")
label_birth_date.pack(pady=10)

entry_birth_date = tk.Entry(root)
entry_birth_date.pack(pady=10)

# Create and place the label and entry for current date
label_current_date = tk.Label(root, text="Enter the current date (YYYY-MM-DD):")
label_current_date.pack(pady=10)

entry_current_date = tk.Entry(root)
entry_current_date.pack(pady=10)

# Create and place the calculate button
button_calculate = tk.Button(root, text="Calculate Age", command=calculate_age)
button_calculate.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()




