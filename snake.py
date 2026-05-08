"""Snake, classic  game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange, choice
from turtle import setup, hideturtle, tracer, listen, onkey, update, ontimer, clear, done

from freegames import square, vector

COLORS = ['blue', 'orange', 'purple', 'pink', 'orange']
def pick_two_different_colors(palette):
    if len(set(palette)) < 2:
        raise ValueError("Palette must contain at least two different colors.")
    snake_color = choice(palette)
    remaining   = [c for c in palette if c != snake_color] 
    food_color  = choice(remaining) 
    return snake_color, food_color 

SNAKE_COLOR, FOOD_COLOR = pick_two_different_colors(COLORS)
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

def move_food():
    """Move food randomly one step without leaving the window."""
    directions = [vector(10,0), vector(-10,0), vector (0,10), vector (0,-10)]
    step       = choice(directions)
    new_x      = food.x + step.x
    new_y      = food.y + step.y

    if -200 < new_x < 190 and -200 < new_y < 190:
        food.x = new_x
        food.y = new_y

def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    move_food()

    clear()

    for body in snake:
        square(body.x, body.y, 9, SNAKE_COLOR)

    square(food.x, food.y, 9, FOOD_COLOR)
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
