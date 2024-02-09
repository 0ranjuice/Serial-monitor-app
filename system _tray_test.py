import tkinter as tk
from pystray import Icon, Menu, MenuItem
from PIL import Image


# Function to minimize the window to the system tray
def minimize_to_tray(window):
    window.iconify()  # Minimize the window
    icon = Icon("Tkinter App")  # Create a pystray Icon object

    # Function to restore the window when the tray icon is clicked
    def restore_window(icon, item):
        window.deiconify()  # Restore the window

    # Create a menu with a single item to restore the window
    menu = Menu(MenuItem('Restore', restore_window))

    # Load an icon image (replace 'icon.png' with your own image)
    icon.icon = Image.open("三永科藝logo.ico")

    # Set the menu for the tray icon
    icon.menu = menu

    # Run the system tray icon
    icon.run()


# Create the Tkinter window
root = tk.Tk()
root.title("Tkinter App")

# Add some widgets to the window
label = tk.Label(root, text="This is a Tkinter window")
label.pack(padx=20, pady=20)

# Minimize the window to the system tray when the window is closed
root.protocol("WM_DELETE_WINDOW", lambda: minimize_to_tray(root))

# Start the Tkinter event loop
root.mainloop()
