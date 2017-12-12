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
        while level not in available_levels:
            print "Sorry, you selected the wrong level!"
            level=raw_input("Choose which level of difficulty you'd like to play (easy, medium or difficult):")
            play_game(level)




print "Fill in the blank the missing word(s) (case sensitive):"
print "\n"

def word_in_pos(playeranswer, answer):
    '''Checks if a word that the player chooses is in the answers to the question
    Args:
        playeranswer: player's response
        answer: the list of correct answrers
    Returns:
        pos: correct answer
    '''
    for pos in answer:
        if pos in playeranswer:
            return pos
    return None

def check_players_answer(question, answer):
    number_of_questions_answered=0
    num_tries=0
    while number_of_questions_answered<=len(answer):
        player_answer=raw_input("What word can you substitute for the blank"+" number "+str(number_of_questions_answered+1)+"?")
        if player_answer==answer[number_of_questions_answered]:
            print "Congratulations! Your answer was correct!"
            return True
        else:
            while num_tries<=4:
                print "Try again!"
                check_players_answer(question, answer)
                num_tries=num_tries+1





def play_game_function(question, answer):
    '''Plays a full game of The Big Bang Theory fill in the blanks quiz.
       A player is prompted to replace blanks in question,
       which appear in blanks with their own words. '''

    game_output=[]
    question=question.split()
    blank_index=0
    for word in question:
        replacement =  word_in_pos(word, answer)
        if replacement != None:
            first_answer=word
            game_output.append("_____"+str(blank_index+1)+"_____")
            blank_index=blank_index+1
        else:
            game_output.append(word)

    game_output = " ".join(game_output)
    print game_output
    number_of_questions=blank_index
    check_players_answer(question, answer, player_answer)

print play_game(level)
