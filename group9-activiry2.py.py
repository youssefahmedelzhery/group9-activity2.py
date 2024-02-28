#names
#1 yousef elzhiri
#2 mouhammed al ghawi
#3 khalid abdulkadir

# githup URL https://github.com/youssefahmedelzhery/group9-activity2.py

"""the following code is a calculator that converts between different currencies"""
this part is done by khalid
"""this following function is a constant in our code that gives the convergon values"""
AED_TO_EUR = 0.25
AED_TO_GBP = 0.22
AED_TO_USD = 0.27

"""the following function is converting AED to other currensies"""
def aed_to_eur(amount):
    return amount * AED_TO_EUR

def aed_to_britishPound(amount):
    return amount * AED_TO_GBP

def aed_to_dollar(amount):
    return amount * AED_TO_USD

"""the following function converts other currencies to AED"""
def dollar_to_aed(amount):
    return amount / AED_TO_USD

def britishPound_to_aed(amount):
    return amount / AED_TO_GBP

def eur_to_aed(amount):
    return amount / AED_TO_EUR

this part done by yousef
"""in this following function  we are calculating the total cost after conversion, and we are giving options for the conversion currencies"""
def main():
    while True:
        print('"main menue"')
        print("welcome to currency convertor")
        print("---------------------")
        print("Select a conversion:")
        print("1. Convert AED to other currencies")
        print("2. Convert other currencies to AED")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            print("Which currency do you want to convert AED to?")
            print("1. Euro (EUR)")
            print("2. British Pound (GBP)")
            print("3. US Dollar (USD)")
            print("4. Go back to the main menu")
            sub_choice = input("Enter your choice (1/2/3/4): ")

            if sub_choice == '1':
                amount = float(input("Enter the amount in AED: "))
                result = aed_to_eur(amount)
                print(f"{amount} AED is equal to {result} EUR")
            elif sub_choice == '2':
                amount = float(input("Enter the amount in AED: "))
                result = aed_to_britishPound(amount)
                print(f"{amount} AED is equal to {result} GBP")
            elif sub_choice == '3':
                amount = float(input("Enter the amount in AED: "))
                result = aed_to_dollar(amount)
                print(f"{amount} AED is equal to {result} USD")
            elif sub_choice == '4':
                print("Returning to the main menu...")
            else:
                print("Invalid choice")

        elif choice == '2':
            print("Which currency do you want to convert to AED?")
            print("1. Euro (EUR)")
            print("2. British Pound (GBP)")
            print("3. US Dollar (USD)")
            print("4. Go back to the main menu")
            sub_choice = input("Enter your choice (1/2/3/4): ")

            if sub_choice == '1':
                amount = float(input("Enter the amount: "))
                result = eur_to_aed(amount)
                print(f"{amount} EUR is equal to {result} AED")
            elif sub_choice == '2':
                amount = float(input("Enter the amount: "))
                result = britishPound_to_aed(amount)
                print(f"{amount} GBP is equal to {result} AED")
            elif sub_choice == '3':
                amount = float(input("Enter the amount: "))
                result = dollar_to_aed(amount)
                print(f"{amount} USD is equal to {result} AED")
            elif sub_choice == '4':
                print("Returning to the main menu...")
            else:
                print("Invalid choice")

        elif choice == '3':
            print("Exiting the program...")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
