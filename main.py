import customtkinter as ctk
import serial
import serial.tools.list_ports
from datetime import datetime
import logging
import os


class Application(ctk.CTkFrame):
    def __init__(self, master=None):
        # 設置logger
        self.logFile = os.getcwd() + "/Log.log"
        logging.basicConfig(filename=self.logFile, level=logging.INFO,
                            format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

        # Log message
        self.log_message = '心跳'

        # Initialize a flag to control the update
        self.update_time_flag = True

        # ctk
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

        # Data for the ComboBoxes
        port_names = list_serial_ports()

        baud_rates = 115200
        data_bits = 8
        parity_options = None
        stop_bits = 1

        """Add widgets to frame_serialPortConfig_l"""
        # Add labels
        label_PortName = ctk.CTkLabel(frame_serialPortConfig_l, font=self.ft, text="埠名 : ")
        label_PortName.grid(row=0, column=0, pady=10)

        # Add comboBoxes
        self.ComboBox_PortName = ctk.CTkComboBox(frame_serialPortConfig_l, values=port_names, font=self.ft)
        self.ComboBox_PortName.grid(row=0, column=1, pady=10)
        self.ComboBox_PortName.set("")

        # Create a frame to group the right of serialPortConfig section (buttons)
        frame_serialPortConfig_r = ctk.CTkFrame(self, fg_color="transparent")
        frame_serialPortConfig_r.grid(row=0, column=2, sticky="nsew")
        frame_serialPortConfig_r.grid_rowconfigure((0, 1, 2, 3), weight=1)

        # Add Connect button
        btn_connect = ctk.CTkButton(frame_serialPortConfig_l, text="連接", font=self.ft,
                                    command=self.btn_connect_clicked)
        btn_connect.grid(row=1, column=0, columnspan=2)

        """Add widgets to frame_serialPortConfig_l"""
        # Add buttons
        btn_start = ctk.CTkButton(frame_serialPortConfig_r, text="開始記錄", font=self.ft,
                                  command=self.btn_start_clicked)
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

        """Top right corner"""
        # Add the "隱藏" button in the top right corner
        btn_hide = ctk.CTkButton(self, text="隱藏", font=self.ft, command=self.minimize_to_tray, width=10)
        btn_hide.place(relx=1.0, rely=0.0, anchor="ne")  # Adjust placement as needed

    def btn_connect_clicked(self):
        # Add functionality to connect to the selected COM port
        selected_port = self.ComboBox_PortName.get()
        if selected_port != "":
            # Perform connection operations
            # Example: Open serial connection to the selected port
            print("Connecting to port:", selected_port)
            # Add your connection code here
        else:
            # No port selected, display an error message or handle accordingly
            print("No port selected. Please select a port before connecting.")

    def btn_start_clicked(self):
        # Set the update flag to True when recording starts
        self.update_time_flag = True
        self.update_time()

    def btn_stop_clicked(self):
        # Set the update flag to False when recording stops
        self.update_time_flag = False

    def btn_clear_clicked(self):
        # Clear all text in the textbox_log
        self.textbox_log.configure(state='normal')  # Enable the textbox for editing
        self.textbox_log.delete('1.0', 'end')  # Delete all text
        self.textbox_log.configure(state='disabled')  # Disable the textbox again

    def btn_look_clicked(self):
        self.build_log_viewer_UI()

    def build_log_viewer_UI(self):
        # Check if a log viewer window is already open
        if hasattr(self, 'child_window') and self.child_window.winfo_exists():
            self.child_window.lift()
            return

        # Create a child window
        self.child_window = ctk.CTkToplevel(self)
        self.child_window.title("Log Viewer")

        # Set the geometry (size and position) of the child window
        self.child_window.geometry(f"{self.app_width}x{self.app_height}")  # Width x Height

        # Date and Time selection widgets
        # You may need to adjust the styling and positioning based on your layout
        label_start_datetime = ctk.CTkLabel(self.child_window, font=self.ft, text="起始日期時間：")
        label_start_datetime.pack(pady=5)

        entry_start_datetime = ctk.CTkEntry(self.child_window, width=190, font=self.ft,
                                            placeholder_text="YYYY-MM-DD HH:MM")
        entry_start_datetime.pack(pady=5)

        label_end_datetime = ctk.CTkLabel(self.child_window, font=self.ft, text="終止日期時間：")
        label_end_datetime.pack(pady=5)

        entry_end_datetime = ctk.CTkEntry(self.child_window, width=190, font=self.ft,
                                          placeholder_text="YYYY-MM-DD HH:MM")
        entry_end_datetime.pack(pady=5)

        # Button to trigger log filtering
        btn_filter_logs = ctk.CTkButton(self.child_window, font=self.ft, text="查詢",
                                        command=lambda: self.filter_logs(entry_start_datetime.get(),
                                                                         entry_end_datetime.get()))
        btn_filter_logs.pack(pady=20)

        # Textbox for displaying filtered logs
        self.textbox_filtered_logs = ctk.CTkTextbox(self.child_window, font=self.ft, width=400, corner_radius=0,
                                                    height=200)
        self.textbox_filtered_logs.pack(pady=20)

    def filter_logs(self, start_datetime_str, end_datetime_str):
        try:
            start_datetime = datetime.strptime(start_datetime_str, "%Y-%m-%d %H:%M")
            end_datetime = datetime.strptime(end_datetime_str, "%Y-%m-%d %H:%M")
        except ValueError:
            # Handle the case where the datetime format is incorrect
            error_message = "日期時間格式錯誤！請使用 YYYY-MM-DD HH:MM 格式."
            # Display the error message
            self.show_error_message(error_message)
            return
        else:
            # If the datetime format is correct, remove the error message label if it exists
            self.clear_error_message()

        # Continue with filtering logs
        filtered_logs = self.filter_logs_by_date_time(start_datetime, end_datetime)

        # Display the filtered logs in the textbox
        self.textbox_filtered_logs.configure(state='normal')
        self.textbox_filtered_logs.delete('1.0', 'end')  # Clear the current contents
        for log in filtered_logs:
            self.textbox_filtered_logs.insert('end', log + '\n')  # Add each filtered log
        self.textbox_filtered_logs.configure(state='disabled')

    def filter_logs_by_date_time(self, start_datetime, end_datetime):
        filtered_logs = []
        # Read logs from the log file
        with open(self.logFile, 'r') as file:
            for line in file:
                # Extract timestamp and log message from each line
                parts = line.strip().split(' ')
                if len(parts) == 3:
                    timestamp_date_str, timestamp_time_str, log_message = parts
                    log_timestamp = datetime.strptime(timestamp_date_str + ' ' + timestamp_time_str,
                                                      "%Y-%m-%d %H:%M:%S")

                    # Check if the log timestamp is within the specified range
                    if start_datetime <= log_timestamp <= end_datetime:
                        filtered_logs.append(line.strip())

        return filtered_logs

    def show_error_message(self, message):
        # Create or update an error message label
        if hasattr(self, 'error_label'):
            self.error_label.configure(text=message)
        else:
            self.error_label = ctk.CTkLabel(self.child_window, font=ctk.CTkFont(family="Microsoft YaHei", size=15),
                                            text=message, text_color="red")
            self.error_label.pack(pady=5)

    def clear_error_message(self):
        # Remove the error message label if it exists
        if hasattr(self, 'error_label'):
            self.error_label.pack_forget()  # Remove the label from the window
            del self.error_label  # Delete the reference to the label

    def update_time(self):
        # Check the update flag before updating the time
        if self.update_time_flag:
            # Get the current time
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Log the heartbeat
            logging.info(self.log_message)

            # Enable the text area temporarily to insert text
            self.textbox_log.configure(state='normal')

            # Insert the current time at the end of the text area
            self.textbox_log.insert('end', current_time + " 心跳" + '\n')

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
