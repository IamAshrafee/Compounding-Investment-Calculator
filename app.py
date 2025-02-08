import tkinter as tk
from tkinter import messagebox


def calculate_investment():
    try:
        initial_amount = float(entry_initial.get())
        annual_increase = float(entry_increase.get()) / 100  # Convert % to decimal
        years = int(entry_years.get())

        investment = initial_amount
        result_text = ""

        for year in range(1, years + 1):
            result_text += f"Year {year}: {investment:.2f} BDT per month\n"
            investment *= 1 + annual_increase  # Apply increase

        result_label.config(text=result_text)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")


# Create GUI window
root = tk.Tk()
root.title("Investment Calculator")
root.geometry("400x300")

tk.Label(root, text="Initial Monthly Investment (BDT):").pack()
entry_initial = tk.Entry(root)
entry_initial.pack()


tk.Label(root, text="Annual Increase (%):").pack()
entry_increase = tk.Entry(root)
entry_increase.pack()


tk.Label(root, text="Number of Years:").pack()
entry_years = tk.Entry(root)
entry_years.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate_investment)
calculate_button.pack()

result_label = tk.Label(root, text="", justify="left")
result_label.pack()

root.mainloop()
