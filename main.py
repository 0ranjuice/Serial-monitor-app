import tkinter as tk
from tkinter import font
import serial
import serial.tools.list_ports


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        default_font = font.nametofont("TkDefaultFont")
        default_font.configure(family="Helvetica", size=16)

        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)

        self.grid(sticky=tk.N + tk.S + tk.E + tk.W)
        self.initUI()

    def initUI(self):
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.quitBtn = tk.Button(self, text='Quit', command=self.quit)
        self.quitBtn.grid(row=0, column=0, sticky = tk.N + tk.S + tk.E + tk.W)



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
    app.master.title('Serial monitor')
    app.master.minsize(width=500, height=300)
    app.mainloop()
