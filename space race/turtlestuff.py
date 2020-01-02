# work on line 54 next, you know what must be done
# Note: The coordinates for the finish line start is 200.0 ,300.0
# imports :)

import random
import turtle
import threading

print("for full screen mode type F, for small screen mode press S")
f = "f"
F = "F"
s = "s"
S = "S"
mode = input("> ")
if mode == 'f' or mode == 'F':
    finishX = -633.0
elif mode == 's' or 'mode' == 'S':
    finishX = 300.0 
score = 0
txt = turtle.Turtle()
txt.color('blue')
txt_style = ('Courier', 30, 'italic')
player_win = False
bot_win = False
# the screen for this game
s = turtle.Screen()
# just a general purpose turtle object to use for backgrounds ect...
main_turtle = turtle.Turtle()
# set the background color for the window to black
s.bgcolor("black")
# create an object for the player
player = turtle.Turtle()

# create an object for the bot
bot = turtle.Turtle()
# the velocity of the player :):):):):):):):):)
player_vel = 25
bot_vel = None
# the object for the amaazing button that lets you move your weird line arrow car thing
move_button = turtle.Turtle()
#set the start position for the player
player.hideturtle()           #make the turtle invisible
player.penup()                #don't draw when turtle moves
player.goto(-200, -200)       #move the turtle to a location
player.pencolor("blue")
player.showturtle()           #make the turtle visible
player.pendown()    


#set the start position for the bot
bot.hideturtle()           #make the turtle invisible
bot.penup()                #don't draw when turtle moves
bot.goto(-200, -100)       #move the turtle to a location
bot.showturtle()           #make the turtle visible
bot.pencolor("red")
bot.pendown()        
# set the color of the move button then draw the move button :):):):):):)
move_button.pencolor("yellow")
move_button.shape("square")
# set position for the txt object
txt.hideturtle()           #make the turtle invisible
txt.penup()                #don't draw when turtle moves
txt.goto(-300, 200)       #move the turtle to a location
txt.showturtle()           #make the turtle visible
txt.pencolor("red")
txt.pendown()       

def bot_move():
    global finishX
    global bot_vel
    bot_vel = random.randint(1, 25)
    bot.forward(bot_vel)
    if bot.xcor() >= finishX and bot.ycor > bot.xcor():
        txt.clear()
        txt.color("red")
        txt.write('you lose, Game Over!', font=txt_style)
# this magnifecent function alllows you to move
def player_move(x, y):
    global finishX
    global player_vel
    global player_win
    global score
    player_vel = random.randint(1, 25)
    score += player_vel
    player.forward(player_vel)
    print(player.xcor())
  
    txt.clear()
    txt.hideturtle()           #make the turtle invisible
    txt.penup()                #don't draw when turtle moves
    txt.goto(finishX, 200)       #move the turtle to a location
    txt.showturtle()           #make the turtle visible
    txt.pencolor("red")
    txt.pendown()     
    
    txt.write("score: " + str(score), font=txt_style)
    
    bot_move()
    
    if player.xcor() >= finishX and player.xcor() > bot.xcor():
        txt.clear()
        txt.color("blue")
        txt.write('you win!', font=txt_style)
        
while True: 
       # makes the player move when the button is pressed
    move_button.onclick(player_move)

