#Step 1: Import muna ang mga library na kakailanganin
import pygame
import sys
import random

#Step 2: mag-initialize ng pygame
pygame.init()

#Step 3: mag set up ng window screen para sa laro
WIDTH, HEIGHT = 800, 600 #screen height and width of window
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #screen window maker
pygame.display.set_caption("Snake") #screen name window

#Step 4: I-set up ang bilis ng laro at Frame per Seconds
clock = pygame.time.Clock() #controling speed of framerate
FPS = 10 #frame per second

#Step 5: mag handa ng mga kulay na gagamitin para sa laro
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

#Optional: Mag handa ng sounds kung gusto mo
sounds = pygame.mixer.Sound("chomp-155392.mp3")

#Step 6: Mag-setup ng player depende sa gusto mo
snake_block = 20 #kung gaano kalaki ang player(snake)
snake_pos = [[100, 100]]
snake_dir = "RIGHT"
score = 0   

#Snake Food
food_x = random.randint(0, (WIDTH - snake_block) // snake_block) * snake_block #random.randint(0, (800-20 / 20) = 0, 39)
food_y = random.randint(0, (HEIGHT - snake_block) // snake_block) * snake_block #random.randint(0, (600 -20 / 20) = 0, 29)

font = pygame.font.SysFont("Arial", 30)

def draw_snake(snake_body):
    for block in snake_body:
        pygame.draw.rect(screen, GREEN, (block[0], block[1], snake_block, snake_block))
        
def show_score():
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (360, 10))

#GAME LOOP
running = True
while running:
    
    #HANDLE INPUT
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
        
    #UPDATE GAME STATE
    #galaw ng snake
    head_x = snake_pos[0][0]
    head_y = snake_pos[0][1]
    
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
        
        food_x = random.randint(0, (WIDTH - snake_block) // snake_block) * snake_block #random.randint(0, (800-20 / 20) = 0, 39)
        food_y = random.randint(0, (HEIGHT - snake_block) // snake_block) * snake_block #random.randint(0, (600 -20 / 20) = 0, 29)
    
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