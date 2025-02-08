import tkinter as tk
from tkinter import messagebox, scrolledtext, filedialog
from num2words import num2words

def format_number(value):
    lakh = 100000
    crore = 10000000
    if value >= crore:
        formatted = f"{value / crore:.2f} crore BDT"
    elif value >= lakh:
        formatted = f"{value / lakh:.2f} lakh BDT"
    else:
        formatted = f"{value:,.2f} BDT"
    return formatted

def calculate_investment():
    try:
        initial_amount = float(entry_initial.get())
        annual_increase = float(entry_increase.get()) / 100
        annual_return = float(entry_return.get()) / 100
        inflation_rate = float(entry_inflation.get()) / 100
        years = int(entry_years.get())
        
        investment = initial_amount
        total_amount = 0
        total_invested = 0
        result_text = ""
        
        for year in range(1, years + 1):
            total_invested += investment * 12
            total_amount += investment * 12
            total_amount *= (1 + annual_return)
            total_before_inflation = total_amount
            total_amount /= (1 + inflation_rate)
            
            result_text += f"Year {year}:\n"
            result_text += f"  Monthly Investment: {format_number(investment)}\n"
            result_text += f"  Total Invested Raw Amount: {format_number(total_invested)}\n"
            result_text += f"  Total (Before Inflation): {format_number(total_before_inflation)}\n"
            result_text += f"  Total (After Inflation): {format_number(total_amount)}\n\n"
            
            investment *= (1 + annual_increase)
        
        result_display.config(state=tk.NORMAL)
        result_display.delete(1.0, tk.END)
        result_display.insert(tk.END, result_text)
        result_display.config(state=tk.DISABLED)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

def reset_fields():
    for entry in entries:
        entry.delete(0, tk.END)
    result_display.config(state=tk.NORMAL)
    result_display.delete(1.0, tk.END)
    result_display.config(state=tk.DISABLED)

def save_results():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[["Text Files", "*.txt"], ["All Files", "*.*"]])
    if file_path:
        with open(file_path, "w") as file:
            file.write(result_display.get(1.0, tk.END))

def toggle_theme():
    current_bg = root.cget("bg")
    new_bg = "#2e2e2e" if current_bg == "#f4f4f4" else "#f4f4f4"
    new_fg = "white" if new_bg == "#2e2e2e" else "black"
    root.configure(bg=new_bg)
    for widget in root.winfo_children():
        if isinstance(widget, tk.Label) or isinstance(widget, tk.Button):
            widget.configure(bg=new_bg, fg=new_fg)

# Create GUI window
root = tk.Tk()
root.title("Investment Calculator")
root.geometry("600x650")
root.configure(bg="#f4f4f4")

# Input fields
fields = [
    ("Initial Monthly Investment (BDT):", "10000"),
    ("Annual Increase (%):", "5"),
    ("Annual Return (%):", "8"),
    ("Inflation Rate (%):", "3"),
    ("Number of Years:", "10")
]

entries = []
for label_text, default in fields:
    tk.Label(root, text=label_text, bg="#f4f4f4", font=("Arial", 12)).pack(pady=2)
    entry = tk.Entry(root, font=("Arial", 12))
    entry.insert(0, default)
    entry.pack(pady=5, ipadx=5, ipady=3)
    entries.append(entry)

entry_initial, entry_increase, entry_return, entry_inflation, entry_years = entries

# Buttons
button_frame = tk.Frame(root, bg="#f4f4f4")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Calculate", command=calculate_investment, bg="#28a745", fg="white", font=("Arial", 12)).pack(side=tk.LEFT, padx=10, ipadx=10)
tk.Button(button_frame, text="Reset", command=reset_fields, bg="#dc3545", fg="white", font=("Arial", 12)).pack(side=tk.LEFT, padx=10, ipadx=10)
tk.Button(button_frame, text="Save Results", command=save_results, bg="#007bff", fg="white", font=("Arial", 12)).pack(side=tk.LEFT, padx=10, ipadx=10)
tk.Button(button_frame, text="Toggle Theme", command=toggle_theme, bg="#6c757d", fg="white", font=("Arial", 12)).pack(side=tk.LEFT, padx=10, ipadx=10)

# Result Display
result_display = scrolledtext.ScrolledText(root, height=15, width=70, state=tk.DISABLED, font=("Courier", 10))
result_display.pack(pady=10)

root.mainloop()