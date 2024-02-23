import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime


class TimestampApp:
    def __init__(self, root):
        self.root = root
        root.title("Real-Time Timestamp Logger")

        # Create a scrolled text widget
        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
        self.text_area.grid(column=0, row=0, padx=10, pady=10)
        self.text_area.config(state='disabled')  # Disable the textbox to prevent user interaction

        # Start the time logging process
        self.update_time()

    def update_time(self):
        # Get the current time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Enable the text area temporarily to insert text
        self.text_area.config(state='normal')

        # Insert the current time at the end of the text area
        self.text_area.insert(tk.END, current_time + '\n')

        # Ensure the last line is always visible
        self.text_area.see(tk.END)

        # Disable the text area again to prevent user interaction
        self.text_area.config(state='disabled')

        # Schedule the update_time method to be called after 1000ms (1 second)
        self.root.after(1000, self.update_time)


if __name__ == "__main__":
    root = tk.Tk()
    app = TimestampApp(root)
    root.mainloop()
