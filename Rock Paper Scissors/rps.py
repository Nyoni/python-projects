import random



class Rps():

    def __init__(self, player, tries, player_score, ui):
        self.highscore = {} 
        self.player = player
        self.tries = tries
        self.player_score = player_score
        self.comp_choice = random.choice(['rock', 'paper', 'scissors'])
        self.ui = ui

    def welcome(self):    
        self.player = input("Please enter your name:\t")
        print("Welcome", self.player.upper(),"to the Rock Pape Scissors game \n\n")

    def high_score(self):
        self.highscore[self.player] = self.player_score
        for key in self.highscore:
            print(key, self.highscore[key])

    def check_tries(self):
        self.player_score = (10 - self.tries) * 10
        if self.tries != 0:
            print("you already guessed ", self.tries, "times.\n Your score", self.player, "is:", self.player_score)
            
        else:
            print("Go on")
            return



    def valid_input(self, prompt, type_=None, min_=None, max_=None, range_=None):
        if min_ is not None and max_ is not None and max_ < min_:
            raise ValueError("min_ must be less than or equal to max_.")
        while True:
            self.ui = input(prompt)
            if type_ is not None:
                try:
                    self.ui = type_(self.ui)
                except ValueError:
                    print("Input type must be {0}.".format(type_.__name__))
                    continue
            if max_ is not None and self.ui > max_:
                print("Input must be less than or equal to {0}.".format(max_))
            elif min_ is not None and self.ui < min_:
                print("Input must be greater than or equal to {0}.".format(min_))
            elif range_ is not None and self.ui not in range_:
                if isinstance(range_, range):
                    template = "Input must be between {0.start} and {0.stop}."
                    print(template.format(range_))
                else:
                    template = "Input must be {0}."
                    if len(range_) == 1:
                        print(template.format(*range_))
                    else:
                        expected = " or ".join((
                            ", ".join(str(x) for x in range_[:-1]),
                            str(range_[-1])
                        ))
                        print(template.format(expected))
            else:
                return self.ui         
            
                       
    def random_func(self): 
    
        print("Computer chooses: " + self.comp_choice)



    def result(self, answer):
        if answer == self.comp_choice:
            print(" DRAW ")
        elif answer == 'rock' or 'r' and self.comp_choice == 'scissors' or 's':
            print(" YOU WIN ")
        elif answer == 'paper' or 'p' and self.comp_choice == 'scissors' or 's':
            print("I WIN") 
        elif answer == 'scissors' or 's' and self.comp_choice == 'rock' or 'r':
            print("I WIN")        
        elif answer == 'paper' or 'p' and self.comp_choice == 'rock' or 'r':
            print("YOU WIN")
        elif answer == 'rock' or 'r' and self.comp_choice == 'paper' or 'p':
            print("I WIN")            
        elif answer == 'scissors' or 's' and self.comp_choice == 'paper' or 'p':
            print("YOU WIN")  

    def compare_input(self, *inputs):
        while self.tries < 3:
            self.tries = self.tries + 1
            print(self.tries)

            inputs = input("Enter a number between 1 and 10: ")
            int_inputs = int(inputs)

            for usr_input in inputs:
                print("Your guess is {}".format(usr_input)) 
                if int_inputs == gen_num:
                    print("Correct guess")       #print("Your score is", player_score)
                    return self.player_score
                
                else:
                    self.player_score = self.player_score - 10
                    print("Guess again", self.player_score)                  
        
        return self.player_score


rps_game = Rps("", 0, 100, "")
rps_game.welcome()
rps_game.check_tries()


answer = rps_game.valid_input("Rock Paper or Scissors: \n", str.lower, range_ =['rock', 'r', 'paper', 'p', 'scissors', 's'])
rps_game.random_func()
rps_game.result(answer)
#print("Your score is", rps_game.compare_input())
rps_game.high_score()
#############################################
