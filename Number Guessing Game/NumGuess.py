
















































































































































































































































































































from random import randint

gen_num = randint(1, 10)
print(gen_num)

class NumGuessing():
    def __init__(self, player, tries, player_score):
        self.highscore = {} 
        self.player = player
        self.tries = tries
        self.player_score = player_score
    
    def welcome(self):    
        self.player = input("Please enter your name:\t")
        print("Welcome", self.player.upper(),"to the Number Guessing game \n\n")
    
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
        
        
num_guess = NumGuessing(" ", 0, 100)
num_guess.welcome()
num_guess.check_tries()
print("Your score is", num_guess.compare_input())
num_guess.high_score()


