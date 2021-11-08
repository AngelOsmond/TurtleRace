import turtle
import time
import random

WIDTH, HEIGHT = 600, 600
NAMES = ['Larry', 'Tiffany', 'Esmeralda', 'Wilhelm', 'The Puch', 'Sylvia', \
         'Ernst', 'Karina', 'Mr. Torty', 'Gilgamesh']

def get_number_of_racers():
    racers = 0

    while True:
        racers = (input("Enter the number of racers(2-10): "))

        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is not numeric... Try again!")
            continue 

        if 2 <= racers <= 10:
            return racers
        else:
            print("It must be a number between 2 and 10!")


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('The Great Turtle Race')

def create_turtles(names):
    turtles = []
    spacingx = WIDTH//(1 + len(names))
    for i, name in enumerate(names):
        racer = turtle.Turtle()
        racer.color("green")
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2+(spacingx*(i+1)),-HEIGHT//2 +50)
        turtles.append(racer)
    return turtles
    
def race(names):
    turtles = create_turtles(names)

    while True:
        for racer in turtles:
            distance = random.randrange(15,35)

            racer.forward(distance)

            x, y = racer.pos()

            if y >= HEIGHT//2 - 20:
                return names[turtles.index(racer)]
    


racers = get_number_of_racers()
init_turtle()

names = NAMES[:racers]

winner = race(names)


turtle.color('green')
style = ('Bookerly', 30, 'bold')
turtle.write("And the winner is " + winner +"!", font=style, align='center')
turtle.hideturtle()
