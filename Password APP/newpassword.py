import tkinter as tk
from tkinter import messagebox
from tkinter import *
import json
import base64  # Added for basic encoding
import secrets
import string

# --- Password Generation ---
def generate_password(length=16):
    """Generates a strong, random password."""
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password

def generate_password_command():
    """Generates a password and inserts it into the password entry."""
    password = generate_password()
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# --- Encoding/Decoding Functions ---
def encode_password(password):
    """Encodes the password using base64."""
    encoded_bytes = base64.b64encode(password.encode('utf-8'))
    return encoded_bytes.decode('utf-8')

def decode_password(encoded_password):
    """Decodes the password using base64."""
    decoded_bytes = base64.b64decode(encoded_password.encode('utf-8'))
    return decoded_bytes.decode('utf-8')

def update_account():
    """Adds a new email/password combination to a website's account list."""
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()

    if not all([website, email, password]):
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    try:
        with open("data2.json", "r") as file:  # Changed filename to data2.json
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}  # Start with an empty dictionary if the file doesn't exist

    if website not in data:
        data[website] = []  # Initialize with an empty list for accounts

    # Encode the password before saving
    encoded_password = encode_password(password)

    # Add the new account to the list of accounts for the website
    data[website].append({
        "Email": email,
        "Password": encoded_password  # Save the encoded password
    })

    try:
        with open("data2.json", "w") as file:  # Changed filename to data2.json
            json.dump(data, file, indent=4)
        messagebox.showinfo("Success", "Account added successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error writing to file: {e}")

    website_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

def search_account():
    """Searches for accounts for a given website and displays the email/password."""
    website = website_entry.get().strip()

    if not website:
        messagebox.showerror("Error", "Please enter a website to search for.")
        return

    try:
        with open("data2.json", "r") as file:  # Changed filename to data2.json
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        messagebox.showinfo("Info", "No data found for this website.")
        return

    if website not in data:
        messagebox.showinfo("Info", "No data found for this website.")
        return

    accounts = data[website]
    if not accounts:
        messagebox.showinfo("Info", "No accounts found for this website.")
        return

    # Display all accounts
    message = ""
    for i, account in enumerate(accounts):
        email = account["Email"]
        encoded_password = account["Password"]
        password = decode_password(encoded_password)  # Decode the password
        message += f"Account {i+1}:\nEmail: {email}\nPassword: {password}\n\n"

    messagebox.showinfo(f"Accounts for {website}", message)
# ----------------------- UI SETUP -----------------------
window = tk.Tk()
window.title("Account Updater")


website_label = tk.Label(text="Website:")
website_label.grid(row=0, column=0)
website_entry = tk.Entry(width=30)
website_entry.grid(row=0, column=1)

email_label = tk.Label(text="Email:")
email_label.grid(row=1, column=0)
email_entry = tk.Entry(width=30)
email_entry.grid(row=1, column=1)

password_label = tk.Label(text="Password:")
password_label.grid(row=2, column=0)
password_entry = tk.Entry(width=30)
password_entry.grid(row=2, column=1)

update_button = tk.Button(text="Update Account", command=update_account)
update_button.grid(row=3, column=1)

search_button = tk.Button(text="Search Account", command=search_account)
search_button.grid(row=4, column=1)  # Add search button

generate_password_button = tk.Button(text="Generate Password", command=generate_password_command)
generate_password_button.grid(row=2, column=2)  # Add button next to password entry

window.mainloop()
