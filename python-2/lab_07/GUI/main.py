import tkinter as tk
from tkinter import messagebox
import requests

url = 'http://localhost:8000'

class CRUDApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter CRUD App")
        self.root.geometry("400x400")

        self.get_button = tk.Button(root, text="Get Users", command=self.get_users)
        self.get_button.pack()

        self.label = tk.Label(root, text="User ID:")
        self.label.pack()

        self.user_id_entry = tk.Entry(root)
        self.user_id_entry.pack()

        self.name_label = tk.Label(root, text="Name:")
        self.name_label.pack()

        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.email_label = tk.Label(root, text="Email:")
        self.email_label.pack()

        self.email_entry = tk.Entry(root)
        self.email_entry.pack()

        self.password_label = tk.Label(root, text="Password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(root)
        self.password_entry.pack()

        self.create_button = tk.Button(root, text="Create User", command=self.create_user)
        self.create_button.pack()

        self.update_button = tk.Button(root, text="Update User", command=self.update_user)
        self.update_button.pack()

        self.delete_button = tk.Button(root, text="Delete User", command=self.confirm_delete_user)
        self.delete_button.pack()

    def get_users(self):
        try:
            response = requests.get(f"{url}/users")
            users_data = response.json()
            messagebox.showinfo("Users Details", str(users_data))
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

    def create_user(self):
        try:
            user_id = self.user_id_entry.get()
            name = self.name_entry.get()
            email = self.email_entry.get()
            password = self.password_entry.get()

            response = requests.post(f"{url}/users", json={
                "id": user_id,
                "name": name,
                "email": email,
                "password": password
            })
            messagebox.showinfo("Success", "User created successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {response.json()['message']}")
            messagebox.showerror("Error", f"Error: {e}")

    def update_user(self):
        try:
            response = requests.put(f"{url}/users/{self.user_id_entry.get()}", json={
                "id": self.user_id_entry.get(),
                "name": self.name_entry.get(),
                "email": self.email_entry.get(),
                "password": self.password_entry.get()
            })
            messagebox.showinfo("Success", "User updated successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {response.json()['message']}")
            messagebox.showerror("Error", f"Error: {e}")

    def confirm_delete_user(self):
        confirmation = messagebox.askokcancel("Delete Confirmation", "Are you sure you want to delete this user?")
        if confirmation:
            self.delete_user()

    def delete_user(self):
        try:
            response = requests.delete(f"{url}/users/{self.user_id_entry.get()}")
            messagebox.showinfo("Success", "User deleted successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {response.json()['message']}")
            messagebox.showerror("Error", f"Error: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CRUDApp(root)
    root.mainloop()
