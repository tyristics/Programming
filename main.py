import pygame, sys, random, pygame_menu
from pygame.math import Vector2

class Game_menu:
    def start_menu(self):
        menu = pygame_menu.Menu('Змейка', cell_number_x * cell_size, cell_number_y * cell_size + not_play_zone, theme=pygame_menu.themes.THEME_GREEN)
        menu.add.button('Играть', start_the_game)
        menu.add.text_input('Имя :', default='Игрок 1')
        menu.add.button('Выход', pygame_menu.events.EXIT)
        menu.mainloop(screen)

class Apple:
    def __init__(self):
        self.x = random.randint(1, cell_number_x - 2)
        self.y = random.randint(4, cell_number_y - 2)
        self.pos = Vector2(self.x, self.y)

    def drow_fruit_apple(self):
        x_pos = int(self.pos.x * cell_size)
        y_pos = int(self.pos.y * cell_size)
        fruit_Rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
        screen.blit(apple, fruit_Rect)

    def spawn(self):
        self.x = random.randint(1, cell_number_x - 2)
        self.y = random.randint(4, cell_number_y - 2)
        self.pos = Vector2(self.x, self.y)

class Mushroom:
    def __init__(self):
        self.x = random.randint(1, cell_number_x - 2)
        self.y = random.randint(4, cell_number_y - 2)
        self.pos = Vector2(self.x, self.y)

    def drow_fruit_mushroom(self):
        x_pos = int(self.pos.x * cell_size)
        y_pos = int(self.pos.y * cell_size)
        fruit_Rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
        screen.blit(mushroom, fruit_Rect)

    def spawn(self):
        self.x = random.randint(1, cell_number_x - 2)
        self.y = random.randint(4, cell_number_y - 2)
        self.pos = Vector2(self.x, self.y)

