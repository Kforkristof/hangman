
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
        
    





