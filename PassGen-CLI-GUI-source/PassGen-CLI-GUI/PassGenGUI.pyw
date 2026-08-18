import os
import secrets
import time
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

PassGenVers = "v" + "1.8" + "-" + "release"  # DO NOT CHANGE THIS UNLESS FIXING A bug OR A NEW UPDATE
print(f"Loading PassGenGUI Version: {PassGenVers[1:17]}...")
time.sleep(5)
print("PassGenGUI successfully Launched!")
print("Do Not Close The Terminal!")
root = tk.Tk()
root.config(bg="darkgray")
root.title("PasswordGenerator")
root.geometry("300x330")
root.resizable(False, False)
generated_password = None
generated_length = None
generated_timestamp = None
label = tk.Label(root, text=f"PassGen {PassGenVers}\nMade by @tuffgit21 on github", pady=20,bg="darkgray")
label.pack()


def check_input():
    value = entry_box.get().strip()
    if not value:
        messagebox.showwarning("Warning", "The entry box cannot be empty!")
        return False

    try:
        n = int(value)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer!")
        return False

    if n < 15 or n > 30:
        messagebox.showwarning("Warning", "Choose length between 15 and 30 digits")
        return False

    return n


def PassGen_output():
    global generated_password, generated_length, generated_timestamp

    n = check_input()
    if n is False:
        return

    output_box.config(state="normal")
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, "Generating Password...\n")
    output_box.update_idletasks()

    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    symbols = ["!", "@", "#", "$", "&", "*", "_", "^", "+", "."]
    uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "PasswordsGenerated.txt")
    password_chars = []

    for _ in range(n):
        time.sleep(0.5)
        password_chars.append(secrets.choice(alphabet + numbers + symbols + uppercase))

    password = "".join(password_chars)
    timestamp = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())
    generated_password = password
    generated_length = n
    generated_timestamp = timestamp

    with open(file_path, "a", encoding="utf-8") as file:
        file.write(f"\n{password} - {n} digits - {timestamp} - {PassGenVers}\n")

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, f"{password} - {n} digits\n")
    output_box.insert(tk.END,f"{timestamp}")
    output_box.see(tk.END)
    output_box.config(state="disabled")
    label2.pack_forget()
    save_button.pack(pady=10)
    label2.pack()
    return n


def clear_output():
    output_box.config(state="normal")
    output_box.delete("1.0", tk.END)
    output_box.config(state="disabled")
    save_button.pack_forget()
    label2.pack()

def save_passwords():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        initialfile="password.txt",
        filetypes=[("Text files", "*.txt")],
        title="Choose where to save the password"
    )
    if file_path:
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(
                f"{generated_password} - {generated_length} digits - "
                f"{generated_timestamp} - {PassGenVers}"
            )
        messagebox.showinfo("PassGenGUI", f"Password saved to: {file_path}")

entry_label = tk.Label(root, text="Enter a digit between 15 and 30.",bg="darkgray")
entry_label.pack()
entry_box = tk.Entry(root, width=5,bg="lightgray",fg="black")
entry_box.pack(pady=0)
out_label = tk.Label(root,text="Password here.",bg="darkgray")
out_label.pack()
output_box = tk.Text(root, height=5, width=35, state="disabled", wrap="word",bg="lightgray",fg="black")
output_box.pack(pady=0)
button = tk.Button(root, text="Generate", command=PassGen_output, bg="red", fg="white")
button.pack(pady=10)
save_button = tk.Button(root,text="Save",command=save_passwords,bg="blue",fg="white")
label2 = tk.Label(root, text="site: https://tuffgit21.github.io/", pady=20,bg="darkgray")
label2.pack()

root.mainloop()
