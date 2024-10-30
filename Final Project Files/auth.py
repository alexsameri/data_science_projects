import getpass
data = {
    "Alex":"sdvjnfjv",
    "Sameri":"dfjmjg"
}
username = input("Enter your username: ")
password = getpass.getpass("Please enter your password: ")
if username in data and data[username] == password:
    print(f"Authentication successful! You are loged in as, {username}")
else:
    print("Authentication failed. Incorrect username or password.")
