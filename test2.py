import tkinter as tk
from tkinter import ttk  # Import the ttk module from tkinter for Combobox
import tkinter.font as tkFont


class App:
    def __init__(self, root):
        # setting title and window size
        root.title("Serial Port Configuration")
        width, height = 600, 500
        screenwidth, screenheight = root.winfo_screenwidth(), root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=True, height=True)

        # Configure root to use half the window for the frame
        root.rowconfigure(0, weight=1)  # Give the frame row weight to take half the space
        root.rowconfigure(1, weight=1)  # Remaining space can be used for other widgets or padding

        ft = tkFont.Font(family='Helvetica', size=10)

        # Create a frame to group labels and comboboxes
        frame = tk.Frame(root)
        frame.grid(row=0, column=0, sticky="ewns", padx=10)
        frame.rowconfigure((0, 1, 2, 3, 4), weight=1)
        print(root.grid_size())

        # Example data for the Comboboxes
        port_names = ["COM1", "COM2", "COM3"]
        baud_rates = ["9600", "19200", "38400"]
        data_bits = ["7", "8"]
        parity_options = ["None", "Even", "Odd"]
        stop_bits = ["1", "1.5", "2"]

        # Add widgets to the frame instead of the root window
        label_PortName = tk.Label(frame, fg="#333333", font=ft, text="Port Name : ")
        label_PortName.grid(row=0, column=0)

        Label_BaudRate = tk.Label(frame, fg="#333333", font=ft, text="Baud Rate : ")
        Label_BaudRate.grid(row=1, column=0)

        Label_DataBits = tk.Label(frame, fg="#333333", font=ft, text="Data Bits : ")
        Label_DataBits.grid(row=2, column=0)

        Label_Parity = tk.Label(frame, fg="#333333", font=ft, text="Parity : ")
        Label_Parity.grid(row=3, column=0)

        Label_StopBits = tk.Label(frame, fg="#333333", font=ft, text="Stop Bits : ")
        Label_StopBits.grid(row=4, column=0)

        # Creating Comboboxes within the frame
        ComboBox_PortName = ttk.Combobox(frame, values=port_names, font=ft)
        ComboBox_PortName.grid(row=0, column=1)

        ComboBox_BaudRate = ttk.Combobox(frame, values=baud_rates, font=ft)
        ComboBox_BaudRate.grid(row=1, column=1)

        ComboBox_DataBits = ttk.Combobox(frame, values=data_bits, font=ft)
        ComboBox_DataBits.grid(row=2, column=1)

        ComboBox_Parity = ttk.Combobox(frame, values=parity_options, font=ft)
        ComboBox_Parity.grid(row=3, column=1)

        ComboBox_StopBits = ttk.Combobox(frame, values=stop_bits, font=ft)
        ComboBox_StopBits.grid(row=4, column=1)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
