###############################3
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

available_levels = ["easy", "medium", "difficult"]

#This function asks the user to choose a difficulty level.
#If the difficulty level is not in the available_levels, the player will receive an error
#The purpose of this function is to decide which question and which answers should
#be used to run the game
def choose_difficulty_level(level):
    if level in available_levels:
        if level == "easy":
            answers = answers_level_easy
            question = question_level_easy
            return "You chose easy level!"
        elif level == "medium":
            answers = answers_level_medium
            question = question_level_medium
            return "You chose medium level!"
        elif level == "medium":
            answers = answers_level_difficult
            question = question_level_difficult
            return "You chose difficult level!"
    else:
        return "Sorry, you selected the wrong level!"

#Testing choose_difficulty_level function
#  print choose_difficulty_level("easy")
#  print choose_difficulty_level("m")
