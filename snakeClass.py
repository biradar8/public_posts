from turtle import Screen, Turtle, ontimer, done
from math import dist
from random import randint

WIDTH = 1500
HEIGHT = 800
DELAY = 100
FOOD_SIZE = 10


class Snake:
    OPPOSITE = {"Up": "Down", "Down": "Up", "Right": "Left", "Left": "Right"}
    OFFSETS = {"Up": (0, 20), "Down": (0, -20), "Left": (-20, 0), "Right": (20, 0)}

    def __init__(self):
        self.turtle = Turtle(shape="square")
        self.turtle.color("#888888")
        self.turtle.penup()
        self.body = [[0, 0], [20, 0], [40, 0], [60, 0]]
        self.direction = "Up"

    def set_direction(self, new_direction):
        if Snake.OPPOSITE[new_direction] != self.direction:
            self.direction = new_direction

    def new_head(self):
        head = self.body[-1].copy()
        head[0] += Snake.OFFSETS[self.direction][0]
        head[1] += Snake.OFFSETS[self.direction][1]
        return head

    def move_snake(self):
        for point in self.body:
            self.turtle.goto(point[0], point[1])
            self.turtle.stamp()

    def snake_collision(self, new_head):
        return (
            (new_head in self.body)
            or (new_head[0] < -WIDTH / 2)
            or (new_head[0] > WIDTH / 2)
            or (new_head[1] < -HEIGHT / 2)
            or (new_head[1] > HEIGHT / 2)
        )


class Food:
    def __init__(self):
        self.position = (0, 0)
        self.turtle = Turtle(shape="circle")
        self.turtle.color("#FFFFFF")
        self.turtle.shapesize(FOOD_SIZE / 20)
        self.turtle.penup()

    def randomize_position(self):
        self.position = (
            randint(-WIDTH // 2 + FOOD_SIZE, WIDTH // 2 - FOOD_SIZE),
            randint(-HEIGHT // 2 + FOOD_SIZE, HEIGHT // 2 - FOOD_SIZE),
        )
        self.turtle.goto(self.position)


class Game:
    def __init__(self):
        self.setup_screen()
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.reset()
        done()

    def setup_screen(self):
        self.screen = Screen()
        self.screen.title("Snake Game")
        self.screen.setup(width=WIDTH, height=HEIGHT)
        self.screen.bgcolor("#000000")
        self.screen.tracer(0)
        self.screen.listen()
        self.screen.onkey(lambda: self.snake.set_direction("Up"), "Up")
        self.screen.onkey(lambda: self.snake.set_direction("Left"), "Left")
        self.screen.onkey(lambda: self.snake.set_direction("Down"), "Down")
        self.screen.onkey(lambda: self.snake.set_direction("Right"), "Right")

    def game_loop(self):
        self.snake.turtle.clearstamps()
        new_head = self.snake.new_head()
        if self.snake.snake_collision(new_head):
            self.reset()
        else:
            self.snake.body.append(new_head)
            if not self.food_collision():
                self.snake.body.pop(0)
            self.snake.move_snake()
            self.screen.title(f"Snake game. SCORE : {self.score}")
            self.screen.update()
            ontimer(self.game_loop, DELAY)

    def food_collision(self):
        if dist(self.snake.body[-1], self.food.position) < 20:
            self.score += 1
            self.food.randomize_position()
            return True
        return False

    def reset(self):
        self.score = 0
        self.snake.body = [[0, 0], [20, 0], [40, 0], [60, 0]]
        self.snake.direction = "Up"
        self.food.randomize_position()
        self.game_loop()


if __name__ == "__main__":
    try:
        game = Game()
    except KeyboardInterrupt:
        ...
    except Exception as e:
        print(e)
