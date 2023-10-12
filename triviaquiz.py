import urllib.request  # Handle the url request
import json  # To parse the json string
import random  # Generate random int and shuffle answer order
from datetime import datetime  # To make timestamp for the filename
# pip install (or pip3 on a Mac) module name if module is not already installed


# Using the Open Trivia Database API to generate questions and answers so that it can be made into a quiz
# The APIs, up to 50 questions per category (depending on how many are available)

# General knowledge
gk_easy = "https://opentdb.com/api.php?amount=50&category=9&difficulty=easy&type=multiple"
gk_medium = "https://opentdb.com/api.php?amount=50&category=9&difficulty=medium&type=multiple"
gk_hard = "https://opentdb.com/api.php?amount=50&category=9&difficulty=hard&type=multiple"

# Science & Nature
sci_easy = "https://opentdb.com/api.php?amount=50&category=17&difficulty=easy&type=multiple"
sci_medium = "https://opentdb.com/api.php?amount=50&category=17&difficulty=medium&type=multiple"
sci_hard = "https://opentdb.com/api.php?amount=50&category=17&difficulty=hard&type=multiple"

# Computers
comp_easy = "https://opentdb.com/api.php?amount=34&category=18&difficulty=easy&type=multiple"
comp_medium = "https://opentdb.com/api.php?amount=50&category=18&difficulty=medium&type=multiple"
comp_hard = "https://opentdb.com/api.php?amount=34&category=18&difficulty=hard&type=multiple"

# History
history_easy = "https://opentdb.com/api.php?amount=50&category=23&difficulty=easy&type=multiple"
history_medium = "https://opentdb.com/api.php?amount=50&category=23&difficulty=medium&type=multiple"
history_hard = "https://opentdb.com/api.php?amount=50&category=23&difficulty=hard&type=multiple"

# Television
tv_easy = "https://opentdb.com/api.php?amount=50&category=14&difficulty=easy&type=multiple"
tv_medium = "https://opentdb.com/api.php?amount=50&category=14&difficulty=medium&type=multiple"
tv_hard = "https://opentdb.com/api.php?amount=28&category=14&difficulty=hard&type=multiple"

# Books
books_easy = "https://opentdb.com/api.php?amount=23&category=10&difficulty=easy&type=multiple"
books_medium = "https://opentdb.com/api.php?amount=40&category=10&difficulty=medium&type=multiple"
books_hard = "https://opentdb.com/api.php?amount=25&category=10&difficulty=hard&type=multiple"

# Film
film_easy = "https://opentdb.com/api.php?amount=50&category=11&difficulty=easy&type=multiple"
film_medium = "https://opentdb.com/api.php?amount=50&category=11&difficulty=medium&type=multiple"
film_hard = "https://opentdb.com/api.php?amount=40&category=11&difficulty=hard&type=multiple"

# Geography
geo_easy = "https://opentdb.com/api.php?amount=50&category=22&difficulty=easy&type=multiple"
geo_medium = "https://opentdb.com/api.php?amount=50&category=22&difficulty=medium&type=multiple"
geo_hard = "https://opentdb.com/api.php?amount=50&category=22&difficulty=hard&type=multiple"

# Lists for user input error handling and to match with the assignment in load_choice() function
cat_list = ["gk", "sci", "comp", "history", "tv", "books", "film", "geo"]
diff_list = ["easy", "medium", "hard"]


# Ask the user their name, which category, and which difficulty they would like
def user_setup():
    full_name = input("What is your full name?: ")
    while True:
        cat_choice = input("-------------------------------\nWhich category would you like?"
                           "\n-----------------------------------------------------------------------------------------"
                           "------------------------------------------\n"
                           "You can choose from General Knowledge (GK), Science & Nature (Sci), Computers (Comp), "
                           "History, TV, Books, Film, or Geography (Geo)."
                           "\n-----------------------------------------------------------------------------------------"
                           "------------------------------------------\n"
                           "Category: ").lower()
        try:
            if cat_choice in cat_list:
                break
            else:
                print("Please enter GK, Sci, Comp, History, TV, Books, Film, or Geo.")
                continue
        except:
            pass

    while True:
        diff_choice = input("--------------------------------\nWhich difficulty would you like?"
                            "\nPlease choose easy, medium, or hard: ").lower()
        try:
            if diff_choice in diff_list:
                break
            else:
                print("Invalid choice.")
                continue
        except:
            pass

    return cat_choice, diff_choice, full_name


cat_choice, diff_choice, full_name = user_setup()  # Call the function


