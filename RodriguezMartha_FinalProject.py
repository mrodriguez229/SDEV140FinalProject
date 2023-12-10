def billCalculator(items):
    #Shows the menu of items and the price that corresponds and will add them to a bill
    menu = {
        'burger': 10.99,
        'chicken wings': 12.50,
        'spaghetti': 9.99,
        'steak': 14.99,
        'pizza': 8.99,
        'salad': 5.99,
        'soda': 1.99,
        'water': 0.99,
        'lemonade': 2.50
    }

    #Calculate the subtotal
    subtotal = sum(menu[item] for item in items)

    #Calculate the tax
    taxRate = 0.07
    tax = subtotal * taxRate
    return subtotal + tax

def main():
    #Get the number of people in the party
    numberOfPeople = int(input("How many people are in the party? "))

    #Initialize an empty list to store the items chosen by each person
    partyTab = []

    # Loop through each person in the party
    for person in range(1, numberOfPeople + 1):
        print(f"\nPerson {person}:")
        personItems = []

        # Ask what they will be eating
        while True:
            item = input("What will you be eating. If you are done ordering type 'done'? ").lower()
            if item == 'done':
                break
            elif item in menu:
                personItems.append(item)
            else:
                print("Invalid item. Please choose from the menu.")

        # Add the person's items to the overall list
        partyTab.extend(personItems)

    # Calculate the bill
    total = billCalculator(partyTab)

    # Ask for gratuity percentage
    gratuityPercentage = float(input("Enter gratuity percentage (18%, 20%, or 22%): "))
    gratuity = total * (gratuityPercentage / 100)

    # Calculate the final total
    finalTotal = total + gratuity

    # Display the results
    print("\nSummary:")
    print(f"Subtotal: ${total:.2f}")
    print(f"Gratuity ({gratuity_percentage}%): ${gratuity:.2f}")
    print(f"Total: ${finalTotal:.2f}")


if __name__ == "__main__":
    main()