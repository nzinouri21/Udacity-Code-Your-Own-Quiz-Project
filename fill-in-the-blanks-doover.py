#Defining the difficulty levels that the player can choose from
available_difficulty_levels = ["easy", "medium", "difficult"]

blanks = ["___1___", "___2___", "___3___", "___4___"]


#The following are the lists containing the words that are the correct answers
#to each level of the game
answers_level_easy  = ["Howard", "Caltech", "The Cheesecake Factory", "India"]
answers_level_medium  = ["Barenaked Ladies", "fourteen billion", "Sheldon", "Soft Kitty"]
answers_level_difficult  = ["Stan Lee", "Friday", "Monday", "Laundry"]

#The following are sentences containing the missing words that the player should
#guess the words
question_level_easy = '''Out of the four guys,  ___1___ is the only one who doesn't have a PhD.
Sheldon and Leonard both work at  ___2___ . In the first few seasons, Penny works at  ___3___ .
Rajesh is originally from ___4___ .'''

question_level_medium = '''___1___ wrote the theme song for the Big Bang Theory show.
A line in the theme song..Fill in the blank : That ___2___ years ago expansion started..wait!
Speaking of songs, ___3___ has a favorite song that culms him down when he is stressed.
And that song is nothing but ___4___ !'''

question_level_difficult = '''Sheldon lost the opportunity to meet ___1___ when he was thrown
to jail after insulting a judge in traffic court. According to the "Sheldonian Calendar",
___2___ night is "Vintage Video Game Night", ___3___ night is "Thai Takeout" night and
Saturday night is of course ___4___ night.'''




def select_level_of_difficulty():
    '''prompts user to select a difficulty level.
    Args:
        None
    Returns:
        level: string, that is a member of available_difficulty_levels list.
    '''
    level = raw_input("Choose which level of difficulty you'd like to play (easy, medium or difficult) or Type 'Q' to quit")
    if level in ["Q","q"]:
        quit()
    else:
        if level in available_difficulty_levels:
            print "you chose  "+ level+"!"
            return level
        else:
            print "Please choose a right input (easy, medium or difficult) "
            select_level_of_difficulty()

def return_questions(level):
    '''retrieves the corresponding question and answer based on selected level.

    Args:
        level: gets the level the player selected.
    Returns:
        question: string for the corresponding level's question.

    '''
    if level in available_difficulty_levels:
        if level == "easy":
            question = question_level_easy
        elif level == "medium":
            question = question_level_medium
        elif level == "difficult":
            question = question_level_difficult
        return question

    else:
        print "You selected a wrong difficulty level!"
#select_level_of_difficulty()

def return_answers(level):
    '''retrieves the corresponding question and answer based on selected level.

    Args:
        level: gets the level the player selected.
    Returns:
        answer: the list of answers for the level selected.
    '''
    if level in available_difficulty_levels:
        if level == "easy":
            answer = answers_level_easy
        elif level == "medium":
            answer = answers_level_medium
        elif level == "difficult":
            answer = answers_level_difficult
        return answer

    else:
        print "You selected a wrong difficulty level!"

def show_question(question, answer, position_of_blank=1, number_answered=0):
    '''validates user response based on the difficulty level selected
    Args:
        level: easy, medium, or difficult
        position_of_blank: position of blanks within sentence, default is first blank
        number_answered: number of blanks already filled, default is zero (no blanks filled)
    Returns:
        None
    '''
    total_questions=4
    while number_answered<=total_questions:
        answer_to_blank=raw_input("What word can you substitute for the blank"+" number "+str(number_answered+1)+"?")
        if check_answer(answer, position_of_blank, answer_to_blank):
            if position_of_blank >= total_questions:
                print "Great job! You got all the answers right!"
                display_filled_sentence(question, answer, position_of_blank)
                print "Returning to the beginning of the game"
                start_game()
            print "Good job! You got this question right!"
            display_filled_sentence(question, answer, position_of_blank)
            number_answered=number_answered+1
            position_of_blank=position_of_blank+1
        else:
            print "your answer is wrong. Try again."
            show_question(level, position_of_blank, number_answered)

def check_answer(answer, blank_index, player_answer):
    '''validates player's response by comparing it to the answers in answer key
    Args:
        answer: correct answer array for either easy, medium, or difficult
        blank_index: position of blanks within sentence,
        player_answer: string, answer provided by the player
    Returns:
        A boolean output to determine whether the response is correct or not
    '''
    return str(player_answer).lower().strip() == answer[blank_index - 1].lower()

def display_filled_sentence(question, answer, position):
    """Displays the sentence as the user fills it in
    Args:
        level : level selected by user
        position : position of blank within sentence
    Returns:
        Does not return anything
    """

    replacement_position = 1
    sentence = question
    while replacement_position <= position:
      question = question.replace('_' + str(replacement_position) + '_', answer[replacement_position - 1])
      replacement_position =replacement_position+1
    print question

def start_game():
    """Prompts user and plays through game
    Args:
        None
    Returns:
        Does not return anything
    """
    # Start game with a prompt to the user
    print("Welcome to the Big Bang Theory fill-in-the-blanks quiz")
    player_name = raw_input("What is your name?")
    print "Hello " + player_name + "!"
    print "Let's see how well you know The Big Bang Theory!"
    while True:
        # Immediately after running the program, user is prompted
        # to select a difficulty level from easy / medium / hard
        level = select_level_of_difficulty()
        answer = return_answers(level)
        question = return_questions(level)
        print question
        show_question(question, answer)

        #start_game() # game starts over
    else:
        quit()

start_game() # game play starts when file is run
