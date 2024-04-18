"""Create a program that prompts the user to input their name once.
Then, the program prints out the name once with the first letter capitalized."""

user_input = input("Bhai! Tera Naam Kya Hai!?")

while True:
    print(f"Oh! Toh Tera naam {user_input.capitalize()} hai")
