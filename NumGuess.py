from random import randint


gen_num = randint(1, 10)

tries = 0
player_score = 100

def welcome():
    player = input("Please enter your name:\t")
    print("Welcome", player.upper(),"to the Number Guessing game \n\n")

def check_tries():
    global player_score
    global tries
    player_score = (10 - tries) * 10
    if tries != 0:
        print("you already guessed ", tries, "times.\n Your score is:", player_score)
    else:



        
    
    def compare_input(*inputs):
            global tries
            global player_score
            tries = 0
            player_score = 100
            while tries < 3:
                tries = tries + 1
                print(tries)
                
                inputs = input("Enter a number between 1 and 10: ")
                int_inputs = int(inputs)
            
                for usr_input in inputs:
                    print("Your guess is {}".format(usr_input)) 
                    if int_inputs == gen_num:
                        print("correct guess")
                        #print("Your score is", player_score)
                        return 
                    else:
                        player_score = player_score - 10
                        print("Guess again")       
            return
        

            
    












   
welcome()       
check_tries()
print("Your score is", player_score)


