import random
import string

def generate_random_password(length=12, required_characters='!&'):  # Requires output to have special usable char
    usable_characters = string.ascii_letters + string.digits + '!,$'
    
    # Ensures at least one required character is in the password
    password = ''.join(random.choice(usable_characters) for _ in range(length - 1))
    password += random.choice(required_characters)
    
    # This shuffles the password to ensure the required character is not always at the end - stregthen password
    password_list = list(password)
    random.shuffle(password_list)
    
    return ''.join(password_list)

def generate_category_password(category):
    categories = {
        'pets': ['dog', 'cat', 'fish', 'bird', 'rabbit'],
        'streets': ['main', 'elm', 'oak', 'maple', 'pine'],
        'colors': ['red', 'blue', 'green', 'yellow', 'purple'],
        'fruits': ['apple', 'banana', 'orange', 'grape', 'kiwi'],
        'sports': ['football', 'basketball', 'soccer', 'tennis', 'golf'],
        # Some categories that people may relate to / favor when creating their own password
        # short list of some common items within each category
    }

    if category in categories:
        selected_category = categories[category]
        
        # Choose one word from the category and randomize capitalization to stregthen the password
        chosen_word = random.choice(selected_category).capitalize()
        
        # Combines the chosen word with a random 3-digit number and either '!' or '&' to further the security
        password_words = [random.choice([char.upper(), char.lower()]) for char in chosen_word]
        password_words.append(str(random.randint(100, 999)))
        password_words.append(random.choice('!&'))
        
        # This shuffles the combined words and characters
        random.shuffle(password_words)
        
        return ''.join(password_words)
    else:
        return "Invalid category"

def generate_user_input_password(user_input):
    if len(user_input) > 10:
        return "Input string exceeds 10 characters."
    # Invalid input
    # Randomize capitalization of the input string - strengthen
    randomized_input = ''.join(random.choice([char.upper(), char.lower()]) for char in user_input)
    
    # Add a random 3-digit number
    randomized_input += str(random.randint(100, 999))
    
    # Ensures the password contains either '!' or '&'
    randomized_input += random.choice('!&')
    
    return randomized_input

def generate_password():
    print("Choose password generation method:")
    print("1. Random Password")
    print("2. Category-based Password")
    print("3. User Input Password")

    choice = input("Enter your choice (1, 2, or 3): ") # allows user to pick generation method

    if choice == '1':
        password_length = int(input("Enter the desired length for the password: "))
        generated_password = generate_random_password(password_length, required_characters='!&') # adds usable special char
        print("Generated Password:", generated_password)

    elif choice == '2':
        print("Choose a category:")
        print("1. Pets")
        print("2. Streets")
        print("3. Colors")
        print("4. Fruits")
        print("5. Sports")
        # The user is able to pick from these common categories

        category_choice = input("Enter your category choice (1, 2, 3, 4, or 5): ")

        if category_choice == '1':
            generated_password = generate_category_password('pets')
        elif category_choice == '2':
            generated_password = generate_category_password('streets')
        elif category_choice == '3':
            generated_password = generate_category_password('colors')
        elif category_choice == '4':
            generated_password = generate_category_password('fruits')
        elif category_choice == '5':
            generated_password = generate_category_password('sports')
        # User input for category

        print("Generated Password:", generated_password) #password will be scrambled and random capitalization

    elif choice == '3':
        user_input = input("Enter a string of up to 10 characters: ")  # User is able to enter string of their choice 
        generated_password = generate_user_input_password(user_input) # Password will contain 3 random digits & usable special char
        print("Generated Password:", generated_password)

    else:
        print("Invalid choice. Please enter a valid option.")  # invalid input

if __name__ == "__main__":  # Gives user chance to rerun script / generate new password
    rerun = 'Y'
    while rerun.upper() == 'Y':
        generate_password()
        rerun = input("Do you want to generate another password? (Y/N): ")
    
    print("Thats a Great Password! Goodbye!")
