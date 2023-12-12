import pygame
from random import randint

WHITE = (150, 150, 150)
BLACK = (100, 100, 100)
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
CLOCK_FREQUENCY = 10
TIME_LIMIT = 10 # s
LENGHT_TILES = 20
STARTING_POSITION = (10, 5) # en tiles
SNAKE_COLOR = (0, 175, 125)
HEAD_COLOR = (0, 100, 200)
FRUIT_COLOR = (250, 25, 25)
DIRECTION = {'u': (-1,0), 'd': (1,0), 'l': (0,-1), 'r': (0,1)}

class snake_class:
    def __init__(self):
        self.position = [(10, 7), (10, 6), (10, 5)]
        self.direction = 'r'
        self.fruit_position = (randint(0, 14), randint(0, 19))
        self.a_perdu = False
        self.score = 0

    
    def afficher(self):
        for i, j in self.position:
            rect = pygame.Rect(j*20, i*20, LENGHT_TILES, LENGHT_TILES)
            pygame.draw.rect(screen, SNAKE_COLOR, rect)
        rect = pygame.Rect(self.position[0][1]*20, self.position[0][0]*20, LENGHT_TILES, LENGHT_TILES)
        pygame.draw.rect(screen, HEAD_COLOR, rect)

        rect = pygame.Rect(self.fruit_position[1]*20, self.fruit_position[0]*20, LENGHT_TILES, LENGHT_TILES)
        pygame.draw.rect(screen, FRUIT_COLOR, rect)

    def avancer(self):
        last_position = self.position[-1]
        for i in range(2, len(self.position)+1):
            self.position[-i+1] = self.position[-i]
        
        hyp_pos = [self.position[0][0] + DIRECTION[self.direction][0], self.position[0][1] + DIRECTION[self.direction][1]]
        if hyp_pos[0] < 0 :
            hyp_pos[0] = 14
        if hyp_pos[0] >= 15:
            hyp_pos[0] = 0
        if hyp_pos[1] < 0:
            hyp_pos[1] = 19
        if hyp_pos[1] >= 20:
            hyp_pos[1] = 0
        self.position[0] = (hyp_pos[0], hyp_pos[1])

        if self.position[0] == self.fruit_position:
            self.position.append(last_position)
            self.fruit_position = (randint(0, 14), randint(0, 19))
            self.score += 1
        
        if self.position[0] in self.position[1:]:
            self.a_perdu = True
    

pygame.init()


screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
clock = pygame.time.Clock()

def starting_screen():
    screen.fill( WHITE )
    for i in range(SCREEN_HEIGHT // LENGHT_TILES):
        for j in range(SCREEN_WIDTH //LENGHT_TILES):
            if (i + j) % 2 == 1:
                rect = pygame.Rect(20*j, 20*i, LENGHT_TILES, LENGHT_TILES)
                pygame.draw.rect(screen, BLACK, rect)

starting_screen()

rect = pygame.Rect(STARTING_POSITION[1]*20, STARTING_POSITION[0]*20, 3*LENGHT_TILES, LENGHT_TILES)
pygame.draw.rect(screen, SNAKE_COLOR, rect)

snake = snake_class()

while not snake.a_perdu :
    pygame.display.set_caption("snake.io - Score = " + str(snake.score))
    clock.tick(CLOCK_FREQUENCY)
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
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
    
    snake.avancer()

    starting_screen()
    snake.afficher()
    pygame.display.update()

pygame.quit()

# Problème :
# revenir sur ses pas en faisant up left