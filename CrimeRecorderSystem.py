import tkinter as tk
from tkinter import messagebox, ttk

class CrimeRecord:
    def __init__(self, id, crime_type, location, accused_name, officer):
        self.id = id
        self.crime_type = crime_type
        self.location = location
        self.accused_name = accused_name
        self.officer = officer

class CrimeRecordSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Crime Record Management System")
        self.root.geometry("800x550")

        # Title
        title = tk.Label(root, text="Crime Record Management System", font=("Verdana", 22, "bold"), fg="red")
        title.pack(pady=10)

        # Form Panel
        self.fields_frame = tk.Frame(root)
        self.fields_frame.pack(side=tk.LEFT, padx=10)

        self.tf_id = tk.Entry(self.fields_frame)
        self.cb_crime_type = ttk.Combobox(self.fields_frame, values=["Theft", "Murder", "Fraud", "Assault", "Cybercrime"])
        self.tf_location = tk.Entry(self.fields_frame)
        self.tf_accused = tk.Entry(self.fields_frame)
        self.tf_officer = tk.Entry(self.fields_frame)
        self.tf_search = tk.Entry(self.fields_frame)

        tk.Label(self.fields_frame, text="Crime ID:").grid(row=0, column=0, sticky=tk.W)
        self.tf_id.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.fields_frame, text="Crime Type:").grid(row=1, column=0, sticky=tk.W)
        self.cb_crime_type.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.fields_frame, text="Location:").grid(row=2, column=0, sticky=tk.W)
        self.tf_location.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.fields_frame, text="Accused Name:").grid(row=3, column=0, sticky=tk.W)
        self.tf_accused.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.fields_frame, text="Officer In Charge:").grid(row=4, column=0, sticky=tk.W)
        self.tf_officer.grid(row=4, column=1, padx=5, pady=5)

        btn_add = tk.Button(self.fields_frame, text="Add Record", command=self.add_record)
        btn_search = tk.Button(self.fields_frame, text="Search Crime Type", command=self.search_crime_type)
        btn_add.grid(row=5, column=0, padx=5, pady=5)
        btn_search.grid(row=5, column=1, padx=5, pady=5)

        # Table
        self.table = ttk.Treeview(root, columns=("ID", "Crime Type", "Location", "Accused", "Officer"), show='headings')
        self.table.heading("ID", text="ID")
        self.table.heading("Crime Type", text="Crime Type")
        self.table.heading("Location", text="Location")
        self.table.heading("Accused", text="Accused")
        self.table.heading("Officer", text="Officer")
        self.table.pack(side=tk.LEFT, padx=10, pady=10)

        # Bottom Panel
        bottom_frame = tk.Frame(root)
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

        tk.Label(bottom_frame, text="Search Crime Type:").pack(side=tk.LEFT)
        self.tf_search.pack(side=tk.LEFT, padx=5)
        btn_show_all = tk.Button(bottom_frame, text="Show All", command=self.show_all_records)
        btn_delete = tk.Button(bottom_frame, text="Delete Selected", command=self.delete_record)
        btn_show_all.pack(side=tk.LEFT, padx=5)
        btn_delete.pack(side=tk.LEFT, padx=5)

        # Initialize crime list
        self.crime_list = []
        self.show_all_records()

    def add_record(self):
        id = self.tf_id.get().strip()
        crime_type = self.cb_crime_type.get()
        location = self.tf_location.get().strip()
        accused = self.tf_accused.get().strip()
        officer = self.tf_officer.get().strip()

        if not all([id, crime_type, location, accused, officer]):
            messagebox.showwarning("Input Error", "Please fill all fields.")
            return

        record = CrimeRecord(id, crime_type, location, accused, officer)
        self.crime_list.append(record)
        self.show_all_records()
        self.clear_fields()

    def show_all_records(self):
        for row in self.table.get_children():
            self.table.delete(row)
        for cr in self.crime_list:
            self.table.insert("", "end", values=(cr.id, cr.crime_type, cr.location, cr.accused_name, cr.officer))

    def search_crime_type(self):
        search = self.tf_search.get().strip()
        for row in self.table.get_children():
            self.table.delete(row)
        for cr in self.crime_list:
            if cr.crime_type.lower() == search.lower():
                self.table.insert("", "end", values=(cr.id, cr.crime_type, cr.location, cr.accused_name, cr.officer))

    def delete_record(self):
        selected_item = self.table.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Select a record to delete.")
            return
        selected_id = self.table.item(selected_item)["values"][0]
        self.crime_list = [cr for cr in self.crime_list if cr.id != selected_id]
        self.show_all_records()

    def clear_fields(self):
        self.tf_id.delete(0, tk.END)
        self.tf_location.delete(0, tk.END)
        self.tf_accused.delete(0, tk.END)
        self.tf_officer.delete(0, tk.END)
        self.cb_crime_type.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = CrimeRecordSystem(root)
    root.mainloop()
