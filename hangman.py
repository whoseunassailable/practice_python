import random
import sqlite3
from tabulate import tabulate

# Secret words for different categories
secret_word_for_animals = ["ant", "baboon", "badger", "bat", "bear", "beaver", "camel", "cat", "clam", "cobra"]
secret_word_for_shapes = ["square", "triangle", "rectangle", "circle", "ellipse", "rhombus", "trapezoid"]
secret_word_for_places = ["Cairo", "London", "Paris", "Baghdad", "Istanbul", "Riyadh"]
secret_word_for_plants = ["rose", "tulip", "sunflower", "daisy", "orchid", "lily", "lavender"]

game_info = [
    ["Easy", "The user will be given the chance to select the list from which the random word will be selected (Animal, Shape, Place). This will make it easier to guess the secret word. Also, the number of trials will be increased from 6 to 8."],
    ["Moderate", "Similar to Easy, the user will be given the chance to select the set from which the random word will be selected (Animal, Plant, Place) but the number of trials will be reduced to 6. The last two graphics will not be used or displayed."],
    ["Hard", "The code will randomly select a set of words. From this set, the code will randomly select a word. The user will have no clue on the secret word. Also, the number of trials will remain at 6."]
]

conn = sqlite3.connect('records.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS records
(id INTEGER PRIMARY KEY AUTOINCREMENT, player_name TEXT, level TEXT, remaining_lives INTEGER)''')

# Function to update record
def update_record(player_name, level, remaining_lives):
    c.execute("SELECT * FROM records WHERE level=? ORDER BY remaining_lives DESC LIMIT 1", (level,))
    existing_record = c.fetchone()
    if existing_record is None or remaining_lives > existing_record[3]:
        c.execute("INSERT INTO records (player_name, level, remaining_lives) VALUES (?, ?, ?)", (player_name, level, remaining_lives))
        conn.commit()

# Function to display Hall of Fame
def display_hall_of_fame():
    print("HALL OF FAME")
    print("Level\tWinner name\tRemaining lives")
    c.execute("SELECT level, player_name, MAX(remaining_lives) FROM records GROUP BY level")
    records = c.fetchall()
    print(tabulate(records, headers=["Level", "Winner Name", "Remaining Lives"], tablefmt="grid"))

# Initialise the game
def initialize_game(word_set, trials):
    word = random.choice(word_set).lower()
    display_word = '_' * len(word)
    print("Guess the word!\n" + display_word)
    return word, display_word, trials

# Choose difficulty and category
def play_game(difficulty_level, category):
    if difficulty_level == 1:
        trials = 8
        print("===== SELECT CATEGORY =====\n1. Animals\n2. Shapes\n3. Places")
        category = int(input("Select the category: "))
        if category == 1:
            word_set = secret_word_for_animals
        elif category == 2:
            word_set = secret_word_for_shapes
        elif category == 3:
            word_set = secret_word_for_places
        else:
            print("Invalid category! Returning to main menu.")
            return

    elif difficulty_level == 2:
        trials = 6
        print("===== SELECT CATEGORY =====\n1. Animals\n2. Plants\n3. Places")
        category = int(input("Select the category: "))
        if category == 1:
            word_set = secret_word_for_animals
        elif category == 2:
            word_set = secret_word_for_plants
        elif category == 3:
            word_set = secret_word_for_places
        else:
            print("Invalid category! Returning to main menu.")
            return

    elif difficulty_level == 3:
        trials = 6
        word_set = random.choice([secret_word_for_animals, secret_word_for_shapes, secret_word_for_places, secret_word_for_plants])

    word, display_word, trials = initialize_game(word_set, trials)

    while trials > 0:
        if display_word == word:
            print(f"Congratulations {category}! You won the game!")
            update_record(category, ["Easy", "Moderate", "Hard"][difficulty_level-1], trials)
            break
        guessed_letter = input("Guess a letter: ").lower()
        if guessed_letter in word:
            print(f"Good guess! The word contains '{guessed_letter}'.")
            for i in range(len(word)):
                if word[i] == guessed_letter:
                    display_word = display_word[:i] + guessed_letter + display_word[i+1:]
            print(display_word)
        else:
            print(f"Oops! The letter '{guessed_letter}' is not in the word.")
            trials -= 1
            print(f"You have {trials} trials left.")

    if trials == 0:
        print(f"Sorry {category}, you lost the game. The word was '{word}'.")

# Main menu
def main():
    print("Hi there! Welcome to HANGMAN.\n")
    name = input("Please enter your name: ")
    print(f"Hi {name}")

    while True:
        print("\n===== MAIN MENU =====\n1. Play the Game\n2. Hall of Fame\n3. About the Game\n4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("\n===== LEVEL SELECTION =====\n1. Easy\n2. Moderate\n3. Hard\n4. Back to Main Menu")
            difficulty = int(input("Select the difficulty level: "))
            if difficulty in [1, 2, 3]:
                play_game(difficulty, name)
            elif difficulty == 4:
                continue # takes you back to the main menu
            else:
                print("Invalid selection, returning to main menu.")
        elif choice == 2:
            display_hall_of_fame()
        elif choice == 3:
            print(tabulate(game_info, headers=["About the Game", "Info"], tablefmt="grid"))
        elif choice == 4:
            print(f"Thanks for playing! Goodbye, {name}.")
            break
        else:
            print("Invalid choice! Please select again.")

# Run the main menu
main()

# Close the database connection
conn.close()
