import tkinter as tk

def on_go_clicked():
    checked_boxes = [box_text[i] for i, var in enumerate(checkbox_vars) if var.get() == 1]
    if checked_boxes:
        print("Checked boxes:", ", ".join(checked_boxes))
    else:
        print("No boxes checked")

# Create the main window
root = tk.Tk()
root.title("Checkbox Checker")

# Checkboxes text
box_text = ["alpha", "beta", "gamma", "x", "y", "z", "one", "two", "three"]

# Variable to store checkbox state
checkbox_vars = [tk.IntVar() for _ in range(len(box_text))]

# Create checkboxes
checkboxes = [tk.Checkbutton(root, text=box_text[i], variable=checkbox_vars[i]) for i in range(len(box_text))]

# Arrange checkboxes using grid layout
for i, checkbox in enumerate(checkboxes):
    checkbox.grid(row=i // 3, column=i % 3, sticky="w")

# Create Go button
go_button = tk.Button(root, text="GO", command=on_go_clicked)
go_button.grid(row=len(box_text)//3 + 1, column=1)

# Start the GUI
root.mainloop()
