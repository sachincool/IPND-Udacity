# IPND Stage 2 Final Project

quiz1 = '''Okay!! So you chose a easy way out Huh? Damn chickened out before things got real. Anyway, Here's the Quiz you been buzzing about:
The chicken crossed the __1__ .But, It realised that the world is not safe place so it went back to his __2__ .
The chicken knew his destiny would find him one day! There was nothing that can stop his burning potential and eager to reach the end of the __1__ .
Sooner or later the __3__ came and took him away. Define the gender of the chicken? __4__ .
'''
quiz2 = ''' You got guts! I like you kid. But not in that way. a normal lovable way without the police and stuff.
This one is a bit more tricky:-
It's a Treasure burried deep in the blue __1__ in my old home. It's shaped like a Pendrive but don't fall into the __2__ of it's mesmerizing powers.
It is far more powerful than you ever imagine. It contains my secret collection of only god knows what. I was a kid, gimme a break. My mom washed away my __1__ before I could watch the __3__ movie collection.
Anyways long story short Deadpool is __4__ .
'''
quiz3 = ''' Out of all the options you had to show your masculinity and machoness to choose the toughest one ever!!
Good Luck!! you will need it.
Once upon a time, at some distant Galaxy there existed __1__ . He wanted to rule the world and kill half the population of the world. Weird but there were some people who were not onboard with this arrangement.
The Earth called them __2__ . Yippity Yappity they fought, after an hour the fight was over __1__ won the fight. half of the __2__ were dead.
The reason they lost was because they didn't had any __3__ and yeah Star-lord Big reason Damn that son of a planet. I cried at the death of __4__ .
P.s Deadpool Rawkzz
'''
total_no_of_questions = 3
difficulty_level = ["1: Too darn easy", "2: Meh", "3: Only the Mightiest and toughest person would choose this"]
options = ["1", "2", "3"]
answers1 = ["theme park", "shell", "kfc", "404 cannot assume gender"]
answers2 = ["trousers", "trap", "avengers", "otaku"]
answers3 = ["thanos", "avengers", "good luck", "spiderman"]
choice=["Well well well first stage cleared!!\n Input the second Guess: ", "Second hurdle Cleared Order some sushi around\n 3rd Guess: ",\
 "You certainly checked the code, why bother playing by the rules. Go ahead and win it!\nTch: ", \
 "Winner Winner Chicken Dinner!! \n Every one bow to the king\n Game Cleared star the repo if you liked it"]

def ask_difficulty():
    """ Asks the difficulty_level
    choose from 3 options
    else Enter again
    """
    for difficult in difficulty_level:
        print(difficult)
    level = input()
    while level not in options:
        print("dude!! enter one from 1,2,3 \n Don't act smart")
        level = input()
    if level == options[0]:
        call_quiz(quiz1,answers1)
    elif level == options[1]:
        call_quiz(quiz2,answers2)
    else:
        call_quiz(quiz3,answers3)


def call_quiz(quiz,answers):
    """printing the quiz and calling the function `ask_the_damn_questions` from within"""
    print(quiz)
    ask_the_damn_questions(quiz,answers)


def check_answer(ques,usr_input,answer,choice,guess_str):
    """
    checking the first qestion with the appropriate answer
    Input:ques(str), usr_input(str),answer(str)
    Output:Updated ques,usr_input
    """
    if usr_input.lower() == answer:
        ques = ques.replace(choice,answer)
        usr_input = input(ques+"\n\n"+guess_str)
        if choice=="__4__":
            exit()
        return ques,usr_input
    return ques,usr_input


def ask_the_damn_questions(ques,answers):
    """
    Intended Behaviour: Asking the Questions for different quiz levels
    Input: answers (list)
    Output: nothing
    """
    attempts = 3
    attempt = 0
    usr_input = input("there are 4 options you need to fill \n Start with 1st: ")
    while attempt != attempts:
        ques,usr_input=check_answer(ques,usr_input,answers[0],"__1__",choice[0])
        ques,usr_input=check_answer(ques,usr_input,answers[1],"__2__",choice[1])
        ques,usr_input=check_answer(ques,usr_input,answers[2],"__3__",choice[2])
        ques,usr_input=check_answer(ques,usr_input,answers[3],"__4__",choice[3])
        if usr_input not in answers:
            usr_input = input("Wrong Answer you have "+str(attempts)+"tries left\n")
            attempts -= 1
            if attempts == attempt:
                print("Enough tries go back simon!! I meant Game Over!!")
                exit()


def start_game():
    """
    Driver Program
    """
    ask_difficulty()


if __name__ == "__main__":
    start_game()
