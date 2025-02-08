import tkinter as tk
from tkinter import messagebox

def calculate_investment():
    try:
        initial_amount = float(entry_initial.get())
        annual_increase = float(entry_increase.get()) / 100  # Convert % to decimal
        annual_return = float(entry_return.get()) / 100  # Convert % to decimal
        inflation_rate = float(entry_inflation.get()) / 100  # Convert % to decimal
        years = int(entry_years.get())
        
        investment = initial_amount
        total_amount = 0
        result_text = ""
        
        for year in range(1, years + 1):
            total_amount += investment * 12  # Add yearly investment
            total_amount *= (1 + annual_return)  # Apply returns
            total_before_inflation = total_amount  # Store value before inflation adjustment
            total_amount /= (1 + inflation_rate)  # Adjust for inflation
            
            result_text += (f"Year {year}:\n"
                            f"  Monthly Investment: {investment:.2f} BDT\n"
                            f"  Total (After Return, Before Inflation): {total_before_inflation:.2f} BDT\n"
                            f"  Total (After Inflation): {total_amount:.2f} BDT\n\n")
            investment *= (1 + annual_increase)  # Increase monthly investment for next year
        
        result_label.config(text=result_text)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Create GUI window
root = tk.Tk()
root.title("Investment Calculator")
root.geometry("500x500")

tk.Label(root, text="Initial Monthly Investment (BDT):").pack()
entry_initial = tk.Entry(root)
entry_initial.pack()


tk.Label(root, text="Annual Increase (%):").pack()
entry_increase = tk.Entry(root)
entry_increase.pack()


tk.Label(root, text="Annual Return (%):").pack()
entry_return = tk.Entry(root)
entry_return.pack()


tk.Label(root, text="Inflation Rate (%):").pack()
entry_inflation = tk.Entry(root)
entry_inflation.pack()


tk.Label(root, text="Number of Years:").pack()
entry_years = tk.Entry(root)
entry_years.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate_investment)
calculate_button.pack()

result_label = tk.Label(root, text="", justify="left")
result_label.pack()

root.mainloop()