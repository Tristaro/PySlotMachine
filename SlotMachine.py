import tkinter as tk
import random
from tkinter import messagebox

# Define the symbols that will appear on the reels
symbols = ['🍒', '🍋', '🍊', '🍇', '🔔', '⭐']

class SlotMachine:
    def __init__(self, root):
        self.root = root
        self.root.title("Slot Machine")
        self.root.configure(bg='darkgreen')

        self.balance = 100
        self.loan_balance = 0
        self.cost_per_spin = 25
        self.win_reward = 25*100

        # Title Label
        self.title_label = tk.Label(root, text="Slot Machine", font=("Arial", 28, "bold"), bg='darkgreen', fg='gold')
        self.title_label.pack(pady=10)

        self.frame = tk.Frame(root, bg='darkgreen')
        self.frame.pack(pady=20)

        # Balance and Loan Labels
        self.balance_label = tk.Label(self.frame, text=f"Balance: ${self.balance}", font=("Arial", 18), bg='darkgreen', fg='white')
        self.balance_label.grid(row=0, column=0, columnspan=3, pady=5)

        self.loan_label = tk.Label(self.frame, text=f"Loan: ${self.loan_balance}", font=("Arial", 18), bg='darkgreen', fg='red')
        self.loan_label.grid(row=1, column=0, columnspan=3, pady=5)

        # Separator Lines
        self.top_line = tk.Label(self.frame, text="---", font=("Arial", 24, "bold"), bg='darkgreen', fg='white')
        self.top_line.grid(row=2, column=0, columnspan=3)

        # Reels
        self.reels = [tk.Label(self.frame, text="", font=("Arial", 48), bg='white', width=4, height=2, relief='sunken', bd=2) for _ in range(3)]
        for j in range(3):
            self.reels[j].grid(row=3, column=j, padx=20, pady=10)

        self.bottom_line = tk.Label(self.frame, text="---", font=("Arial", 24, "bold"), bg='darkgreen', fg='white')
        self.bottom_line.grid(row=4, column=0, columnspan=3)

        # Spin Button
        self.spin_button = tk.Button(self.frame, text="Spin", command=self.spin, font=("Arial", 18, "bold"), bg='gold', fg='black', relief='raised', bd=4)
        self.spin_button.grid(row=5, column=0, columnspan=3, pady=20)

        # Message Label
        self.message = tk.Label(self.frame, text="", font=("Arial", 18), bg='darkgreen', fg='white')
        self.message.grid(row=6, column=0, columnspan=3, pady=10)

        # Loan Buttons
        self.loan_buttons = []
        self.create_loan_buttons()

    def create_loan_buttons(self):
        loan_amounts = [100, 250, 500, 750, 1000]
        for amount in loan_amounts:
            btn = tk.Button(self.frame, text=f"Loan ${amount}", command=lambda amt=amount: self.take_loan(amt), font=("Arial", 12, "bold"), bg='grey', fg='white', relief='raised', bd=2)
            self.loan_buttons.append(btn)
            btn.grid(row=7, column=loan_amounts.index(amount), padx=5, pady=5)

    def update_balance(self, amount):
        self.balance += amount
        self.balance_label.config(text=f"Balance: ${self.balance}")

    def update_loan_balance(self, amount):
        self.loan_balance += amount
        self.loan_label.config(text=f"Loan: ${self.loan_balance}")

    def spin(self):
        if self.balance < self.cost_per_spin:
            self.show_loan_options()
            return

        self.update_balance(-self.cost_per_spin)

        results = [random.choice(symbols) for _ in range(3)]

        for j in range(3):
            self.reels[j].config(text=results[j])

        if results[0] == results[1] == results[2]:
            self.message.config(text="Congratulations, you win!")
            self.pay_loan_or_add_balance(self.win_reward)
        else:
            self.message.config(text="Better luck next time!")

        if self.balance < 0:
            self.show_loan_options()

    def show_loan_options(self):
        self.message.config(text="Balance below zero. Consider taking a loan.")

    def take_loan(self, amount):
        self.update_balance(amount)
        self.update_loan_balance(amount)
        self.message.config(text=f"Loan of ${amount} taken.")

    def pay_loan_or_add_balance(self, amount):
        if self.loan_balance > 0:
            if amount >= self.loan_balance:
                amount -= self.loan_balance
                self.update_loan_balance(-self.loan_balance)
                self.update_balance(amount)
            else:
                self.update_loan_balance(-amount)
        else:
            self.update_balance(amount)

if __name__ == "__main__":
    root = tk.Tk()
    slot_machine = SlotMachine(root)
    root.mainloop()
