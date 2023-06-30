import tkinter as tk
from tkinter import messagebox

# Es Projekt vo Blerian und Ömer

# Die Caesar-Funktion fürd Verschlüsselig
def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            encrypted_text += char
    return encrypted_text

# Die Caesar-Funktion fürd Entschlüsselig
def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# Die XOR-Funktion fürd Verschlüsselig
def xor_encrypt(text, key):
    encrypted_text = ""
    for i in range(len(text)):
        encrypted_text += chr(ord(text[i]) ^ ord(key[i % len(key)]))
    return encrypted_text

# Die XOR-Funktion fürd Entschlüsselig
def xor_decrypt(text, key):
    return xor_encrypt(text, key)

# Die Vigenere-Funktion fürd Verschlüsselig
def vigenere_encrypt(text, key):
    encrypted_text = ""
    for i in range(len(text)):
        if text[i].isalpha():
            ascii_offset = ord('A') if text[i].isupper() else ord('a')
            key_shift = ord(key[i % len(key)].upper()) - ord('A')
            encrypted_text += chr((ord(text[i]) - ascii_offset + key_shift) % 26 + ascii_offset)
        else:
            encrypted_text += text[i]
    return encrypted_text

# Die Vigenere-Funktion fürd Entschlüsselig
def vigenere_decrypt(text, key):
    decrypted_text = ""
    for i in range(len(text)):
        if text[i].isalpha():
            ascii_offset = ord('A') if text[i].isupper() else ord('a')
            key_shift = ord(key[i % len(key)].upper()) - ord('A')
            decrypted_text += chr((ord(text[i]) - ascii_offset - key_shift) % 26 + ascii_offset)
        else:
            decrypted_text += text[i]
    return decrypted_text

# Die Funktion fürd Verschlüsselig vom Text
def encrypt_text():
    selected_method = method_var.get()
    input_text = input_text_entry.get("1.0", tk.END).strip()
    input_key = key_entry.get().strip()

    if not input_text:
        messagebox.showerror("Fehler", "Bitte gib einen Text ein.")
        return

    if selected_method == "Caesar":
        if not input_key.isdigit():
            messagebox.showerror("Fehler", "Der Schlüssel muss eine positive ganze Zahl sein.")
            return
        shift = int(input_key)
        encrypted_text = caesar_encrypt(input_text, shift)
    elif selected_method == "XOR":
        if not input_key:
            messagebox.showerror("Fehler", "Bitte gib einen Schlüssel ein.")
            return
        encrypted_text = xor_encrypt(input_text, input_key)
    elif selected_method == "Vigenère":
        if not input_key.isalpha():
            messagebox.showerror("Fehler", "Der Schlüssel muss aus Buchstaben bestehen.")
            return
        encrypted_text = vigenere_encrypt(input_text, input_key)
    else:
        messagebox.showerror("Fehler", "Bitte wähle eine Verschlüsselungsmethode aus.")
        return

    output_text_entry.delete("1.0", tk.END)
    output_text_entry.insert(tk.END, encrypted_text)

# Die Funktion fürd Entschlüsselig vom Text
def decrypt_text():
    selected_method = method_var.get()
    input_text = input_text_entry.get("1.0", tk.END).strip()
    input_key = key_entry.get().strip()

    if not input_text:
        messagebox.showerror("Fehler", "Bitte gib einen Text ein.")
        return

    if selected_method == "Caesar":
        if not input_key.isdigit():
            messagebox.showerror("Fehler", "Der Schlüssel muss eine positive ganze Zahl sein.")
            return
        shift = int(input_key)
        decrypted_text = caesar_decrypt(input_text, shift)
    elif selected_method == "XOR":
        if not input_key:
            messagebox.showerror("Fehler", "Bitte gib einen Schlüssel ein.")
            return
        decrypted_text = xor_decrypt(input_text, input_key)
    elif selected_method == "Vigenère":
        if not input_key.isalpha():
            messagebox.showerror("Fehler", "Der Schlüssel muss aus Buchstaben bestehen.")
            return
        decrypted_text = vigenere_decrypt(input_text, input_key)
    else:
        messagebox.showerror("Fehler", "Bitte wähle eine Verschlüsselungsmethode aus.")
        return

    output_text_entry.delete("1.0", tk.END)
    output_text_entry.insert(tk.END, decrypted_text)

# Erstelle vom Tkinter-Fenster
window = tk.Tk()
window.title("Verschlüsselungstool")
window.geometry("600x400")
window.resizable(False, False)

# Methodeuswahl fürd Verschlüsselig
method_label = tk.Label(window, text="Wähle eine Verschlüsselungsmethode:")
method_label.pack()

method_var = tk.StringVar()
method_var.set("Caesar")  # Standardmodus

method_option_menu = tk.OptionMenu(window, method_var, "Caesar", "XOR", "Vigenère")
method_option_menu.pack()

# Ihgabe
input_label = tk.Label(window, text="Eingabetext:")
input_label.pack()

input_text_entry = tk.Text(window, height=4, width=50)
input_text_entry.pack()

# Schlüssel
key_label = tk.Label(window, text="Verschlüsselungsschlüssel:")
key_label.pack()

key_entry = tk.Entry(window)
key_entry.pack()

# Usgabetext
output_label = tk.Label(window, text="Ergebnis:")
output_label.pack()

output_text_entry = tk.Text(window, height=4, width=50)
output_text_entry.pack()

# Verschlüsselig und Entschlüsselig
encrypt_button = tk.Button(window, text="Verschlüsseln", command=encrypt_text, width=20, height=2)
encrypt_button.pack(pady=10)

decrypt_button = tk.Button(window, text="Entschlüsseln", command=decrypt_text, width=20, height=2)
decrypt_button.pack()

# Zum Starte vo Tkinter
window.mainloop()
