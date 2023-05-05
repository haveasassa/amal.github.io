from tkinter import *
from tkinter import messagebox

# Create a window
window = Tk()
window.title("Login Form")

# Create a function to validate the user's credentials
def validate_login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "admin" and password == "password":
        messagebox.showinfo("Success", "Login successful!")
        # TODO: redirect to main application window
    else:
        messagebox.showerror("Error", "Invalid username or password")

# Create a username label and entry field
username_label = Label(window, text="Username:")
username_label.pack()
username_entry = Entry(window)
username_entry.pack()

# Create a password label and entry field
password_label = Label(window, text="Password:")
password_label.pack()
password_entry = Entry(window, show="*")
password_entry.pack()

# Create a login button
login_button = Button(window, text="Login", command=validate_login)
login_button.pack()

# Run the window
window.mainloop()
