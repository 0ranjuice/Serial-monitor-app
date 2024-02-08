import customtkinter as ctk
import serial
import serial.tools.list_ports


class Application(ctk.CTkFrame):
    def __init__(self, master=None):
        ctk.CTkFrame.__init__(self, master)
        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)

        self.grid(sticky="nsew")
        self.grid_rowconfigure((0, 1), weight=1)
        self.grid_columnconfigure((0, 3), weight=1)
        self.grid_columnconfigure((1, 2), weight=1)

        # Configure window
        app_width = 600
        app_height = 600
        screenwidth = self.master.winfo_screenwidth()
        screenheight = self.master.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (
            app_width, app_height, (screenwidth - app_width) / 2, (screenheight - app_height) / 2)
        self.master.geometry(alignstr)
        self.master.title('Serial monitor')

        self.ft = ctk.CTkFont(family="Microsoft YaHei", size=16, weight="bold")  # Font

        self.initUI()

    def initUI(self):
        # Create a frame to group the left serialPortConfig section (labels and comboBoxes)
        frame_serialPortConfig_l = ctk.CTkFrame(self, fg_color="transparent")
        frame_serialPortConfig_l.grid(row=0, column=1, sticky="n")
        frame_serialPortConfig_l.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        frame_serialPortConfig_l.grid_columnconfigure((0, 1), weight=1)

        print(self.grid_size())

        # Example data for the ComboBoxes
        port_names = ["COM1", "COM2", "COM3"]
        baud_rates = ["9600", "19200", "38400"]
        data_bits = ["7", "8"]
        parity_options = ["None", "Even", "Odd"]
        stop_bits = ["1", "1.5", "2"]

        """Add widgets to frame_serialPortConfig_l"""
        # Add labels
        label_PortName = ctk.CTkLabel(frame_serialPortConfig_l, font=self.ft, text="Port Name : ")
        label_PortName.grid(row=0, column=0, pady=10)

        label_BaudRate = ctk.CTkLabel(frame_serialPortConfig_l, font=self.ft, text="Baud Rate : ")
        label_BaudRate.grid(row=1, column=0, pady=10)

        Label_DataBits = ctk.CTkLabel(frame_serialPortConfig_l, font=self.ft, text="Data Bits : ")
        Label_DataBits.grid(row=2, column=0, pady=10)

        Label_Parity = ctk.CTkLabel(frame_serialPortConfig_l, font=self.ft, text="Parity : ")
        Label_Parity.grid(row=3, column=0, pady=10)

        Label_StopBits = ctk.CTkLabel(frame_serialPortConfig_l, font=self.ft, text="Stop Bits : ")
        Label_StopBits.grid(row=4, column=0, pady=10)

        # Add comboBoxes
        ComboBox_PortName = ctk.CTkComboBox(frame_serialPortConfig_l, values=port_names, font=self.ft)
        ComboBox_PortName.grid(row=0, column=1, pady=10)

        ComboBox_BaudRate = ctk.CTkComboBox(frame_serialPortConfig_l, values=baud_rates, font=self.ft)
        ComboBox_BaudRate.grid(row=1, column=1, pady=10)

        ComboBox_DataBits = ctk.CTkComboBox(frame_serialPortConfig_l, values=data_bits, font=self.ft)
        ComboBox_DataBits.grid(row=2, column=1, pady=10)

        ComboBox_Parity = ctk.CTkComboBox(frame_serialPortConfig_l, values=parity_options, font=self.ft)
        ComboBox_Parity.grid(row=3, column=1, pady=10)

        ComboBox_StopBits = ctk.CTkComboBox(frame_serialPortConfig_l, values=stop_bits, font=self.ft)
        ComboBox_StopBits.grid(row=4, column=1, pady=10)

        # Create a frame to group the right serialPortConfig section (buttons)
        frame_serialPortConfig_r = ctk.CTkFrame(self, fg_color="transparent")
        frame_serialPortConfig_r.grid(row=0, column=2, sticky="new")
        frame_serialPortConfig_r.grid_rowconfigure((0, 1, 2, 3), weight=1)

        """Add widgets to frame_serialPortConfig_l"""
        # Add buttons
        btn_start = ctk.CTkButton(frame_serialPortConfig_r, text="開始記錄", font=self.ft, command=self.btn_start_clicked)
        btn_start.grid(row=0, column=0, pady=15)

        btn_stop = ctk.CTkButton(frame_serialPortConfig_r, text="停止記錄", font=self.ft, command=self.btn_stop_clicked)
        btn_stop.grid(row=1, column=0, pady=15)

        btn_clear = ctk.CTkButton(frame_serialPortConfig_r, text="清除", font=self.ft, command=self.btn_clear_clicked)
        btn_clear.grid(row=2, column=0, pady=15)

        btn_look = ctk.CTkButton(frame_serialPortConfig_r, text="查看記錄", font=self.ft, command=self.btn_look_clicked)
        btn_look.grid(row=3, column=0, pady=15)

    def btn_start_clicked(self):
        pass

    def btn_stop_clicked(self):
        pass

    def btn_clear_clicked(self):
        pass

    def btn_look_clicked(self):
        pass


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


if __name__ == '__main__':
    app = Application()
    app.mainloop()
