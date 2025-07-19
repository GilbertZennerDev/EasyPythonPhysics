import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Buttons on Same Height')

frame = ttk.Frame(root, padding=10)
frame.pack(fill='x')

# List of button labels
labels = ["One", "Two", "Three", "Four"]

# Place buttons on the same row (row=0)
for i, label in enumerate(labels):
    btn = ttk.Button(frame, text=label)
    btn.grid(row=0, column=i, padx=8, pady=8, sticky='nsew')
    frame.columnconfigure(i, weight=1)  # expand buttons evenly

root.mainloop()
