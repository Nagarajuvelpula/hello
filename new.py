import streamlit as st
import tkinter as tk
from tkinter import messagebox as msg
import mysql.connector
import re


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nagaraju@123",
    database="register_1"
)

cursor = db.cursor()

window = tk.Tk()
window.title("Registration Page")


def execute_query(query, values=None):
    try:
        cursor.execute(query, values)
        db.commit()
        return True
    except mysql.connector.Error as error:
        print("Error:", error)
        db.rollback()
        return False


def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[!@#$%^&*]", password):
        return False
    return True


def validate_name(name):
    if not re.match(r"^[A-Za-z]+$", name):
        return False
    return True


def validate_phone_number(ph_number):
    if len(ph_number) != 10:
        return False
    if not ph_number.isdigit():
        return False
    return True


def register():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    user_name = user_name_entry.get()
    ph_number = ph_number_entry.get()
    password = password_entry.get()
    conform_password = conform_password_entry.get()

    if not all([first_name, last_name, user_name, ph_number, password, conform_password]):
        msg.showerror("Error", "Please fill all the fields")
        return
    if not validate_name(first_name):
        msg.showerror("Error", "Invalid first name, Please enter characters only")
        return

    if not validate_name(last_name):
        msg.showerror("Error", "Invalid last name , Please enter characters only")
        return
    if password != conform_password:
        msg.showerror("Error", "Passwords doesn't matched")
        return

    if not validate_password(password):
        msg.showerror(
            "Error",
            "Invalid password. It should have at least 8 characters, one special character, and one uppercase letter",
        )
        return

    if not validate_phone_number(ph_number):
        msg.showerror("Error", "Invalid phone number, Please enter 10 digits")
        return

    query = "SELECT * FROM users_1 WHERE user_name = %s"
    values = (user_name,)
    cursor.execute(query, values)
    existing_user = cursor.fetchone()
    if existing_user:
        msg.showerror("Error", "User already exists")
        return

    query = "INSERT INTO users_1 (first_name, last_name, user_name, ph_number, password, conform_password) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (first_name, last_name, user_name, ph_number, password, conform_password)

    if execute_query(query, values):
        msg.showinfo("Register Successfully")

        first_name_entry.delete(0, tk.END)
        last_name_entry.delete(0, tk.END)
        user_name_entry.delete(0, tk.END)
        ph_number_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        conform_password_entry.delete(0, tk.END)

    else:
        msg.showerror("Registration Failure")


first_name_label = tk.Label(window, text="First Name:")
first_name_label.pack()
first_name_entry = tk.Entry(window)
first_name_entry.pack()

last_name_label = tk.Label(window, text="Last Name:")
last_name_label.pack()
last_name_entry = tk.Entry(window)
last_name_entry.pack()

user_name_label = tk.Label(window, text="User Name:")
user_name_label.pack()
user_name_entry = tk.Entry(window)
user_name_entry.pack()

ph_number_label = tk.Label(window, text="Phone Number:")
ph_number_label.pack()
ph_number_entry = tk.Entry(window)
ph_number_entry.pack()

password_label = tk.Label(window, text="Password:")
password_label.pack()
password_entry = tk.Entry(window, show="*")
password_entry.pack()

conform_password_label = tk.Label(window, text="Confirm Password:")
conform_password_label.pack()
conform_password_entry = tk.Entry(window, show="*")
conform_password_entry.pack()

register_button = tk.Button(window, text="Register", command=register)
register_button.pack()

success_label = tk.Label(window, fg="green")
success_label.pack()

error_label = tk.Label(window, fg="red")
error_label.pack()

window.mainloop()





