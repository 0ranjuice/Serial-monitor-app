import tkinter as tk
from tkinter import font
import customtkinter as ctk
import serial
import serial.tools.list_ports


class Application(ctk.CTkFrame):
    def __init__(self, master=None):
        ctk.CTkFrame.__init__(self, master)
        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)

        self.grid(sticky=tk.N + tk.S + tk.E + tk.W)
        self.rowconfigure((0, 1, 2), weight=1)
        self.columnconfigure(0, weight=1)

        # Configure window
        app_width = 600
        app_height = 600
        screenwidth = self.master.winfo_screenwidth()
        screenheight = self.master.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (
            app_width, app_height, (screenwidth - app_width) / 2, (screenheight - app_height) / 2)
        self.master.geometry(alignstr)
        self.master.title('Serial monitor')

        # Font settings
        default_font = font.nametofont("TkDefaultFont")
        default_font.configure(family="Helvetica", size=16)

        self.initUI()

    def initUI(self):
        self.quitBtn = ctk.CTkButton(self, text='Quit', border_width=2, command=self.quit)
        self.quitBtn.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

        # 新增按鈕
        self.newBtn1 = ctk.CTkButton(self, text='Button 1', border_width=2, command=self.onNewBtn1Click)
        self.newBtn1.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

        self.newBtn2 = ctk.CTkButton(self, text='Button 2', border_width=2, command=self.onNewBtn2Click)
        self.newBtn2.grid(row=2, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

        # Create a Button with a gray border
        gray_border_button = ctk.CTkButton(self, text="Click Me", border_width=2)

        # Pack the Button into the window
        gray_border_button.grid(pady=20, padx=20)

    def onNewBtn1Click(self):
        print("Button 1 clicked")

    def onNewBtn2Click(self):
        print("Button 2 clicked")



def list_serial_ports():
    ports = serial.tools.list_ports.comports()
    available_ports = []
    for port, desc, hwid in sorted(ports):
        print(f"{port}: {desc} [HWID: {hwid}]")
        available_ports.append(port)
    return available_ports


# List and print all available COM ports
available_ports = list_serial_ports()
print("Available COM Ports:", available_ports)


def connect_to_serial():
    # code to connect to serial port
    pass


if __name__ == '__main__':
    app = Application()
    app.mainloop()
