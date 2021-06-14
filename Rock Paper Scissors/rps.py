import random





def random_func(): 
    comp_choice = random.choice(['rock', 'paper', 'scissors'])
    print("Computer chooses: " + comp_choice)

def valid_input(prompt, type_=None, min_=None, max_=None, range_=None):
    if min_ is not None and max_ is not None and max_ < min_:
        raise ValueError("min_ must be less than or equal to max_.")
    while True:
        ui = input(prompt)
        if type_ is not None:
            try:
                ui = type_(ui)
            except ValueError:
                print("Input type must be {0}.".format(type_.__name__))
                continue
        if max_ is not None and ui > max_:
            print("Input must be less than or equal to {0}.".format(max_))
        elif min_ is not None and ui < min_:
            print("Input must be greater than or equal to {0}.".format(min_))
        elif range_ is not None and ui not in range_:
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
            return ui

def result():
    if answer == comp_choice:
        print(" DRAW ")
    elif answer == 'rock' or 'r' and comp_choice == 'scissors' or 's':
        print(" YOU WIN ")
    elif answer == 'paper' or 'p' and comp_choice == 'scissors' or 's':
        print("I WIN") 
    elif answer == 'scissors' or 's' and comp_choice == 'rock' or 'r':
        print("I WIN")        
    elif answer == 'paper' or 'p' and comp_choice == 'rock' or 'r':
        print("YOU WIN")
    elif answer == 'rock' or 'r' and comp_choice == 'paper' or 'p':
        print("I WIN")            
    elif answer == 'scissors' or 's' and comp_choice == 'paper' or 'p':
        print("YOU WIN")  





answer = valid_input("[R]ock, [P]aper, [S]cissors: \n", str.lower, range_ =['rock', 'r', 'paper', 'p', 'scissors', 's'])
random_func()
result()
#############################################
