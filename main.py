import tkinter as tk
import requests

class CurrencyConverter:
    def __init__(self, window):
        self.window = window
        self.window.title("Simple Currency Converter")

        self.amount_label = tk.Label(window, text="Amount:")
        self.amount_label.pack()
        self.amount_entry = tk.Entry(window)
        self.amount_entry.pack()

        self.from_currency_label = tk.Label(window, text="From Currency:")
        self.from_currency_label.pack()
        self.from_currency_entry = tk.Entry(window)
        self.from_currency_entry.pack()

        self.to_currency_label = tk.Label(window, text="To Currency:")
        self.to_currency_label.pack()
        self.to_currency_entry = tk.Entry(window)
        self.to_currency_entry.pack()

        self.convert_button = tk.Button(window, text="Convert Currency", command=self.convert_currency)
        self.convert_button.pack()

        self.result_label = tk.Label(window, text="Result:")
        self.result_label.pack()

    def convert_currency(self):
        amount = float(self.amount_entry.get())
        from_currency = self.from_currency_entry.get().upper()
        to_currency = self.to_currency_entry.get().upper()

        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        response = requests.get(url)
        data = response.json()

        if to_currency in data["rates"]:
            rate = data["rates"][to_currency]
            result = amount * rate
            self.result_label.config(text=f"Result: {result:.2f} {to_currency}")
        else:
            self.result_label.config(text="Invalid currency.")

# Create the main window
window = tk.Tk()

# Create an instance of the CurrencyConverter class
currency_converter = CurrencyConverter(window)

# Start the main loop
window.mainloop()
