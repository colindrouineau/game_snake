import pygame
from random import randint

BACKGROUND_COLOR = (150, 150, 150)
TILES_COLOR = (100, 100, 100)
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
CLOCK_FREQUENCY = 10
TIME_LIMIT = 10 # s
LENGHT_TILES = 20
STARTING_POSITION = (10, 5) # in tiles
SNAKE_COLOR = (0, 175, 125)
HEAD_COLOR = (0, 100, 200)
FRUIT_COLOR = (250, 25, 25)
DIRECTIONS = {'up': (-1,0), 'down': (1,0), 'left': (0,-1), 'right': (0,1)}

class Snake():

    def __init__(self):
        self.position = [(10, 7), (10, 6), (10, 5)]
        self.direction = 'r'
        self.fruit_position = (randint(0, 14), randint(0, 19))
        self.is_alive = True
        self.score = 0

    
    def display(self):
        for i, j in self.position:
            rect = pygame.Rect(j*20, i*20, LENGHT_TILES, LENGHT_TILES)
            pygame.draw.rect(screen, SNAKE_COLOR, rect)
        rect = pygame.Rect(self.position[0][1]*20, self.position[0][0]*20, LENGHT_TILES, LENGHT_TILES)
        pygame.draw.rect(screen, HEAD_COLOR, rect)

        rect = pygame.Rect(self.fruit_position[1]*20, self.fruit_position[0]*20, LENGHT_TILES, LENGHT_TILES)
        pygame.draw.rect(screen, FRUIT_COLOR, rect)

    def move(self):
        last_position = self.position[-1]
        for i in range(2, len(self.position)+1):
            self.position[-i+1] = self.position[-i]
        
        futur_position = [self.position[0][0] + DIRECTIONS[self.direction][0], self.position[0][1] + DIRECTIONS[self.direction][1]]
        # Si la tête du serpent sort de l'écran, on la fait réapparaître de l'autre côté de telle sorte que le serpent fait un tour
        if futur_position[0] < 0 :
            futur_position[0] = 14
        if futur_position[0] >= 15:
            futur_position[0] = 0
        if futur_position[1] < 0:
            futur_position[1] = 19
        if futur_position[1] >= 20:
            futur_position[1] = 0
        self.position[0] = (futur_position[0], futur_position[1])

        if self.position[0] == self.fruit_position:
            self.position.append(last_position)
            self.fruit_position = (randint(0, 14), randint(0, 19))
            self.score += 1
        
        if self.position[0] in self.position[1:]:
            self.is_alive = False
    

pygame.init()


screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
clock = pygame.time.Clock()

def starting_screen():
    screen.fill( BACKGROUND_COLOR )
    for i in range(SCREEN_HEIGHT // LENGHT_TILES):
        for j in range(SCREEN_WIDTH // LENGHT_TILES):
            if (i + j) % 2 == 1:
                rect = pygame.Rect(20*j, 20*i, LENGHT_TILES, LENGHT_TILES)
                pygame.draw.rect(screen, TILES_COLOR, rect)

def draw_game_over_screen():
    screen.fill(TILES_COLOR)
    font = pygame.font.SysFont('arial', 40)
    title = font.render('Game Over', True, (255, 255, 255))
    screen.blit(title, (SCREEN_WIDTH/2 - title.get_width()/2, SCREEN_HEIGHT/2 - title.get_height()/3))
    pygame.display.update()

starting_screen()

rect = pygame.Rect(STARTING_POSITION[1]*20, STARTING_POSITION[0]*20, 3*LENGHT_TILES, LENGHT_TILES)
pygame.draw.rect(screen, SNAKE_COLOR, rect)

snake = Snake()

while snake.is_alive :
    pygame.display.set_caption("snake.io - Score = " + str(snake.score))
    clock.tick(CLOCK_FREQUENCY)
    one_passage = True
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and one_passage:
            one_passage = False
            if event.key == pygame.K_UP and snake.direction != 'd':
                snake.direction = 'u'
            if event.key == pygame.K_DOWN and snake.direction != 'u':
                snake.direction = 'd'
            if event.key == pygame.K_LEFT and snake.direction != 'r':
                snake.direction = 'l'
            if event.key == pygame.K_RIGHT and snake.direction != 'l':
                snake.direction = 'r'

            if event.key == pygame.K_q:
                pygame.quit()
                snake.is_alive = False
    
    snake.move()

    starting_screen()
    snake.display()
    pygame.display.update()

draw_game_over_screen()
clock.tick(0.1)

pygame.quit()
