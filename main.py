import customtkinter as ctk
import serial
import serial.tools.list_ports

ft = ('Helvetica', 18)  # Font

class Application(ctk.CTkFrame):
    def __init__(self, master=None):
        ctk.CTkFrame.__init__(self, master)
        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)

        self.grid(sticky="nsew")
        self.grid_rowconfigure((0,1), weight=1)
        self.grid_columnconfigure((0,2), weight=1)
        self.grid_columnconfigure(1, weight=0)

        # Configure window
        app_width = 600
        app_height = 600
        screenwidth = self.master.winfo_screenwidth()
        screenheight = self.master.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (
            app_width, app_height, (screenwidth - app_width) / 2, (screenheight - app_height) / 2)
        self.master.geometry(alignstr)
        self.master.title('Serial monitor')

        self.initUI()

    def initUI(self):
        # Create a frame to group labels and comboBoxes
        frame_serialPortConfig = ctk.CTkFrame(self, fg_color="transparent")
        frame_serialPortConfig.grid(row=0, column=1, sticky="nsew")
        frame_serialPortConfig.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        frame_serialPortConfig.grid_columnconfigure((0, 1), weight=1)

        print(self.grid_size())

        # Example data for the ComboBoxes
        port_names = ["COM1", "COM2", "COM3"]
        baud_rates = ["9600", "19200", "38400"]
        data_bits = ["7", "8"]
        parity_options = ["None", "Even", "Odd"]
        stop_bits = ["1", "1.5", "2"]

        """Add widgets to frame_serialPortConfig"""
        # Add labels
        label_PortName = ctk.CTkLabel(frame_serialPortConfig, font=ft, text="Port Name : ")
        label_PortName.grid(row=0, column=0)

        label_BaudRate = ctk.CTkLabel(frame_serialPortConfig, font=ft, text="Baud Rate : ")
        label_BaudRate.grid(row=1, column=0)

        Label_DataBits = ctk.CTkLabel(frame_serialPortConfig, font=ft, text="Data Bits : ")
        Label_DataBits.grid(row=2, column=0)

        Label_Parity = ctk.CTkLabel(frame_serialPortConfig, font=ft, text="Parity : ")
        Label_Parity.grid(row=3, column=0)

        Label_StopBits = ctk.CTkLabel(frame_serialPortConfig, font=ft, text="Stop Bits : ")
        Label_StopBits.grid(row=4, column=0)

        # Add comboBoxes
        ComboBox_PortName = ctk.CTkComboBox(frame_serialPortConfig, values=port_names, font=ft)
        ComboBox_PortName.grid(row=0, column=1)

        ComboBox_BaudRate = ctk.CTkComboBox(frame_serialPortConfig, values=baud_rates, font=ft)
        ComboBox_BaudRate.grid(row=1, column=1)

        ComboBox_DataBits = ctk.CTkComboBox(frame_serialPortConfig, values=data_bits, font=ft)
        ComboBox_DataBits.grid(row=2, column=1)

        ComboBox_Parity = ctk.CTkComboBox(frame_serialPortConfig, values=parity_options, font=ft)
        ComboBox_Parity.grid(row=3, column=1)

        ComboBox_StopBits = ctk.CTkComboBox(frame_serialPortConfig, values=stop_bits, font=ft)
        ComboBox_StopBits.grid(row=4, column=1)

"""
        self.quitBtn = ctk.CTkButton(self, text='Quit', border_width=2, command=self.quit)
        self.quitBtn.grid(row=0, column=0, sticky="nsew")

        # 新增按鈕
        self.newBtn1 = ctk.CTkButton(self, text='Button 1', border_width=2, command=self.onNewBtn1Click)
        self.newBtn1.grid(row=1, column=0, sticky="nsew")

        self.newBtn2 = ctk.CTkButton(self, text='Button 2', border_width=2, command=self.onNewBtn2Click)
        self.newBtn2.grid(row=2, column=0, sticky="nsew")

        # Create a Button with a gray border
        gray_border_button = ctk.CTkButton(self, text="Click Me", border_width=2)

        # Pack the Button into the window
        gray_border_button.grid(pady=20, padx=20)

    def onNewBtn1Click(self):
        print("Button 1 clicked")

    def onNewBtn2Click(self):
        print("Button 2 clicked")
    """

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
