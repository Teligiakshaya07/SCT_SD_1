import tkinter as tk
from tkinter import ttk

def convert_temperature():
    try:
        temp = float(temp_entry.get())
        from_unit = from_combo.get()
        to_unit = to_combo.get()

        if from_unit == to_unit:
            result = temp
        elif from_unit == "Celsius" and to_unit == "Fahrenheit":
            result = (temp * 9/5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = (temp - 32) * 5/9
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            result = temp + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            result = temp - 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            result = (temp - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            result = (temp - 273.15) * 9/5 + 32
        else:
            result_label.config(text="Conversion not supported.")
            return

        result_label.config(text=f"Result: {result:.2f}°{to_unit[0]}")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

# Create main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x300")
root.configure(bg="#6a5acd")

# Title
title_label = tk.Label(root, text="Temperature Converter", font=("Helvetica", 16, "bold"), bg="#6a5acd", fg="white")
title_label.pack(pady=10)

# Dropdowns
frame = tk.Frame(root, bg="#6a5acd")
frame.pack(pady=5)

from_label = tk.Label(frame, text="From:", bg="#6a5acd", fg="white")
from_label.grid(row=0, column=0, padx=5)
from_combo = ttk.Combobox(frame, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly")
from_combo.set("Celsius")
from_combo.grid(row=0, column=1, padx=5)

to_label = tk.Label(frame, text="To:", bg="#6a5acd", fg="white")
to_label.grid(row=0, column=2, padx=5)
to_combo = ttk.Combobox(frame, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly")
to_combo.set("Fahrenheit")
to_combo.grid(row=0, column=3, padx=5)

# Temperature input label
temp_label = tk.Label(root, text="Enter Temperature:", font=("Helvetica", 12), bg="#6a5acd", fg="white")
temp_label.pack(pady=(15, 5))

# Temperature input box
temp_entry = tk.Entry(root, font=("Helvetica", 12))
temp_entry.pack(pady=5)

# Convert button
convert_button = tk.Button(root, text="Convert", bg="green", fg="white", command=convert_temperature)
convert_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="Result:", font=("Helvetica", 12), bg="#6a5acd", fg="white")
result_label.pack(pady=10)

root.mainloop()
