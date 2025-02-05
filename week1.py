#random username generator

import random
import string

def generate_username(include_numbers=True, include_special_chars=False):
    """Generate a random username."""
    adjectives = ["cool", "swift", "lucky", "mighty",  "happy", "brave", "clever", "witty"]
    nouns = ["flower", "moon", "sun", "eagle", "spirit", "fire","Tiger", "sage", "muse", "nova", "echo", "ghost" "Panther"]
    special_chars = "*!@#$%^&"
    
    #random adjective and noun
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    username = adj + noun
    
    # Add number if user want
    if include_numbers:
        username += ''.join(random.choices(string.digits, k=2))
    
    #Add special character if user want
    if include_special_chars:
        username += random.choice(special_chars)
    
    return username

def save_username_to_file(username, filename="usernames.txt"):
    # Save the generated username to a text file
    with open(filename, "a") as file:
        file.write(username + "\n")

def main():
    
    print("Random Username Generator: ")
    include_numbers = input("Would you like to include numbers? (yes/no): ").strip().lower() == "yes"
    include_special_chars = input("Would you like to include special characters? (yes/no): ").strip().lower() == "yes"
    
    # Generate and display the username
    username = generate_username(include_numbers, include_special_chars)
    print(f"Your unique username: {username}")
    
    # Ask if the user wants to save it to a file
    save_username = input("Would you like to save this username? (yes/no): ").strip().lower()
    if save_username == "yes":
        save_username_to_file(username)
        print("Username saved successfully!")

if __name__ == "__main__":
    main()
