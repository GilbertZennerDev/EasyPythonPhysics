import tkinter as tk
import subprocess as sp
from load_save_text import loadText, saveText
from tkinter import ttk

def handle_load():
    filename = filenameEntry.get()
    if filename:
        content = loadText(filename)
        writtenText.delete('1.0', 'end')
        writtenText.insert('end', content)

def handle_save():
    filename = filenameEntry.get()
    if filename:
        content = writtenText.get('1.0', 'end-1c')
        saveText(filename, content)
        
def handle_run():
    handle_save()
    filename = filenameEntry.get()
    sp.run(["python3", filename])

root = tk.Tk()
root.title("Text Editor")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}+0+0")

filenameEntry = tk.Entry(root)
filenameEntry.pack()

# Make sure writtenText exists before defining the button commands!
writtenText = tk.Text(root, height=50, width=100)
writtenText.pack()

frame = ttk.Frame(root, padding=10)
frame.pack(fill='x')

# Set up the buttons
load_btn = ttk.Button(frame, text="Load", command=handle_load)
save_btn = ttk.Button(frame, text="Save", command=handle_save)
run_btn = ttk.Button(frame, text="Save and Run", command=handle_run)

load_btn.grid(row=0, column=0, padx=8, pady=8, sticky='nsew')
save_btn.grid(row=0, column=1, padx=8, pady=8, sticky='nsew')
run_btn.grid(row=0, column=2, padx=8, pady=8, sticky='nsew')

frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

root.mainloop()
