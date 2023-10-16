#1f
passowrd = True
import re
from datetime import datetime

# function to validate username
def is_valid_username(username):
    # check length
    if len(username) < 3 or len(username) > 20:
        return False
    # check characters
    if not re.match("^[a-zA-Z0-9_-]+$", username):
        return False
    
    passowrd = True
  

# function to validate password
def is_valid_password(password):
    # check length
    if len(password) < 6 or len(password) > 20:
        return False
    # check characters
    if not re.match("^[a-zA-Z0-9_-]+$", password):
        return False
    passowrd = True


# function to read user_info.txt and return a dictionary of usernames and passwords
def get_user_info():
    with open("user_info.txt", "r") as f:
        lines = f.readlines()
    user_info = {}
    for line in lines:
        username, password = line.strip().split(",")
        user_info[username] = password
    return user_info

# function to write a new username and password to user_info.txt
def add_user_to_file(username, password):
    with open("user_info.txt", "a") as f:
        f.write(username + "," + password + "\n")


        

# get user info from file
user_info = get_user_info()

    


while True and passowrd == True:
    choice = input("(l)ogin, (r)egister or (q)uit: ")

    if choice == "q":
        break

    elif choice == "r":
        print("Register for an account")
        user_info = get_user_info()
        username = input("Username (case sensitive): ")
        password = input("Password (case sensitive): ")
        if not is_valid_username(username):
            print("Invalid username, registration cancelled")
        if username in user_info:
            print("Duplicate username, registration cancelled")
        else:
            print("Registration successful!")
            add_user_to_file(username, password)

    elif choice == "l":

        print("Log In")
        def user_login(user_info):

            
            
            username = input("Username (case sensitive): ")
            password = input("Password (case sensitive): ")
        
            while username not in user_info or user_info[username] != password:
                print("Incorrect username or password, please try again")

                username = input("Username (case sensitive): ")
                password = input("Password (case sensitive): ")

            else:
                print(f"You have been logged in successfully as {username}")

            return True, username

        
        
        logged_in = False
        while not logged_in:
            logged_in, username = user_login(user_info)
            if not logged_in:
                continue

            while True:
                    
                    import datetime


                    sub_choice = input("(r)ead messages, (s)end a message, (d)elete messages or (l)ogout: ")
                    if sub_choice == "r":
                    
                   
                        def print_messages(username1):
                            with open('messages.txt', 'r') as f:
                                count = 0
                                for line in f:
                                    if username1 in {line.split('|')[0]} and username != {line.split('|')[1]}:
                                        count += 1
                                        print()
                                        print(f"Message #{count} received from {line.split('|')[1]}")
                                        print(f"Time: {line.split('|')[2]}")
                                        print(line.split('|')[3])
                                        print()
        
                                if count == 0:
                                        print(f"No messages found for {username1}")

                        print_messages(username)





                    elif sub_choice == "s":
                        recipient = input("Username of recipient: ")
                        text = input("Type your message: ")


                    # Generate the current time
                        now = datetime.datetime.now()
                        date_and_time = now.strftime("%m/%d/%Y %H:%M:%S")

                    # Create the message string
                        message_string = f"{username}|{date_and_time}|{text}\n"

                    # Write the message to the recipient's message file

                        with open('messages.txt', 'a') as file:
                            file.write(f"{recipient}")
                            file.write('|')
                            file.write(message_string)
                            file.write('\n')
                        

                        print('Message sent!')



                    elif sub_choice == "d":

                      


                        def delete_messages(username1):
                                with open('messages.txt', 'r') as f:
                                    lines = f.readlines()

                                with open('messages.txt', 'w') as f:
                                    for line in lines:
                                        if line[1]==(username1):
                                            f.write(line)

                                print(f"All messages for {username1} have been deleted.")



                            
                        
                        delete_messages(username)

                    elif sub_choice == "l":
                        print(f"Logging out as username {username}")
                        break
                    else:
                        print("Invalid choice")