class Snake:
    def __init__(self):
        self.x = random.randint(2, cell_number_x - 2)
        self.y = random.randint(5, cell_number_y - 2)
        self.body = [Vector2(self.x, self.y), Vector2(self.x - 1, self.y), Vector2(self.x - 2, self.y)]
        self.direction = Vector2(1, 0)
        self.add = False
        self.delete = False
        self.snake_head = snake_head_r
        self.snake_tail = snake_tail_l

    def snake_graphics(self):
        self.snake_head_graphics()
        self.snake_tail_graphics()

    def drow_snake(self):
        self.snake_graphics()
        for index, i in enumerate(self.body):
            x_pos = int(i.x * cell_size)
            y_pos = int(i.y * cell_size)
            snake_Rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            if index == 0:
                screen.blit(self.snake_head, snake_Rect)
            elif index == len(self.body) - 1:
                screen.blit(self.snake_tail, snake_Rect)
            else:
                snake_body_1 = self.body[index + 1] - i
                snake_body_2 = self.body[index - 1] - i
                if snake_body_1.x == snake_body_2.x:
                    screen.blit(snake_body_tb, snake_Rect)
                elif snake_body_1.y == snake_body_2.y:
                    screen.blit(snake_body_rl, snake_Rect)
                else:
                    if snake_body_1.x == -1 and snake_body_2.y == -1:
                        screen.blit(snake_head_bl, snake_Rect)
                    if snake_body_1.y == -1 and snake_body_2.x == -1:
                        screen.blit(snake_head_bl, snake_Rect)
                    if snake_body_1.x == 1 and snake_body_2.y == 1:
                        screen.blit(snake_head_tr, snake_Rect)
                    if snake_body_1.y == 1 and snake_body_2.x == 1:
                        screen.blit(snake_head_tr, snake_Rect)
                    if snake_body_1.x == -1 and snake_body_2.y == 1:
                        screen.blit(snake_head_tl, snake_Rect)
                    if snake_body_1.y == 1 and snake_body_2.x == -1:
                        screen.blit(snake_head_tl, snake_Rect)
                    if snake_body_1.x == 1 and snake_body_2.y == -1:
                        screen.blit(snake_head_br, snake_Rect)
                    if snake_body_1.y == -1 and snake_body_2.x == 1:
                        screen.blit(snake_head_br, snake_Rect)

    def snake_head_graphics(self):
        head_update = self.body[1] - self.body[0]
        if head_update == Vector2(1, 0):
            self.snake_head = snake_head_r
        elif head_update == Vector2(-1, 0):
            self.snake_head = snake_head_l
        elif head_update == Vector2(0, 1):
            self.snake_head = snake_head_t
        elif head_update == Vector2(0, -1):
            self.snake_head = snake_head_b

    def snake_tail_graphics(self):
        tail_update = self.body[-2] - self.body[-1]
        if tail_update == Vector2(1, 0):
            self.snake_tail = snake_tail_l
        elif tail_update == Vector2(-1, 0):
            self.snake_tail = snake_tail_r
        elif tail_update == Vector2(0, 1):
            self.snake_tail = snake_tail_b
        elif tail_update == Vector2(0, -1):
            self.snake_tail = snake_tail_t

    def snake_move(self):
            new_body = self.body[:-1]
            new_body.insert(0, new_body[0] + self.direction)
            self.body = new_body[:]

    def add_to_array(self):
        if self.add == True:
            new_body = self.body[:-1]
            new_body.insert(0, new_body[0] + self.direction)
            self.body = new_body[:]
            self.add = True
        else:
            new_body = self.body[:]
            new_body.insert(0, new_body[0] + self.direction)
            self.body = new_body[:]

    def delete_from_array(self):
        if self.delete == True:
            new_body = self.body[:-1]
            new_body.insert(0, new_body[0] + self.direction)
            self.body = new_body[:]
            self.delete = True
        else:
            new_body = self.body[:-2]
            new_body.insert(0, new_body[0] + self.direction)
            self.body = new_body[:]

    def spawn(self):
        self.x = random.randint(7, cell_number_x - 7)
        self.y = random.randint(10, cell_number_y - 7)
        self.body = [Vector2(self.x, self.y), Vector2(self.x - 1, self.y), Vector2(self.x - 2, self.y)]

class Grass:
    def drow_grass(self):
        for row in range(cell_number_y):
            if row % 2 != 0:
                for column in range(cell_number_x):
                    if column % 2 != 0:
                        grass_Rect = pygame.Rect(column * cell_size, row * cell_size + not_play_zone, cell_size, cell_size)
                        pygame.draw.rect(screen, cell_color_uneven, grass_Rect)
            else:
                for column in range(cell_number_x):
                    if column % 2 == 0:
                        grass_Rect = pygame.Rect(column * cell_size, row * cell_size + not_play_zone, cell_size, cell_size)
                        pygame.draw.rect(screen, cell_color_uneven, grass_Rect)

class Main:
    def __init__(self):
        self.snake = Snake()
        self.fruit_apple = Apple()
        self.fruit_mushroom = Mushroom()
        self.grass = Grass()
        self.game_menu = Game_menu()
        self.counter = 0

    def update(self):
        self.snake.snake_move()
        self.collision()
        self.dead()

    def drow_elements(self):
        self.grass.drow_grass()
        self.snake.drow_snake()
        self.fruit_apple.drow_fruit_apple()
        self.drow_element_mushroom()
        self.drow_counter()

    def drow_element_mushroom(self):
        if len(self.snake.body) > 5:
            self.fruit_mushroom.drow_fruit_mushroom()

    def drow_counter(self):
        counter_surface = text_apple.render(str(self.counter), True, counter_color)
        x_pos = int((cell_size * cell_number_x - cell_size * 5))
        y_pos = int(30)
        counter_Rect = counter_surface.get_rect(center = (x_pos, y_pos))
        screen.blit(counter_surface, counter_Rect)
        apple_counter_Rect = (x_pos + 15, y_pos - 10)
        screen.blit(apple, apple_counter_Rect)

    def collision(self):
        if self.snake.body[0] == self.fruit_apple.pos:
            self.fruit_apple.spawn()
            self.counter += 1
            self.snake.add_to_array()
        if self.snake.body[0] == self.fruit_mushroom.pos:
            self.fruit_mushroom.spawn()
            self.counter -= 1
            self.snake.delete_from_array()
        for i in self.snake.body[:1]:
            if i == self.fruit_apple.pos:
                self.fruit_apple.spawn()
            if i == self.fruit_mushroom.pos:
                self.fruit_mushroom.spawn()

    def dead(self):
        if not 0 <= self.snake.body[0].x < cell_number_x:
            self.game_over()
        if not 3 <= self.snake.body[0].y < (cell_number_y + 3):
            self.game_over()
        for i in self.snake.body[1:]:
            if i == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        self.counter = 0
        main.drow_elements()
        main.snake.spawn()
        self.game_menu.start_menu()


