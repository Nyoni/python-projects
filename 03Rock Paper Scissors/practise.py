from tkinter import *
#import tkinter.font as font
#from tkinter.ttk import *
import random

#initialize window
gui = Tk()
gui.geometry('400x400')
gui.resizable(0,0)
gui.title('Rock, Paper or Scissors by Guizer')
gui.config(bg ='#0f3752')


Label(gui, text = 'Rock, Paper ,Scissors' , font='arial 20 bold', background = '#0f3752').pack()



user_take = StringVar()
Label(gui, text = 'choose any one: rock, paper ,scissors' , font='arial 15 bold', background = 'seashell2').place(x = 20,y=70)
Entry(gui, font = 'arial 15', textvariable = user_take , background = 'antiquewhite2').place(x=90 , y = 130)



#computer choice
comp_pick = random.randint(1,3)
if comp_pick == 1:
    comp_pick = 'rock'
elif comp_pick ==2:
    comp_pick = 'paper'
else:
    comp_pick = 'scissors'
    



##function to play
Result = StringVar()

def play():
    user_pick = user_take.get()
    if user_pick == comp_pick:
        Result.set('tie,you both select same')
    elif user_pick == 'rock' and comp_pick == 'paper':
        Result.set('you loose,computer select paper')
    elif user_pick == 'rock' and comp_pick == 'scissors':
        Result.set('you win,computer select scissors')
    elif user_pick == 'paper' and comp_pick == 'scissors':
        Result.set('you loose,computer select scissors')
    elif user_pick == 'paper' and comp_pick == 'rock':
        Result.set('you win,computer select rock')
    elif user_pick == 'scissors' and comp_pick == 'rock':
        Result.set('you loose,computer select rock')
    elif user_pick == 'scissors' and comp_pick == 'paper':
        Result.set('you win ,computer select paper')
    else:
        Result.set('invalid: choose any one -- rock, paper, scissors')
    
        
    
##fun to reset
def Reset():
    Result.set("") 
    user_take.set("")

##fun to exit
def Exit():
    gui.destroy()



###### button
Entry(gui, font = 'arial 10 bold', textvariable = Result, background ='antiquewhite2',width = 50,).place(x=25, y = 250)

Button(gui, font = 'arial 13 bold', text = 'PLAY'  ,padx =5, background ='seashell4' ,command = play).place(x=150,y=190)

Button(gui, font = 'arial 13 bold', text = 'RESET'  ,padx =5, background ='seashell4' ,command = Reset).place(x=70,y=310)

Button(gui, font = 'arial 13 bold', text = 'EXIT'  ,padx =5, background ='seashell4' ,command = Exit).place(x=230,y=310)

gui.mainloop()