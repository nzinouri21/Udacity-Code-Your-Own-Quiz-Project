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


#select_level_of_difficulty()

def show_question(level, position_of_blank=1, number_answered=0):
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
        if check_answer(level, position_of_blank, answer_to_blank):
            if position_of_blank >= total_questions:
                print "Great job! You got all the answers right!"
                display_filled_sentence(level, position_of_blank)
                print "Returning to the beginning of the game"
                start_game()
            print "Good job! You got this question right!"
            display_filled_sentence(level, position_of_blank)
            number_answered=number_answered+1
            position_of_blank=position_of_blank+1
        else:
            print "your answer is wrong. Try again."
            show_question(level, position_of_blank, number_answered)
