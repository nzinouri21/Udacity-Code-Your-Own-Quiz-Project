#in-line comment! Starting the game by asking the player's name
#and greeting them!
player_name = raw_input("What is your name?")
print "\n"
print "Hello " + player_name + "!"
print "\n"
print "Let's see how well you know The Big Bang Theory!"

#Defining the difficulty levels that the player can choose from
available_levels = ["easy", "medium", "difficult"]

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


def choose_difficulty_level():
    '''prompts the user to select the difficulty level.
    Returns: a member of the list, available_levels.
    '''
    level=raw_input("Choose which level of difficulty you'd like to play (easy, medium or difficult):")
    while level not in available_levels:
        print "Sorry, you selected the wrong level!"
        level=raw_input("Choose which level of difficulty you'd like to play (easy, medium or difficult):")
    print "you chose" + level + "!"
    return level

def get_question_and_answer(level):
    '''retrieves the corresponding question and answer based on selected level.

    Args:
        level: gets the level the player selected.
    Returns:
        question: string for the corresponding level's question.
        answer: the list of answers for the level selected.
    '''
    if level == "easy":
        answer = answers_level_easy
        question = question_level_easy
    elif level == "medium":
        answer = answers_level_medium
        question = question_level_medium
    elif level == "difficult":
        answer = answers_level_difficult
        question = question_level_difficult
    else:
        print "You selected a wrong difficulty level!"
    return answer, question




#print choose_difficulty_level()
print get_question_and_answer("easy")
