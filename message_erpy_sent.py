import random
import tkinter as tk
from tkinter import messagebox

def encrypt_data(data):
    with open("dbms.txt", "w") as f:
        with open("key_no.txt", "w") as kf:
            pkey = 0
            st = bytearray(data, "ascii")
            
            for _ in range(0, 5):
                key = random.randint(10, 99)
                pkey = pkey * 100 + key
                
                for i, v in enumerate(st):
                    st[i] = v ^ key
            
            encrypted_data = st.decode()
            f.write(encrypted_data)
            kf.write(str(pkey))
            f.close()
            kf.close()

    messagebox.showinfo("Encryption Complete", "Your message is encrypted. Now your data is safe.")

def decrypt_data():
    try:
        with open("dbms.txt", "r") as f:
            with open("key_no.txt", "r") as kf:
                encrypted_data = f.read()
                key_str = kf.read()
                f.close()
                kf.close()
                key = int(key_str)
                st = bytearray(encrypted_data, "ascii")
                
                for _ in range(0, 5):
                    for i, v in enumerate(st):
                        st[i] = v ^ (key % 100)
                    key = key // 100

                decrypted_data = st.decode()
                messagebox.showinfo("Decryption Complete", f"Decrypted Data:\n{decrypted_data}")
    except FileNotFoundError:
        messagebox.showwarning("File Not Found", "Encrypted data and key files not found. Please encrypt data first.")

# Create the main window
root = tk.Tk()
root.title("Data Encryption Program")

# Create and place widgets in the window
label = tk.Label(root, text="Enter the data you want to encrypt:")
label.pack(pady=10)

data_entry = tk.Entry(root, width=50)
data_entry.pack(pady=10)

encrypt_button = tk.Button(root, text="Send Message", command=lambda: encrypt_data(data_entry.get()))
encrypt_button.pack(pady=10)

decrypt_button = tk.Button(root, text="Take data", command=decrypt_data)
decrypt_button.pack(pady=10)

root.mainloop()
