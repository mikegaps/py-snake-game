import pygame
import sys
import random

pygame.init() #initialization of pygame

#SCREEN SETUP
WIDTH, HEIGHT = 800, 600 #screen height and width of window
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #screen window maker
pygame.display.set_caption("Snake") #screen name window

clock = pygame.time.Clock() #controling speed of framerate
FPS = 10 #frame per second

WHITE = (255, 255, 255) #colors
GREEN = (0, 200, 0) #colors
RED = (255, 0, 0) #colors
BLACK = (0, 0, 0) #colors

sounds = pygame.mixer.Sound("chomp-155392.mp3")

#PLAYER SETUP
snake_block = 20
snake_pos = [[100, 100]]
snake_dir = "RIGHT"
score = 0   

#Snake Food
food_x = random.randint(0, (WIDTH - snake_block) // snake_block) * snake_block
food_y = random.randint(0, (HEIGHT - snake_block) // snake_block) * snake_block

font = pygame.font.SysFont("Arial", 30)

def draw_snake(snake_body):
    for block in snake_body:
        pygame.draw.rect(screen, GREEN, (block[0], block[1], snake_block, snake_block))
        
def show_score():
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

#GAME LOOP
running = True
while running:
    
    #Step 1: Handle Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    #direksyon ng snake
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake_dir != "RIGHT":
                snake_dir = "LEFT"
            if event.key == pygame.K_RIGHT and snake_dir != "LEFT":
                snake_dir = "RIGHT"
            if event.key == pygame.K_UP and snake_dir != "DOWN":
                snake_dir = "UP"
            if event.key == pygame.K_DOWN and snake_dir != "UP":
                snake_dir = "DOWN"
        
    #Step 2: Update Game State 
    #galaw ng snake
    head_x, head_y =  snake_pos[0]
    if snake_dir == "LEFT":
        head_x -= snake_block
    elif snake_dir == "RIGHT":
        head_x += snake_block
    elif snake_dir == "UP":
        head_y -= snake_block
    elif snake_dir == "DOWN":
        head_y += snake_block
        
    #bagong ulo ng snake    
    new_head = [head_x, head_y]
    snake_pos.insert(0, new_head)
    
    #kapag kumain na ang snake
    if head_x == food_x and head_y == food_y:
        score += 1
        sounds.play()
        
        food_x = random.randint(0, (WIDTH - snake_block) // snake_block) * snake_block
        food_y = random.randint(0, (HEIGHT - snake_block) // snake_block) * snake_block
    
    else:
        snake_pos.pop()
        
    #banggaan sa pader
    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
        running = False
        
    #bangga sa sarili
    for block in snake_pos[1:]:
        if new_head == block:
            running = False
            
    #RENDER
    screen.fill(WHITE)
    draw_snake(snake_pos)
    pygame.draw.rect(screen, RED, (food_x, food_y, snake_block, snake_block)) #pagkain
    show_score()
    pygame.display.flip()

    clock.tick(FPS) #tick clock

#quit   
pygame.quit()
sys.exit()