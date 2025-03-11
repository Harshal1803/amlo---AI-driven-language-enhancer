from tkinter import Tk, Entry, Text, Button
import ollama
import tkinter as tk
import threading
from pynput import keyboard

def hotkey():
    def on_activate():
        print('Hotkey pressed')
        window.deiconify()
    listener = keyboard.GlobalHotKeys({'<alt>+a': on_activate})
    listener.start()  
threading.Thread(target=hotkey, daemon=True).start()

def enhance_text(text, mode):
    response = ollama.chat(
        model="gemma",
        messages=[{"role": "user", "content": f"{mode}: {text}"}]
    )
    return response["message"]["content"]

def process_text(mode):
    input_text = text_area.get("1.0", "end-1c")  # Get text from upper text area
    if input_text.strip():
        enhanced_text = enhance_text(input_text, mode)
        text_area.delete("1.0", "end")
        text_area.insert("1.0", enhanced_text)

# GUI Setup
window = tk.Tk()
window.title("amlo - Language Enhancer")
window.geometry("500x400")
window.configure(bg="#222")

# Text Area
text_area = tk.Text(window, wrap="word", height=10, width=50, font=("Helvetica", 12))
text_area.place(x=20, y=20, width=460, height=150)

# Custom prompt input
entry_1 = tk.Entry(window, font=("Arial", 12), width=40)
entry_1.place(x=20, y=190, width=360, height=30)

# Buttons for different modes
button_modes = ["Formal", "Funny", "Shorten", "Rephrase"]
x_positions = [20, 140, 260, 380]

for i, mode in enumerate(button_modes):
    btn = tk.Button(
        window,
        text=mode,
        command=lambda m=mode: process_text(m),
        relief="ridge",
        bg="#333",
        fg="white",
        font=("Arial", 10),
        padx=10,
        pady=5
    )
    btn.place(x=x_positions[i], y=230, width=100, height=30)

# Custom prompt button
custom_button = tk.Button(
    window,
    text="Apply Custom Prompt",
    command=lambda: process_text("custom"),
    relief="ridge",
    bg="#444",
    fg="white",
    font=("Arial", 10),
    padx=10,
    pady=5
)
custom_button.place(x=20, y=270, width=460, height=30)

# Run GUI
window.mainloop()
