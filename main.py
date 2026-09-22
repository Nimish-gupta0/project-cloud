try:
    choice = int(input("Enter your choice (1-3): "))
except ValueError:
    print("Invalid input — please enter an integer.")
else:
    if choice == 1:
        print("You selected pizza.")
    elif choice == 2:
        print("You selected Burger.")
    elif choice == 3:
        print("You selected sandwich.")
    else:
        print("Invalid choice.")

# If the file is run by double-clicking, keep the window open until the user
# presses Enter. When running from a terminal this just waits for Enter.
try:
    input("Press Enter to exit...")
except EOFError:
    pass

