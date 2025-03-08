def while_password():
    password = 'secret'
    user_input = ''

    while user_input != password:
        user_input = input("Enter password: ")
    
    print("Access granded!")

while_password()