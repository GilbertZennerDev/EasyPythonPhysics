import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from load_save_text import loadText, saveText
from ournorm import *

# ---- Helper Functions ----
def handle_load(event=None):
    filename = filename_var.get().strip()
    if not filename:
        messagebox.showwarning("Missing filename", "Please enter a filename to load.")
        return
    content = loadText(filename)
    writtenText.delete('1.0', 'end')
    writtenText.insert('end', content)
    status_var.set(f"Loaded: {filename}")

def handle_save(event=None):
    filename = filename_var.get().strip()
    if not filename:
        messagebox.showwarning("Missing filename", "Please enter a filename to save.")
        return
    content = writtenText.get('1.0', 'end-1c')
    saveText(filename, content)
    status_var.set(f"Saved: {filename}")

def autocomplete(event=None):
    content = open("./text/printtext.py", "r").read()
    writtenText.insert('end', content)

def checkNorm(event=None):
    content = writtenText.get('1.0', 'end-1c').splitlines()
    if check25lines(content):
        print("25 Lines ok")
    else:
        print("Error: More than 25 Lines")
    if checkEmptyLine(content):
        print("No Empty Lines!")
    else:
        print("Error: Empty Lines!")
    fixWrittenText()

def fixWrittenText(event=None):
    content = writtenText.get('1.0', 'end-1c').splitlines()
    
    fixedcontent = ""
    for line in content:
        fixedcontent += checkFunctionTab(line)
    writtenText.delete('1.0', 'end')
    writtenText.insert('end', fixedcontent)

    fixedcontent = ""
    for line in content:
        fixedcontent += checkTabIdent(line)
    writtenText.delete('1.0', 'end')
    writtenText.insert('end', fixedcontent)
    status_var.set("Norme fixed")
    

def ask_open_file():
    path = filedialog.askopenfilename(defaultextension=".txt")
    if path:
        filename_var.set(path)
        handle_load()

def ask_save_file():
    path = filedialog.asksaveasfilename(defaultextension=".txt")
    if path:
        filename_var.set(path)
        handle_save()

# ---- Main Window Setup ----
root = tk.Tk()
root.title("Tkinter Text Editor")
root.minsize(800, 600)

# --- Style ---
style = ttk.Style(root)
style.theme_use('clam')  # Smoother look on all platforms

# --- Filename and Toolbar ---
toolbar = ttk.Frame(root, padding=(8,4), style='TFrame')
toolbar.pack(side='top', fill='x')

filename_var = tk.StringVar()
filename_entry = ttk.Entry(toolbar, textvariable=filename_var, width=50)
filename_entry.pack(side='left', padx=(0,8))

ttk.Button(
    toolbar, text='Open...', command=ask_open_file
).pack(side='left', padx=3)
ttk.Button(
    toolbar, text='Save As...', command=ask_save_file
).pack(side='left', padx=3)
ttk.Button(
    toolbar, text='Load (Ctrl+O)', command=handle_load
).pack(side='left', padx=3)
ttk.Button(
    toolbar, text='Save (Ctrl+S)', command=handle_save
).pack(side='left', padx=3)
ttk.Button(
    toolbar, text='Complete (Ctrl+A)', command=autocomplete
).pack(side='left', padx=3)
ttk.Button(
    toolbar, text='Norme (Ctrl+R)', command=checkNorm
).pack(side='left', padx=3)

filename_entry.insert(0, "Untitled.py")

# --- Text Editing Area ---
mainframe = ttk.Frame(root, padding=(8,8))
mainframe.pack(fill='both', expand=True)

writtenText = tk.Text(
    mainframe,
    wrap='word',
    font=('Consolas', 13),
    undo=True,
    borderwidth=1,
    relief='flat'
)
writtenText.pack(fill='both', expand=True, side='left')
yscroll = ttk.Scrollbar(mainframe, orient='vertical', command=writtenText.yview)
yscroll.pack(side='right', fill='y')
writtenText['yscrollcommand'] = yscroll.set

# --- Status Bar ---
status_var = tk.StringVar(value="Ready")
status_bar = ttk.Label(root, textvariable=status_var, padding=6, anchor='w', background='#ececec')
status_bar.pack(side='bottom', fill='x')

# --- Keyboard Shortcuts ---
root.bind('<Control-s>', handle_save)
root.bind('<Control-o>', handle_load)
root.bind('<Control-a>', autocomplete)
root.bind('<Control-r>', checkNorm)

# --- Run Application ---
root.mainloop()
