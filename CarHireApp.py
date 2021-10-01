import sys

#initialise catalogue
def initialise():
    print("initialising book catalogue.....")
    car1 = ["J1", "JEEP", "Grand Cherokee", "4 Cylinder", "Leaded", 7, 32.60, True] #True means available
    car2 = ["J2", "JEEP", "Renegade", "4 Cylinder", "Unleaded", 5, 29.99, False]
    car3 = ["R1", "Renault", "Megane", "3 Cylinder", "Diesel", 6, 25.00, True]
    car4 = ["V1", "Vauxhall", "Astra", "2 Cylinder", "Diesel", 5, 18.99, True]
    car5 = ["VO2", "Volkswagen", "Golf", "2 Cylinder", "Leaded", 5, 22.50, False]
    cars = {"J1": car1, "J2": car2, "R1": car3, "V1": car4, "VO2": car5}
    return cars


def show_all_cars(catalogue):
    print("Showing all cars.....")
    for book in catalogue.values():
        print("%-4s => %-50s" % (book[0], book[1]))

def show_all_available_cars(catalogue):
    print("Showing all AVAILABLE cars.....")
    for book in catalogue.values():
        if book[7] == True:
            print("%-4s => %-50s" % (book[0], book[1]))

#list all details for one book
def car_detail(catalogue):
    print("View details of a specific car.....")
    reg = input("Enter a car registration: ")
    if reg in catalogue.keys():
        car = catalogue[reg]
        print("Reg: ", car[0])
        print("Make: ", car[1])
        print("Model: ", car[2])
        print("Engine Size: ", car[3])
        print("Fuel type: ", car[4])
        print("No.seats: ", car[5])
        print("Daily RR: ", end=" ")
        print("£%5.2f" % car[6])
        print("Available: ", car[7])
    else:
        print("Car not found")

def is_number(value):
    try:
        var = float(value)
        return True
    except (TypeError, ValueError):
        return False

#update price for a car
def update_RR(catalogue):
    print("Update the Daily Rental Rate of a car.....")
    reg = input("Enter car reg: ")
    if reg in catalogue.keys():
        car = catalogue[reg]
        price = input("New price: ")
        if is_number(price):
            price_value = float(price)
        else:
            price_value = 0.0
            print("Warning: invalid price, set to 0")
        car[6] = price_value
        print("RR of car", reg, "is now £", car[6])
    else:
        print("Car not found")

def availability(catalogue):
    print("Update the Availability of a car.....")
    reg = input("Enter car reg: ")
    if reg in catalogue.keys():
        car = catalogue[reg]
        print("Current availability = ", car[7])
        switch = input("Would you like this car to be available (y or n): ")
        if switch == 'y':
            car[7] = True
        elif switch == 'n':
            car[7] = False
        else:
            car[7] = False
            print("Warning: invalid input, set to False")
        print("Availability of car", reg, "is now ", car[7])
    else:
        print("Car not found")



#start main program
catalogue = initialise()
#print greeting
print("Welcome to the car hire firm")
print("---------------------------------")
print()
while True:
    #print out the menu
    print("Please select an option :")
    print("1  List all cars")
    print("2  List all available cars")
    print("3  View details of a specific car")
    print("4  Update daily rate")
    print("5  Update availability")
    print("X  Exit")

    #get the users choice
    choice = input("> ")
    #carry out task
    if choice == '1':
        show_all_cars(catalogue)
    elif choice == '2':
        show_all_available_cars(catalogue)
    elif choice == '3':
        car_detail(catalogue)
    elif choice == '4':
        update_RR(catalogue)
    elif choice == '5':
        availability(catalogue)
    elif choice == 'X':
        print("Bye")
        break
    else:
        print("Invalid choice")
    print()