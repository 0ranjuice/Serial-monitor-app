import customtkinter as ctk
import serial
import serial.tools.list_ports
from datetime import datetime


class Application(ctk.CTkFrame):
    def __init__(self, master=None):
        ctk.CTkFrame.__init__(self, master)
        self.top = self.winfo_toplevel()
        self.top.rowconfigure(0, weight=1)
        self.top.columnconfigure(0, weight=1)

        self.grid(sticky="nsew")
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_columnconfigure((0, 3), weight=1)
        self.grid_columnconfigure((1, 2), weight=1)

        # Configure window
        self.app_width = 600
        self.app_height = 600
        screenwidth = self.master.winfo_screenwidth()
        screenheight = self.master.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (
            self.app_width, self.app_height, (screenwidth - self.app_width) / 2, (screenheight - self.app_height) / 2)
        self.master.geometry(alignstr)
        self.master.title('Serial monitor')

        self.ft = ctk.CTkFont(family="Microsoft YaHei", size=16, weight="bold")  # Font

        self.initUI()

    def initUI(self):
        # Create a frame to group the left of serialPortConfig section (labels and comboBoxes)
        frame_serialPortConfig_l = ctk.CTkFrame(self, fg_color="transparent")
        frame_serialPortConfig_l.grid(row=0, column=1, sticky="ns")
        frame_serialPortConfig_l.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        frame_serialPortConfig_l.grid_columnconfigure((0, 1), weight=1)

        print(self.grid_size())

        # Example data for the ComboBoxes
        port_names = list_serial_ports()
        baud_rates = 115200
        data_bits = 8
        parity_options = None
        stop_bits = 1

        """Add widgets to frame_serialPortConfig_l"""
        # Add labels
        label_PortName = ctk.CTkLabel(frame_serialPortConfig_l, font=self.ft, text="Port Name : ")
        label_PortName.grid(row=0, column=0, pady=10)

        # Add comboBoxes
        ComboBox_PortName = ctk.CTkComboBox(frame_serialPortConfig_l, values=port_names, font=self.ft)
        ComboBox_PortName.grid(row=0, column=1, pady=10)

        # Create a frame to group the right of serialPortConfig section (buttons)
        frame_serialPortConfig_r = ctk.CTkFrame(self, fg_color="transparent")
        frame_serialPortConfig_r.grid(row=0, column=2, sticky="nsew")
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

        """Add widget to the lower half"""
        self.textbox_log = ctk.CTkTextbox(self, width=400, corner_radius=0)
        self.textbox_log.grid(row=1, column=1, columnspan=2, sticky="nsew")
        self.textbox_log.configure(state="disabled")

        self.textbox_log.configure(state="normal")
        self.textbox_log.insert("end", "Some example text!\n")
        self.textbox_log.configure(state="disabled")

        self.update_time()

        """Top right corner"""
        # Add the "隱藏" button in the top right corner
        btn_hide = ctk.CTkButton(self, text="隱藏", font=self.ft, command=self.minimize_to_tray, width=10)
        btn_hide.place(relx=1.0, rely=0.0, anchor="ne")  # Adjust placement as needed

    def btn_start_clicked(self):
        pass

    def btn_stop_clicked(self):
        pass

    def btn_clear_clicked(self):
        pass

    def btn_look_clicked(self):
        # Create a child window
        self.child_window = ctk.CTkToplevel(self)
        self.child_window.title("Log Lookup")

        # Set the geometry (size and position) of the child window
        self.child_window.geometry(f"{self.app_width}x{self.app_height}")  # Width x Height

        # Date and time entry fields
        date_entry = ctk.CTkEntry(self.child_window, placeholder_text="YYYY-MM-DD")
        date_entry.pack(pady=10)
        time_entry = ctk.CTkEntry(self.child_window, placeholder_text="HH:MM:SS")
        time_entry.pack(pady=10)

        # Search button
        search_btn = ctk.CTkButton(self.child_window, text="Search Logs",
                                   command=lambda: self.search_logs(date_entry.get(), time_entry.get()))
        search_btn.pack(pady=20)

        # Close button
        close_btn = ctk.CTkButton(self.child_window, text="Close Window", command=self.child_window.destroy)
        close_btn.pack(pady=10)

    def search_logs(self, date_str, time_str):
        # Convert date_str and time_str to a datetime object (you might want to add error handling)
        try:
            search_datetime = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M:%S")
            # Here you would call your function to retrieve and display the logs for this datetime
            # For example: self.display_logs_for_datetime(search_datetime)
            print(f"Searching for logs at {search_datetime}")
        except ValueError as e:
            print("Error parsing date/time. Please use the format YYYY-MM-DD for date and HH:MM:SS for time.")
            # You might want to show this error in the GUI instead of printing

    def update_time(self):
        # Get the current time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Enable the text area temporarily to insert text
        self.textbox_log.configure(state='normal')

        # Insert the current time at the end of the text area
        self.textbox_log.insert('end', current_time + '\n')

        # Ensure the last line is always visible
        self.textbox_log.see('end')

        # Disable the text area again to prevent user interaction
        self.textbox_log.configure(state='disabled')

        # Schedule the update_time method to be called after 1000ms (1 second)
        self.top.after(1000, self.update_time)

    def minimize_to_tray(self):
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
