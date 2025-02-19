import tkinter as tk
from tkinter import filedialog, messagebox

# ROT-N Function
def rot_n(text, n):
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base + n) % 26 + base))
        else:
            result.append(char)
    return ''.join(result)

# Encrypt File
def encrypt_file():
    file_path = filedialog.askopenfilename(title="Select a File")
    if not file_path:
        return

    try:
        n = int(shift_entry.get())
        with open(file_path, "r", encoding="utf-8") as file:
            data = file.read()

        encrypted_data = rot_n(data, n)

        enc_file_path = file_path + ".enc"
        with open(enc_file_path, "w", encoding="utf-8") as file:
            file.write(encrypted_data)

        messagebox.showinfo("Success", f"File encrypted and saved as:\n{enc_file_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Decrypt File
def decrypt_file():
    file_path = filedialog.askopenfilename(title="Select Encrypted File")
    if not file_path:
        return

    try:
        n = int(shift_entry.get())
        with open(file_path, "r", encoding="utf-8") as file:
            encrypted_data = file.read()

        decrypted_data = rot_n(encrypted_data, -n)

        dec_file_path = file_path.replace(".enc", "_decrypted.txt")
        with open(dec_file_path, "w", encoding="utf-8") as file:
            file.write(decrypted_data)

        messagebox.showinfo("Success", f"File decrypted and saved as:\n{dec_file_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Resize UI Elements Dynamically
def resize_widgets(event):
    width, height = root.winfo_width(), root.winfo_height()
    font_size = max(12, height // 30)
    button_width = width // 20
    button_height = height // 100

    shift_label.config(font=("Arial", font_size))
    shift_entry.config(font=("Arial", font_size))

    encrypt_button.config(font=("Arial", font_size, "bold"), width=button_width, height=button_height)
    decrypt_button.config(font=("Arial", font_size, "bold"), width=button_width, height=button_height)

# GUI Setup
root = tk.Tk()
root.title("ROT-N File Encryption")
root.geometry("600x400")  # Medium size window
root.minsize(500, 350)  # Minimum size

# Shift Value Input
shift_label = tk.Label(root, text="ROT-N Shift Value:", font=("Arial", 16))
shift_label.pack(pady=10)

shift_entry = tk.Entry(root, font=("Arial", 16))
shift_entry.pack(pady=5)

# Buttons
encrypt_button = tk.Button(root, text="Encrypt File", command=encrypt_file, font=("Arial", 16, "bold"), height=2, width=20)
encrypt_button.pack(pady=10)

decrypt_button = tk.Button(root, text="Decrypt File", command=decrypt_file, font=("Arial", 16, "bold"), height=2, width=20)
decrypt_button.pack(pady=5)

# Bind Resize Event
root.bind("<Configure>", resize_widgets)

# Run GUI
root.mainloop()
