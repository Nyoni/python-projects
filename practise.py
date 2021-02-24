##high_score = {"High Score": 100, "Score": 0}





foo = 1
def func():
    bar = 2
    print(globals().keys()) # prints all variable names in global scope
    print(locals().keys())

func()
