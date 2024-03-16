from turtle import Screen, Turtle, ontimer, onkey, done
from math import dist
from random import randint

WIDTH = 500
HEIGHT = 500
DELAY = 100
FOOD_SIZE = 10
SCORE = 0
OFFSETS = {'Up':(0, 20), 'Down':(0,-20), 'Left':(-20, 0), 'Right':(20, 0)}
OPPOSITE = {'Up':'Down', 'Down':'Up', 'Right':'Left', 'Left':'Right'}

def set_snake_direction(new_direction):
    global SNAKE_DIRECTION, OPPOSITE
    if OPPOSITE[new_direction] != SNAKE_DIRECTION:
        SNAKE_DIRECTION = new_direction

def get_random_food():
    x = randint(-WIDTH//2 + FOOD_SIZE, WIDTH//2 - FOOD_SIZE)
    y = randint(-HEIGHT//2 + FOOD_SIZE, HEIGHT//2 - FOOD_SIZE)
    return (x, y)

def food_colision():
    global food_pos, SCORE, snake
    if dist(snake[-1], food_pos) < 20:
        SCORE += 1
        food_pos = get_random_food()
        food.goto(food_pos)
        return True
    return False

def game_loop():
    tim.clearstamps()
    new_head = snake[-1].copy()
    new_head[0] += OFFSETS[SNAKE_DIRECTION][0]
    new_head[1] += OFFSETS[SNAKE_DIRECTION][1]
    if (new_head in snake) or (new_head[0] < -WIDTH/2) or (new_head[0] > WIDTH/2) \
        or (new_head [1] < -HEIGHT/2 ) or (new_head[1] > HEIGHT/2):
        reset()
    else:
        snake.append(new_head)
        if not food_colision():
            snake.pop(0)
        for point in snake:
            tim.goto(point[0], point[1])
            tim.stamp()
        game_screen.title(f'Snake game. SCORE : {SCORE}')
        game_screen.update()
        ontimer(game_loop, DELAY)

def reset():
    global SCORE, snake, SNAKE_DIRECTION, food_pos
    SCORE = 0
    snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
    SNAKE_DIRECTION = 'Up'
    food_pos = get_random_food()
    food.goto(food_pos)
    game_loop()

def start_game():
    global game_screen, tim, food, food_pos
    game_screen = Screen()
    game_screen.title('Snake game')
    game_screen.setup(width=WIDTH, height=HEIGHT)
    game_screen.bgcolor('#eab676')
    game_screen.tracer(0)
    game_screen.listen()
    game_screen.onkey(lambda:set_snake_direction('Up'), 'Up')
    game_screen.onkey(lambda:set_snake_direction('Left'), 'Left')
    game_screen.onkey(lambda:set_snake_direction('Down'), 'Down')
    game_screen.onkey(lambda:set_snake_direction('Right'), 'Right')
    tim = Turtle(shape='square')
    tim.color('#1B5E20')
    tim.penup()

    food = Turtle(shape='circle')
    food.color('blue')
    food.shapesize(FOOD_SIZE/20)
    food.penup()

    food_pos = get_random_food()
    food.goto(food_pos)
    reset()
    done()

if __name__ =='__main__':
    start_game()
