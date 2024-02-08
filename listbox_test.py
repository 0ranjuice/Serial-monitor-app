import tkinter as tk
from tkinter import ttk


# Function to be called when selection changes
def on_combobox_select(event):
    # Get the selected value
    selected_value = combobox_var.get()
    print(f"Selected: {selected_value}")
    # Update label to show the selected value
    label.config(text=f"You selected: {selected_value}")


# Create the main window
root = tk.Tk()
root.title("ComboBox Example")
root.geometry("300x150")

# Create a StringVar to hold the selected value of the ComboBox
combobox_var = tk.StringVar()

# Create a ComboBox
combobox = ttk.Combobox(root, textvariable=combobox_var)
combobox['values'] = ('Option 1', 'Option 2', 'Option 3', 'Option 4')
combobox.current(0)  # Set the default value to index 0: 'Option 1'
combobox.pack(pady=5)

# Bind the select event
combobox.bind('<<ComboboxSelected>>', on_combobox_select)

# Create a label to display the selected option
label = ttk.Label(root, text="Please select an option")
label.pack(pady=10)

# Start the GUI event loop
root.mainloop()
