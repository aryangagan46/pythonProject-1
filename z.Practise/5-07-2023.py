class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        while True:
            input_username = input("Enter your username: ")
            input_password = input("Enter your password: ")

            if input_username == self.username and input_password == self.password:
                print("Login successful!")
                break
            else:
                print("Invalid username or password. Please try again.")


# Usage:
user = User("myusername", "mypassword")
user.login()