# Function to use the user's category and difficulty choice to read the correct API url, load_data and max_index are
# returned, max_index is used for the random int method
def load_choice():
    if cat_choice == "gk":
        if diff_choice == "easy":
            url_data = gk_easy
            max_index = 49
        elif diff_choice == "medium":
            url_data = gk_medium
            max_index = 49
        else:
            url_data = gk_hard
            max_index = 49
    elif cat_choice == "sci":
        if diff_choice == "easy":
            url_data = sci_easy
            max_index = 49
        elif diff_choice == "medium":
            url_data = sci_medium
            max_index = 49
        else:
            url_data = sci_hard
            max_index = 49
    elif cat_choice == "comp":
        if diff_choice == "easy":
            url_data = comp_easy
            max_index = 33
        elif diff_choice == "medium":
            url_data = comp_medium
            max_index = 49
        else:
            url_data = comp_hard
            max_index = 33
    elif cat_choice == "history":
        if diff_choice == "easy":
            url_data = history_easy
            max_index = 49
        elif diff_choice == "medium":
            url_data = history_medium
            max_index = 49
        else:
            url_data = history_hard
            max_index = 49
    elif cat_choice == "tv":
        if diff_choice == "easy":
            url_data = tv_easy
            max_index = 49
        elif diff_choice == "medium":
            url_data = tv_medium
            max_index = 49
        else:
            url_data = tv_hard
            max_index = 27
    elif cat_choice == "books":
        if diff_choice == "easy":
            max_index = 22
            url_data = books_easy
        elif diff_choice == "medium":
            url_data = books_medium
            max_index = 39
        else:
            url_data = books_hard
            max_index = 24
    elif cat_choice == "film":
        if diff_choice == "easy":
            url_data = film_easy
            max_index = 49
        elif diff_choice == "medium":
            url_data = film_medium
            max_index = 49
        else:
            url_data = film_hard
            max_index = 39
    else:  # Geography
        if diff_choice == "easy":
            url_data = geo_easy
            max_index = 49
        elif diff_choice == "medium":
            url_data = geo_medium
            max_index = 49
        else:
            url_data = geo_hard
            max_index = 49

    web_url = urllib.request.urlopen(url_data)  # Request
    if web_url.getcode() == 200:
        data = web_url.read()  # Read data if response code is successful
        load_data = json.loads(data)  # Parse the json string and load into a dictionary
    else:
        print("Received an error from the server, cannot print results", web_url.getcode())  # If response fails

    return load_data, max_index


load_data, max_index = load_choice()   # Call the function


# Takes the user's choices and generates the quiz
def quiz_generator():
    count = 0  # Counter for while loop
    score = 0  # Quiz score
    random_list = []  # List to store the generated ints so can check if any duplicates

    print("\n------------------------\nTime for the questions!\n------------------------\nPlease enter a, b, c, or d.")
    while count < 10:
        r = random.randint(0, max_index)  # Random int range up to the max index of the chosen list
        if r not in random_list:  # Need to avoid duplicates
            random_list.append(r)  # Add random int to list if not already in it
            random_int = random_list[-1]  # Save most recent random int as a variable so can use as the current index

            # Don't like needing to use multiple .replace methods, but found it tricky to do with other methods.
            # Would be better to clean up data in advance (or better yet import it clean) but also ideally only want to
            # clean up the data as it is being used since there is a lot of different options.
            question = load_data["results"][random_int]["question"].replace('&quot;', '"').replace("&#039;", "'").\
                replace("&amp;", "&").replace("&rsquo;", "'").replace("&ldquo;", '"').replace("&rdquo;", '"').replace(
                "&hellip;", "...").replace("&aacute;", "á").replace("&eacute;", "é")
            print(f"\n{count + 1}.", question)  # The question

            # Answers
            a = load_data["results"][random_int]["incorrect_answers"][0]
            b = load_data["results"][random_int]["incorrect_answers"][1]
            c = load_data["results"][random_int]["correct_answer"]
            d = load_data["results"][random_int]["incorrect_answers"][2]
            list_answers = [a, b, c, d]
            # Make answers into a list and shuffle them so that correct answer is not always "c"!
            random.shuffle(list_answers)
            answer = input("Is it a. {}, b. {}, c. {}, or d. {}?: ".format(list_answers[0], list_answers[1],
                                                                           list_answers[2], list_answers[3]).replace(
                "&#039;", "'").replace("&rsquo;", "'").replace("&aacute;", "á").replace("&oacute;", "ó").replace(
                "&shy;", "").replace("&amp;", "&").replace("&lrm;", "").replace("&iacute;", "í")).lower()
            # Replacing characters again, in the string rather than answer variables above because need them to match
            # exactly with if statement below

            # If statement to check if answer was correct, score added if it was
            if answer == "a" and list_answers[0] == load_data["results"][random_int]["correct_answer"]:
                score += 1
                print("That is the correct answer.")
            elif answer == "b" and list_answers[1] == load_data["results"][random_int]["correct_answer"]:
                score += 1
                print("That is the correct answer.")
            elif answer == "c" and list_answers[2] == load_data["results"][random_int]["correct_answer"]:
                score += 1
                print("That is the correct answer.")
            elif answer == "d" and list_answers[3] == load_data["results"][random_int]["correct_answer"]:
                score += 1
                print("That is the correct answer.")
            else:
                print("Sorry the correct answer was {}.".format(c).replace("&#039;", "'").replace(
                    "&rsquo;", "'").replace("&aacute;", "á").replace("&oacute;", "ó").replace("&shy;", "").replace(
                    "&amp;", "&").replace("&lrm;", "").replace("&iacute;", "í"))
            count += 1  # Increase count for while loop
    return score


score = quiz_generator()  # Call the function
print(f"\nYou scored: {score} out of 10.")


# Function to turn full name into initials (for use in the filename)
def get_initials(full_name):
    name_list = full_name.split()
    initials = ""

    for i in range(len(name_list)):
        full_name = name_list[i]
        initials += (full_name[0].upper())
    return initials


initials = get_initials(full_name)  # Call the function


# Function to create a file with the user's results
def file_create():
    timestamp = datetime.now().strftime("%H%M_%d%m%y")
    filename = f"{initials}_quiz_{timestamp}.txt"
    category = load_data["results"][0]["category"]
    difficulty = (load_data["results"][0]["difficulty"]).capitalize()
    results = f"==============\n Quiz results\n==============\nName: {full_name}\nCategory: {category}" \
              f"\nDifficulty: {difficulty}\nScore: {score}/10"
    with open(filename, "w") as quiz_file:
        quiz_file.write(results)
    print(f"Your file has been saved as: {filename}.")


# Ask the user if they want to save their results as a file
user_file = input("Would you like to save your results as a file? (Yes or No): ").lower()
if user_file == "yes" or user_file == "y":
    file_create()  # Call create file function if they say yes
else:
    print("Results have not been saved.")


# Damn extra missing stuff
# &ndash; answers