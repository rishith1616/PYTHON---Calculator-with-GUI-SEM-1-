import tkinter as tk


def button_click(number):
    """Appends the clicked number or operator to the display."""
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, str(current) + str(number))


def clear_display():
    """Clears the calculator display."""
    display.delete(0, tk.END)


def calculate():
    """Evaluates the mathematical expression in the display."""
    try:
        expression = display.get()
        # eval() evaluates a string as a Python expression (e.g., "2+3" becomes 5)
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception:
        # If the user types something invalid (like "7++3"), show an error
        display.delete(0, tk.END)
        display.insert(0, "Error")


# 1. Initialize the main application window
root = tk.Tk()
root.title("Calculator With GUI")

# 2. Create the display entry box
display = tk.Entry(
    root, width=16, font=("Arial", 24), borderwidth=5, justify="right"
)
# Place the display at the top, spanning across 4 columns
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# 3. Define the buttons in a grid layout (Label, Row, Column)
buttons = [
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("/", 1, 3),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("*", 2, 3),
    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("-", 3, 3),
    ("C", 4, 0),
    ("0", 4, 1),
    ("=", 4, 2),
    ("+", 4, 3),
]

# 4. Loop through the list to create and place the buttons
for text, row, col in buttons:
    if text == "=":
        action = calculate
    elif text == "C":
        action = clear_display
    else:
        # We use a lambda function to pass the specific button text to button_click
        action = lambda t=text: button_click(t)

    btn = tk.Button(
        root, text=text, padx=20, pady=20, font=("Arial", 14), command=action
    )
    btn.grid(row=row, column=col, sticky="nsew")

# 5. Start the application loop (keeps the window open)
root.mainloop()