cell_number_x = 30
cell_number_y = 20
cell_size = 20
not_play_zone = 60

pygame.init()
pygame.display.set_caption('Snake')

screen = pygame.display.set_mode((cell_size * cell_number_x, cell_size * cell_number_y + not_play_zone))
clock = pygame.time.Clock()
FPS = 60

cell_color_even = (171, 215, 80)
cell_color_uneven = (162, 209, 72)
counter_color = (1, 1, 1)

snake_body_rl = pygame.image.load('img/body_rl.png')
snake_body_rl.convert()
snake_body_tb = pygame.image.load('img/body_tb.png')
snake_body_tb.convert()

snake_head_b = pygame.image.load('img/snake_head_b.png')
snake_head_b.convert()
snake_head_t = pygame.image.load('img/snake_head_t.png')
snake_head_t.convert()
snake_head_l = pygame.image.load('img/snake_head_l.png')
snake_head_l.convert()
snake_head_r = pygame.image.load('img/snake_head_r.png')
snake_head_r.convert()

snake_tail_b = pygame.image.load('img/snake_tail_b.png')
snake_tail_b.convert()
snake_tail_t = pygame.image.load('img/snake_tail_t.png')
snake_tail_t.convert()
snake_tail_l = pygame.image.load('img/snake_tail_l.png')
snake_tail_l.convert()
snake_tail_r = pygame.image.load('img/snake_tail_r.png')
snake_tail_r.convert()

snake_head_bl = pygame.image.load('img/snake_head_bl.png')
snake_head_bl.convert()
snake_head_tl = pygame.image.load('img/snake_head_tl.png')
snake_head_tl.convert()
snake_head_br = pygame.image.load('img/snake_head_br.png')
snake_head_br.convert()
snake_head_tr = pygame.image.load('img/snake_head_tr.png')
snake_head_tr.convert()

mushroom = pygame.image.load('img/mushroom.png')
mushroom.convert()
apple = pygame.image.load('img/apple.png')
apple.convert()
text_apple = pygame.font.Font('font/PFAgoraSlabPro Bold.ttf', 25)

speed = 120
UPDATE = pygame.USEREVENT
pygame.time.set_timer(UPDATE, speed)

main = Main()

def start_the_game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == UPDATE:
                main.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    if main.snake.direction.y != 1:
                        main.snake.direction = Vector2(0, -1)
                if event.key == pygame.K_a:
                    if main.snake.direction.x != 1:
                        main.snake.direction = Vector2(-1, 0)
                if event.key == pygame.K_s:
                    if main.snake.direction.y != -1:
                        main.snake.direction = Vector2(0, 1)
                if event.key == pygame.K_d:
                    if main.snake.direction.x != -1:
                        main.snake.direction = Vector2(1, 0)
        screen.fill((cell_color_even))
        main.drow_elements()
        pygame.display.update()
        clock.tick(FPS)

if __name__ == '__main__':
    main.game_menu.start_menu()