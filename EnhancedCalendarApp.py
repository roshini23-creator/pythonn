import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime, timedelta
import calendar
from tkcalendar import DateEntry

class EnhancedCalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mobile Style Calendar with Search")
        self.root.geometry("400x650")  # Increased height for search panel
        
        # Configure main colors
        self.bg_color = "#f5f5f5"
        self.header_color = "#4285f4"
        self.weekday_color = "#757575"
        self.today_color = "#4285f4"
        self.day_color = "#212121"
        self.other_month_color = "#bdbdbd"
        self.cell_color = "#ffffff"
        self.selected_color = "#e3f2fd"

        # Set up current date
        self.current_date = datetime.now()
        self.selected_date = None
        
        # Create UI
        self.create_header()
        self.create_search_panel()  # New search panel
        self.create_weekday_header()
        self.create_calendar_grid()
        self.create_footer()
        
        # Populate calendar
        self.update_calendar()

    def create_header(self):
        header_frame = tk.Frame(self.root, bg=self.header_color, height=80)
        header_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Previous month button
        prev_btn = tk.Button(header_frame, text="◀", command=lambda: self.change_month(-1),
                            bg=self.header_color, fg="white", bd=0, font=("Arial", 14))
        prev_btn.pack(side=tk.LEFT, padx=10)
        
        # Month and year display
        self.month_year_var = tk.StringVar()
        month_year_lbl = tk.Label(header_frame, textvariable=self.month_year_var,
                                 bg=self.header_color, fg="white", font=("Arial", 18, "bold"))
        month_year_lbl.pack(side=tk.LEFT, expand=True)
        
        # Next month button
        next_btn = tk.Button(header_frame, text="▶", command=lambda: self.change_month(1),
                            bg=self.header_color, fg="white", bd=0, font=("Arial", 14))
        next_btn.pack(side=tk.RIGHT, padx=10)

    def create_search_panel(self):
        search_frame = tk.Frame(self.root, bg=self.bg_color)
        search_frame.pack(fill=tk.X, padx=10, pady=(5, 0))
        
        tk.Label(search_frame, text="Search Date:", bg=self.bg_color).pack(side=tk.LEFT)
        
        # Date picker for search
        self.search_date_entry = DateEntry(
            search_frame, 
            date_pattern="dd/mm/yyyy",
            background="white",
            foreground="black",
            selectbackground="lightblue",
            maxdate=datetime(2100, 12, 31),
            mindate=datetime(1900, 1, 1)
        )
        self.search_date_entry.pack(side=tk.LEFT, padx=5)
        
        search_btn = tk.Button(search_frame, text="Go", command=self.search_date)
        search_btn.pack(side=tk.LEFT)

    def create_weekday_header(self):
        weekday_frame = tk.Frame(self.root, bg=self.bg_color)
        weekday_frame.pack(fill=tk.X, padx=10, pady=5)
        
        weekdays = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
        for day in weekdays:
            tk.Label(weekday_frame, text=day, bg=self.bg_color, fg=self.weekday_color, 
                    font=("Arial", 10), width=5).pack(side=tk.LEFT)

    def create_calendar_grid(self):
        self.calendar_frame = tk.Frame(self.root, bg=self.bg_color)
        self.calendar_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Create grid for calendar days (6 rows x 7 columns)
        self.day_buttons = []
        for row in range(6):
            row_frame = tk.Frame(self.calendar_frame, bg=self.bg_color)
            row_frame.pack(fill=tk.X)
            row_buttons = []
            for col in range(7):
                day_btn = tk.Button(row_frame, text="", bd=0, font=("Arial", 12), 
                                   width=5, height=2, bg=self.cell_color)
                day_btn.pack(side=tk.LEFT, padx=2, pady=2)
                row_buttons.append(day_btn)
            self.day_buttons.append(row_buttons)

    def create_footer(self):
        footer_frame = tk.Frame(self.root, bg=self.bg_color, height=30)
        footer_frame.pack(fill=tk.X, padx=5, pady=5)
        
        today_btn = tk.Button(footer_frame, text="TODAY", command=self.go_to_today,
                             bg=self.today_color, fg="white", bd=0, font=("Arial", 10))
        today_btn.pack(pady=5)

    def update_calendar(self):
        self.month_year_var.set(self.current_date.strftime("%B %Y"))
        
        # Get the calendar for current month
        cal = calendar.monthcalendar(self.current_date.year, self.current_date.month)
        today = datetime.now()
        
        # Clear all buttons first
        for row in self.day_buttons:
            for btn in row:
                btn.config(text="", bg=self.cell_color, fg=self.day_color,
                          state=tk.NORMAL, relief=tk.RAISED)
        
        # Fill in the days
        today_found = False
        for week_num, week in enumerate(cal):
            for day_num, day in enumerate(week):
                if day == 0:
                    continue  # Skip empty days
                    
                btn = self.day_buttons[week_num][day_num]
                btn.config(text=str(day), 
                          command=lambda d=day: self.select_day(d))
                
                # Highlight today
                if (self.current_date.year == today.year and 
                    self.current_date.month == today.month and 
                    day == today.day):
                    btn.config(bg=self.today_color, fg="white")
                    today_found = True
                
        # If today not in current month view, indicate with an asterisk
        if not today_found and self.current_date.month == today.month:
            for week_num, week in enumerate(cal):
                for day_num, day in enumerate(week):
                    if day == today.day:
                        btn = self.day_buttons[week_num][day_num]
                        btn.config(text=f"{day}*", fg=self.today_color)
                        break

    def select_day(self, day):
        self.selected_date = self.current_date.replace(day=day)
        self.highlight_selected_day(day)
        messagebox.showinfo("Date Selected", self.selected_date.strftime("%A, %B %d, %Y"))

    def highlight_selected_day(self, day):
        cal = calendar.monthcalendar(self.current_date.year, self.current_date.month)
        for week_num, week in enumerate(cal):
            for day_num, day_val in enumerate(week):
                btn = self.day_buttons[week_num][day_num]
                if day_val == day:
                    btn.config(relief=tk.SUNKEN, bg=self.selected_color)
                else:
                    btn.config(relief=tk.RAISED, bg=self.cell_color)

    def search_date(self):
        try:
            search_date = self.search_date_entry.get_date()
            if search_date:
                self.current_date = search_date
                self.update_calendar()
                self.highlight_selected_day(search_date.day)
        except Exception as e:
            messagebox.showerror("Invalid Date", "Please select a valid date")

    def change_month(self, delta):
        # Calculate new month (handling year boundaries)
        new_month = self.current_date.month + delta
        new_year = self.current_date.year
        
        if new_month > 12:
            new_month = 1
            new_year += 1
        elif new_month < 1:
            new_month = 12
            new_year -= 1
            
        self.current_date = self.current_date.replace(year=new_year, month=new_month, day=1)
        self.update_calendar()

    def go_to_today(self):
        self.current_date = datetime.now()
        self.update_calendar()
        self.highlight_selected_day(self.current_date.day)

if __name__ == "__main__":
    root = tk.Tk()
    
    # Install the required calendar widget if not already installed
    try:
        from tkcalendar import DateEntry
    except ImportError:
        messagebox.showerror("Dependency Missing", "Please install tkcalendar package:\npip install tkcalendar")
        root.destroy()
        exit()
    
    app = EnhancedCalendarApp(root)
    root.mainloop()
