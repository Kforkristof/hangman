
import random


def print_header():
    print("""
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    """)


def print_hangman(file="hangmans.txt", nth_pic=0):
    with open(file, "r") as read_hangman:
        hangamn_body = read_hangman.read()
        hangmans_list = hangamn_body.split("@")
        print(hangmans_list[nth_pic])


def get_random_word(file="capitals.txt"):
    with open(file, "r") as read_capitals:
        capitals = read_capitals.read()
        list_of_capitals = capitals.split(", ")
        random_word = random.choice(list_of_capitals)
        return random_word


"""
abc = ("abcdefghijklmnopqrstuvwxyz")
correct = ("cica")
wrongs = []
wrong_guess = 0


def show_wrong_latters(wrongs):
    print("Fails:" , "\t" , ", ".join(wrongs))

while wrong_guess < 3:
    guess = input(str("Word"))
    if guess not in correct:
        wrong_guess+=1
        if guess in wrongs:
            print("You've already tried this")
        else:    
            wrongs.append(guess)
            show_wrong_latters(wrongs)
"""

def main():
    print_header()
    print_hangman(nth_pic=7)
    get_random_word()


main()
