import tkinter as tk
import tkinter.font as tkFont


class App:
    def __init__(self, root):
        # setting title and window size
        root.title("undefined")
        width, height = 600, 500
        screenwidth, screenheight = root.winfo_screenwidth(), root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=True, height=True)

        root.rowconfigure((0, 1, 2, 3, 4), weight=1)

        ft = tkFont.Font(family='Helvetica', size=10)

        # Using grid instead of place
        label_PortName = tk.Label(root, fg="#333333", font=ft, text="Port Name : ")
        label_PortName.grid(row=0, column=0, padx=10, pady=10)

        Label_BaudRate = tk.Label(root, fg="#333333", font=ft, text="Baud Rate : ")
        Label_BaudRate.grid(row=1, column=0, padx=10, pady=10)

        Label_DataBits = tk.Label(root, fg="#333333", font=ft, text="Data Bits : ")
        Label_DataBits.grid(row=2, column=0, padx=10, pady=10)

        Label_Parity = tk.Label(root, fg="#333333", font=ft, text="Parity : ")
        Label_Parity.grid(row=3, column=0, padx=10, pady=10)

        Label_StopBits = tk.Label(root, fg="#333333", font=ft, text="Stop Bits : ")
        Label_StopBits.grid(row=4, column=0, padx=10, pady=10)

        ListBox_PortName = tk.Listbox(root, borderwidth="1px", font=ft, fg="#333333")
        ListBox_PortName.grid(row=0, column=1, padx=10, pady=10)

        ListBox_BaudRate = tk.Listbox(root, borderwidth="1px", font=ft, fg="#333333")
        ListBox_BaudRate.grid(row=1, column=1, padx=10, pady=10)

        ListBox_DataBits = tk.Listbox(root, borderwidth="1px", font=ft, fg="#333333")
        ListBox_DataBits.grid(row=2, column=1, padx=10, pady=10)

        ListBox_Parity = tk.Listbox(root, borderwidth="1px", font=ft, fg="#333333")
        ListBox_Parity.grid(row=3, column=1, padx=10, pady=10)

        ListBox_StopBits = tk.Listbox(root, borderwidth="1px", font=ft, fg="#333333")
        ListBox_StopBits.grid(row=4, column=1, padx=10, pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
