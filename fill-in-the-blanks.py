###############################3
#Let's start getting some input from the player!
playername=raw_input("What is your name?")
print "\n"
print "Hello " + playername + "!"
print "\n"
print "Let's see how well you know The Big Bang Theory!"
level=raw_input("Choose which level of difficulty you'd like to play (easy, medium or difficult):")



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

blanks = ["___1___", "___2___", "___3___", "___4___"]




def play_game(level):
    '''This function asks the user to choose a difficulty level.
       If the difficulty level is not in the available_levels, the player will receive an error
       The purpose of this function is to decide which question and which answers should
       be used to run the game '''

    if level in available_levels:
        if level == "easy":
            answers = answers_level_easy
            question = question_level_easy
            play_game_function(question, answers)
            return "You chose easy level!"
        elif level == "medium":
            answers = answers_level_medium
            question = question_level_medium
            play_game_function(question, answers)
            return "You chose medium level!"
        elif level == "difficult":
            answers = answers_level_difficult
            question = question_level_difficult
            play_game_function(question, answers)
            return "You chose difficult level!"
    else:
        return "Sorry, you selected the wrong level!"



print "Fill in the blank the missing word(s) (case sensitive):"
print "\n"

#Testing choose_difficulty_level function
#  print choose_difficulty_level("easy")
#  print choose_difficulty_level("m")



def word_in_pos(playeranswer, answers):
    '''Checks if a word that the player chooses is in the answers to the question'''
    for pos in answers:
        if pos in playeranswer:
            return pos
    return None

# Plays a full game of The Big Bang Theory fill in the blanks quiz.
# A player is prompted to replace blanks in question,
# which appear in blanks with their own words.
def play_game_function(question, answers):
    game_output=[]
    question=question.split()
    blank_index=0
    for word in question:
        replacement =  word_in_pos(word, answers)
        if replacement != None:
            first_answer=word
            game_output.append("_____"+str(blank_index+1)+"_____")
            blank_index=blank_index+1
        else:
            game_output.append(word)
    game_output = " ".join(game_output)
    print game_output
    number_of_questions=blank_index
    number_of_questions_answered=0
    while number_of_questions_answered<len(answers):
        question_answer=raw_input("What word can you substitute for the blank"+" number "+str(number_of_questions_answered+1)+"?")
        if question_answer==answers[number_of_questions_answered]:
            print "Congratulations! Your answer was correct!"
        else:
            question_answer=raw_input("What word can you substitute for the blank"+" number "+str(number_of_questions_answered+1)+"?")
            if question_answer==answers[number_of_questions_answered]:
                print "Congratulations! Your answer was correct!"
            else:
                print "This level might have been too difficult for you!"
        number_of_questions_answered=number_of_questions_answered+1
    print "Thanks for playing!"




print play_game(level)
