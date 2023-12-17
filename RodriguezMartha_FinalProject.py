import tkinter as tk
from tkinter import ttk

class restaurantBillApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Bill App")
        self.titleWindow()

#Creates a title screen that shows a start button
    def titleWindow(self):
        self.titleFrame = tk.Frame(self.root)
        tk.Label(self.titleFrame, text="Welcome to Restaurant Bill App").pack(pady=20)
        tk.Button(self.titleFrame, text="Start", command=self.getGuestsScreen).pack()
        self.titleFrame.pack()

#Takes the user to a new window that asks how many people are in the party
    def getGuestsScreen(self):
        self.titleFrame.destroy()

        self.getGuestsFrame = tk.Frame(self.root)
        tk.Label(self.getGuestsFrame, text="Enter the number of guests:").pack(pady=20)
        self.guestsEntry = tk.Entry(self.getGuestsFrame)
        self.guestsEntry.pack(pady=10)
        tk.Button(self.getGuestsFrame, text="Next", command=self.menuScreen).pack()
        self.getGuestsFrame.pack()

#Takes the user to the menu screen which will ask what the 
#guest(s) will be eating based off of how many are in the party.
    def menuScreen(self):
        try:
            guestsEntryValue = self.guestsEntry.get()
            numberOfGuests = int(guestsEntryValue)
            if numberOfGuests <= 0:
                raise ValueError("Number of guests must be a positive integer.")
        except ValueError as e:
            print(f"Error: {e}")
            return
        
        self.getGuestsFrame.destroy()

        self.menuFrame = tk.Frame(self.root)
        tk.Label(self.menuFrame, text="Menu:").pack(pady=20)

        menuItems = {
            "burger": 12.50,
            "pizza": 15.99,
            "spaghetti": 14.50,
            "salad": 8.99,
            "chicken tenders": 11.50,
            "hotdog": 6.50
        }

        self.menuVars = [tk.StringVar() for _ in range(numberOfGuests)]
        for i in range(numberOfGuests):
            tk.Label(self.menuFrame, text=f"Guest {i + 1} Menu:").pack(pady=10)
            entry = ttk.Combobox(self.menuFrame, textvariable=self.menuVars[i], values=list(menuItems.keys()))
            entry.pack(pady=10)

        tk.Button(self.menuFrame, text="Next", command=self.getGratuityScreen).pack(pady=10)
        self.menuFrame.pack()

#Takes the user to the getGratuityScreen which will ask the amount of 
#gratuity the user would like to add to the party's bill
    def getGratuityScreen(self):
        self.menuFrame.destroy()

        self.getGratuityFrame = tk.Frame(self.root)
        tk.Label(self.getGratuityFrame, text="Choose gratuity:").pack(pady=20)

        self.gratuityVar = tk.StringVar()
        gratuityOptions = ["18%", "20%", "22%"]
        ttk.Combobox(self.getGratuityFrame, textvariable=self.gratuityVar, values=gratuityOptions).pack(pady=10)

        tk.Button(self.getGratuityFrame, text="Calculate", command=self.totalScreen).pack(pady=10)

        self.getGratuityFrame.pack()

#Takes the user to the totalScreen which will take the price from every food 
#the guest(s) have chosen, adds sales tax, and also gratuity that was chosen and displays it.
    def totalScreen(self):
        totalScreen = tk.Toplevel(self.root)
        totalScreen.title("Total Screen")

        partyBill = self.guestsEntry.get()

        partyBill = int(self.guestsEntry.get())

        menuItems = {
            "burger": 12.50,
            "pizza": 15.99,
            "spaghetti": 14.50,
            "salad": 8.99,
            "chicken tenders": 11.50,
            "hotdog": 6.50
        }

        partyBill = []

        for i in menuItems in enumerate(self.menuVars, start=1):
            partyBill = menuVars.get()
            price = menuItems.get(partyBill, 0.0)
            partyBill.append((partyBill, price))

        gratuityPercentage = int(self.gratuityVar.get().rstrip("%"))
        gratuityRate = gratuityPercentage / 100

        subtotal = sum(item[1] for item in partyBill)
        tax = 0.07 * subtotal
        gratuity = gratuityRate * subtotal

        totalWithoutTax = subtotal + gratuity
        totalWithTax = totalWithoutTax + tax

        tk.Label(totalScreen, text=f"Total (Before Tax): ${totalWithoutTax:.2f}").pack(pady=10)
        tk.Label(totalScreen, text=f"Total (With Tax): ${totalWithTax:.2f}").pack(pady=10)

        totalEntry = tk.Entry(totalScreen, state="readonly", font=("Helvetica", 14))
        totalEntry.insert(0, f"Total: ${totalWithTax + gratuity:.2f}")
        totalEntry.pack(pady=20)

        tk.Button(totalScreen, text="Exit", command=self.restartProgram).pack()

#Will restart the program and take the user back to the title screen.
    def restartProgram(self):
        self.root.destroy()
        main()

#Initializes the app
def main():
    root = tk.Tk()
    app = restaurantBillApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
