import tkinter as tk
from time import strftime
from tkinter import scrolledtext

def log_time():
    # Get the current time in a human-readable format
    current_time = strftime('%H:%M:%S %p')
    # Insert the current time at the end of the Text widget, followed by a newline
    text_widget.insert(tk.END, current_time + "\n")
    # Scroll to the end of the Text widget to ensure the latest entry is visible
    text_widget.see(tk.END)
    # Schedule the log_time function to be called again after 1000 milliseconds
    root.after(1000, log_time)

root = tk.Tk()
root.title("Real-Time Log")

# Create a scrolled Text widget to display the log
text_widget = scrolledtext.ScrolledText(root, font=('calibri', 12), bg="white", state='disabled')
text_widget.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Initially call the log_time function to start logging
log_time()

root.mainloop()
