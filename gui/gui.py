import tkinter as tk

#Function to change the text of the label
def click_me():
        my_label.config(text="No more C :) ")

#Create the graphical user interface with one label and button
root = tk.Tk()
root.title("My first Python GUI")
root.geometry("300x150")        

#Create the label
my_label = tk.Label(root, text="We love Python", font=("Arial", 16))
my_label.pack(pady=20)

#Create the button who calls our function
my_button = tk.Button(root, text="Click me", command=click_me)
my_button.pack(pady=10)

#Function to run the GUI
root.mainloop()
