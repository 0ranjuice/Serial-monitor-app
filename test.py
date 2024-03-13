import customtkinter as tk


def on_checkbox_change(checkbox, var):
    print(f"Checkbox {checkbox} changed. Current value: {var.get()}")


def main():
    root = tk.CTk()

    checkbox_vars = []
    checkboxes = []

    for i in range(1, 5):
        var = tk.BooleanVar(value=True)
        checkbox_var = f"Checkbox {i}"
        checkbox_vars.append((checkbox_var, var))

        checkbox = tk.CTkCheckBox(root, text=f"Checkbox {i}", variable=var)
        checkbox.grid(row=i - 1, column=0, padx=10, pady=5)
        checkboxes.append(checkbox)

        var.trace_add('write', lambda *args, checkbox_var=checkbox_var, var=var: on_checkbox_change(checkbox_var, var))

    root.mainloop()


if __name__ == "__main__":
    main()
