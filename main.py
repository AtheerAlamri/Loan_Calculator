from tkinter import *


# Create class
class LoanCalculator:

    # Self is a variable that represents an instance of the object itself
    def __init__(self):
        window = Tk()  # Create application window
        window.title("Loan Calculator")  # Set title to application window
        window.configure(bg="#cdd4d3")  # Set background color to application window

        # Adding Label widgets to application window
        Label(window, font="Helvetica 12 bold", bg="#cdd4d3", text="Annual Interest Rate").grid(row=1, column=1,
                                                                                                sticky=W)
        Label(window, font="Helvetica 12 bold", bg="#cdd4d3", text="Number of Years").grid(row=2, column=1, sticky=W)
        Label(window, font="Helvetica 12 bold", bg="#cdd4d3", text="Loan Amount").grid(row=3, column=1, sticky=W)
        Label(window, font="Helvetica 12 bold", bg="#cdd4d3", fg="#2c2c66", text="Monthly Payment").grid(row=4,
                                                                                                         column=1,
                                                                                                         sticky=W)
        Label(window, font="Helvetica 12 bold", bg="#cdd4d3", fg="#800080", text="Total Payment").grid(row=5, column=1,
                                                                                                       sticky=W)

        # Create objects and add entry functions
        self.annualInterestRateVar = StringVar()
        Entry(window, textvariable=self.annualInterestRateVar, justify=LEFT).grid(row=1, column=2)
        self.numberOfYearsVar = StringVar()
        Entry(window, textvariable=self.numberOfYearsVar, justify=LEFT).grid(row=2, column=2)
        self.loanAmountVar = StringVar()
        Entry(window, textvariable=self.loanAmountVar, justify=LEFT).grid(row=3, column=2)

        self.monthlyPaymentVar = StringVar()
        lblMonthlyPayment = Label(window, font="Helvetica 12 bold", bg="#cdd4d3", textvariable=self.monthlyPaymentVar)
        lblMonthlyPayment.grid(row=4, column=2, sticky=E)
        self.totalPaymentVar = StringVar()
        lblTotalPayment = Label(window, font="Helvetica 12 bold", bg="#cdd4d3", textvariable=self.totalPaymentVar)
        lblTotalPayment.grid(row=5, column=2, sticky=E)

        # Create compute payment and clear buttons, when clicked they will call their respective functions.
        btComputePayment = Button(window, text="Compute Payment", font="Helvetica 12 bold", bg="#58554a", fg="white",
                                  command=self.compute_payment)
        btComputePayment.grid(row=6, column=2, sticky=E)
        btDelete_all = Button(window, text="Clear", font="Helvetica 12 bold", bg="#a52a2a", fg="white",
                              command=self.delete_all)
        btDelete_all.grid(row=6, column=3, padx=25, pady=25, sticky=E)

        window.mainloop()  # Runs the application program

    # Create function to compute total payment
    def compute_payment(self):
        monthlyPayment = self.get_monthly_payment(
            float(self.loanAmountVar.get()),
            float(self.annualInterestRateVar.get()) / 1200,
            int(self.numberOfYearsVar.get())
        )
        self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))

        totalPayment = float(self.monthlyPaymentVar.get()) * 12 * int(self.numberOfYearsVar.get())
        self.totalPaymentVar.set(format(totalPayment, '10.2f'))

    def get_monthly_payment(self, loanAmount, monthlyInterestRate, numberOfYears):
        monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
        return monthlyPayment

    # Function to clear inputs
    def delete_all(self):
        self.annualInterestRateVar.set("")
        self.numberOfYearsVar.set("")
        self.loanAmountVar.set("")
        self.monthlyPaymentVar.set("")
        self.totalPaymentVar.set("")


LoanCalculator()
