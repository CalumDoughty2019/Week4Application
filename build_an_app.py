import sys

#initialise catalogue
def initialise():
    print("initialising book catalogue.....")
    book1 = ["BX", "Learning Python", "D. Lutz & M. Asher", "O'Reilly", "2004", 17.50, 250]
    book2 = ["BT", "Python in a Nutshell", "A, Martelli", "O'Reilly", "2003", 17.50, 150]
    book3 = ["BY", "Python Programming for the Absolute Beginner", "M. Dawson", "Premier Press", "2003", 13.50, 340]
    book4 = ["BZ", "Dive into Python", "M. Pilgrim", "APress", "2004", 21.50, 185]
    books = {"BX": book1, "BT": book2, "BY": book3, "BZ": book4}
    return books

def is_number(value):
    try:
        var = float(value)
        return True
    except (TypeError, ValueError):
        return False

#list all book codes and titles
def show_all_books(cat):
    print("Showing all books.....")
    for book in cat.values():
        print("%-4s => %-50s" % (book[0], book[1]))

#list all details for one book
def book_detail(cat):
    print("View details of a book.....")
    code = input("Enter a book code: ")
    if code in cat.keys():
        book = cat[code]
        print("Code: ", book[0])
        print("Title: ", book[1])
        print("Author(s): ", book[2])
        print("Publisher: ", book[3])
        print("Year: ", book[4])
        print("Price: ", end=" ")
        print("£%5.2f" % book[5])
        print("Sales: ", book[6])
    else:
        print("Book not found")

#update price for a book
def update_price(cat):
    print("Update the price of a book.....")
    code = input("Enter book code: ")
    if code in cat.keys():
        book = cat[code]
        price = input("New price: ")
        if is_number(price):
            price_value = float(price)
        else:
            price_value = 0.0
            print("Warning: invalid price, set to 0")
        book[5] = price_value
        print("Price of book", code, "is now £", book[5])
    else:
        print("Book not found")


#start main program
catalogue = initialise()
#print greeting
print("Welcome to the book sales program")
print("---------------------------------")
print()
while True:
    #print out the menu
    print("Please select an option :")
    print("1  List all books")
    print("2  View details of a book")
    print("3  Update price")
    print("X  Exit")

    #get the users choice
    choice = input("> ")
    #carry out task
    if choice == '1':
        show_all_books(catalogue)
    elif choice == '2':
        book_detail(catalogue)
    elif choice == '3':
        update_price(catalogue)
    elif choice == 'X':
        print("Bye")
        break
    else:
        print("Invalid choice")
    print()