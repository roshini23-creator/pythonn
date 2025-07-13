import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime

class Member:
    def __init__(self, member_id, name, age, phone, plan):
        self.id = member_id
        self.name = name
        self.age = age
        self.phone = phone
        self.plan = plan
        self.join_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class GymManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Gym Management System")
        self.root.geometry("800x500")
        self.root.configure(bg="#CCEEFF")

        # Data
        self.members = {}

        # Header
        self.header_frame = tk.Frame(self.root, bg="#003366")
        self.header_frame.pack(fill=tk.X)
        self.title_label = tk.Label(self.header_frame, text="GYM MANAGEMENT SYSTEM", bg="#003366", fg="white", font=("Arial", 24))
        self.title_label.pack(pady=10)

        # Input Frame
        self.input_frame = tk.Frame(self.root, bg="#CCEEFF")
        self.input_frame.pack(pady=10)

        self.name_label = tk.Label(self.input_frame, text="Name:", bg="#CCEEFF")
        self.name_label.grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(self.input_frame)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.age_label = tk.Label(self.input_frame, text="Age:", bg="#CCEEFF")
        self.age_label.grid(row=1, column=0, padx=10, pady=5)
        self.age_entry = tk.Entry(self.input_frame)
        self.age_entry.grid(row=1, column=1, padx=10, pady=5)

        self.phone_label = tk.Label(self.input_frame, text="Phone:", bg="#CCEEFF")
        self.phone_label.grid(row=2, column=0, padx=10, pady=5)
        self.phone_entry = tk.Entry(self.input_frame)
        self.phone_entry.grid(row=2, column=1, padx=10, pady=5)

        self.plan_label = tk.Label(self.input_frame, text="Plan (Basic/Premium):", bg="#CCEEFF")
        self.plan_label.grid(row=3, column=0, padx=10, pady=5)
        self.plan_entry = tk.Entry(self.input_frame)
        self.plan_entry.grid(row=3, column=1, padx=10, pady=5)

        # Button Frame
        self.button_frame = tk.Frame(self.root, bg="#CCEEFF")
        self.button_frame.pack(pady=10)

        self.add_button = tk.Button(self.button_frame, text="Add Member", command=self.add_member, bg="#009933", fg="white")
        self.add_button.pack(side=tk.LEFT, padx=10)

        self.remove_button = tk.Button(self.button_frame, text="Remove Member", command=self.remove_member, bg="#CC0000", fg="white")
        self.remove_button.pack(side=tk.LEFT, padx=10)

        self.view_button = tk.Button(self.button_frame, text="View Details", command=self.view_member_details, bg="#003366", fg="white")
        self.view_button.pack(side=tk.LEFT, padx=10)

        # Members List
        self.member_listbox = tk.Listbox(self.root, width=50, height=15)
        self.member_listbox.pack(pady=10)

        # Member Details Area
        self.details_text = tk.Text(self.root, width=50, height=10, state='disabled')
        self.details_text.pack(pady=10)

    def add_member(self):
        name = self.name_entry.get().strip()
        age = self.age_entry.get().strip()
        phone = self.phone_entry.get().strip()
        plan = self.plan_entry.get().strip()

        if not name or not age or not phone or not plan:
            messagebox.showerror("Error", "Please fill all fields!")
            return

        try:
            age = int(age)
            member_id = f"M{len(self.members) + 1}"
            new_member = Member(member_id, name, age, phone, plan)
            self.members[member_id] = new_member
            self.member_listbox.insert(tk.END, f"{member_id} - {name}")
            self.clear_fields()
            messagebox.showinfo("Success", f"Member added successfully!\nID: {member_id}\nName: {name}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid age!")

    def remove_member(self):
        selected_index = self.member_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Please select a member!")
            return

        selected_member = self.member_listbox.get(selected_index)
        member_id = selected_member.split(" - ")[0]
        del self.members[member_id]
        self.member_listbox.delete(selected_index)
        self.details_text.config(state='normal')
        self.details_text.delete(1.0, tk.END)
        self.details_text.config(state='disabled')
        messagebox.showinfo("Success", f"Member removed: {selected_member}")

    def view_member_details(self):
        selected_index = self.member_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Please select a member!")
            return

        selected_member = self.member_listbox.get(selected_index)
        member_id = selected_member.split(" - ")[0]
        member = self.members[member_id]

        self.details_text.config(state='normal')
        self.details_text.delete(1.0, tk.END)
        self.details_text.insert(tk.END, f"Member Details:\n"
                                           f"ID: {member.id}\n"
                                           f"Name: {member.name}\n"
                                           f"Age: {member.age}\n"
                                           f"Phone: {member.phone}\n"
                                           f"Plan: {member.plan}\n"
                                           f"Join Date: {member.join_date}\n")
        self.details_text.config(state='disabled')

    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.plan_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = GymManagementSystem(root)
    root.mainloop()
