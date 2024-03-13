import tkinter as tk


def calculate():
  try:
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operator = operator_var.get()
    result = perform_calculation(num1, num2, operator)
    if result is not None:
      result_label.config(text=f"Result: {result}", font=("Arial", 14))  
  except ValueError:
    result_label.config(text="Invalid input. Please enter numbers only.", font=("Arial", 12))


def perform_calculation(num1, num2, operator):
  if operator == "+":
    return num1 + num2
  elif operator == "-":
    return num1 - num2
  elif operator == "*":
    return num1 * num2
  elif operator == "/":
    if num2 == 0:
      return "Error: Division by zero"
    else:
      return num1 / num2
  else:
    return "Invalid operator"


window = tk.Tk()
window.title("Simple Calculator")
window.geometry("400x300") 

entry_num1 = tk.Entry(window, width=15)
entry_num1.grid(row=0, column=0, padx=10, pady=10)
entry_num2 = tk.Entry(window, width=15)
entry_num2.grid(row=0, column=1, padx=10, pady=10)


operator_label = tk.Label(window, text="Operator:", font=("Arial", 12))
operator_label.grid(row=1, column=0, padx=5, pady=5)


operator_var = tk.StringVar()
operator_var.set("+") 

operator_add = tk.Radiobutton(window, text="+", variable=operator_var, value="+")
operator_add.grid(row=1, column=1, padx=5, pady=5)

operator_subtract = tk.Radiobutton(window, text="-", variable=operator_var, value="-")
operator_subtract.grid(row=2, column=1, padx=5, pady=5)

operator_multiply = tk.Radiobutton(window, text="*", variable=operator_var, value="*")
operator_multiply.grid(row=3, column=1, padx=5, pady=5)

operator_divide = tk.Radiobutton(window, text="/", variable=operator_var, value="/")
operator_divide.grid(row=4, column=1, padx=5, pady=5)


calculate_button = tk.Button(window, text="Calculate", command=calculate, width=15)
calculate_button.grid(row=5, columnspan=2, padx=10, pady=10)


result_label = tk.Label(window, text="", font=("Arial", 14))
result_label.grid(row=6, columnspan=2, padx=10, pady=10)


window.mainloop()

