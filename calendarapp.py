# Importing tkinter module
from tkinter import *
from tkinter import messagebox
import calendar

# Function to show the calendar of the given year
def showCalendar():
    year = year_field.get().strip()  # Fetch and clean input

    if not year.isdigit() or int(year) < 1:  # Validate year
        messagebox.showerror("Invalid Input", "Please enter a valid year!")
        return
    
    year = int(year)

    # Creating a new window for the calendar
    gui = Toplevel(new)  # Use Toplevel instead of Tk() to avoid multiple main windows
    gui.config(background='white')
    gui.title(f"Calendar for {year}")
    gui.geometry("600x700")
    gui.minsize(500, 600)  # Set minimum size

    # Formatting the calendar output
    cal_content = calendar.TextCalendar().formatyear(year, 2, 1, 1, 3)

    # Creating a scrollable text widget
    text_widget = Text(gui, font=("Consolas", 10), bg="white", wrap=NONE)
    text_widget.insert(END, cal_content)  # Insert calendar text
    text_widget.config(state=DISABLED)  # Disable editing
    
    # Adding Scrollbars
    scroll_y = Scrollbar(gui, orient=VERTICAL, command=text_widget.yview)
    scroll_x = Scrollbar(gui, orient=HORIZONTAL, command=text_widget.xview)
    
    text_widget.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
    
    # Layout
    text_widget.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
    scroll_y.grid(row=0, column=1, sticky="ns")
    scroll_x.grid(row=1, column=0, sticky="ew")

    # Make the window resizable
    gui.grid_rowconfigure(0, weight=1)
    gui.grid_columnconfigure(0, weight=1)

# Driver code
if __name__ == "__main__":
    # Creating main window
    new = Tk()
    new.config(background='black')
    new.title("Calendar")
    new.geometry("250x140")
    new.minsize(250, 140)

    # Creating widgets
    cal_label = Label(new, text="Calendar", bg='grey', font=("times", 20, "bold"))
    year_label = Label(new, text="Enter Year", bg='yellow')
    year_field = Entry(new)
    button = Button(new, text='Show Calendar', fg='black', bg='orange', command=showCalendar)
    exit_button = Button(new, text='Exit', fg='Black', bg='pink', command=new.quit)

    # Placing widgets in position
    cal_label.grid(row=0, column=0, columnspan=2, pady=5)
    year_label.grid(row=1, column=0, padx=5, pady=5)
    year_field.grid(row=1, column=1, padx=5, pady=5)
    button.grid(row=2, column=0, columnspan=2, pady=5)
    exit_button.grid(row=3, column=0, columnspan=2, pady=5)

    # Running the main loop
    new.mainloop()



