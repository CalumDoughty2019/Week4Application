#initialise catalogue
def initialise():
    print("initialising book catalogue.....")
    #list all book codes and titles

#show all books
def show_all_books(cat):
    print("Showing all books.....")

#list all details of  a specific book
def book_detail(cat):
    print("View details of a book.....")

#update price for a book
def update_price(cat):
    print("Update the price of a book.....")


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