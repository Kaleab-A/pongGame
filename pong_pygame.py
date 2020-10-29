import pygame
import random, sys
from pygame.locals import *
import winsound

# Colors
BLACK = (0, 0, 0)
WHITE = tuple([255] * 4)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pong by @Kal")

# Variable
FPS = 60
fpsClock = pygame.time.Clock()
paddle_speed = 8
ball_speed = 4
win_width, win_height = 800, 600
paddle_w, paddle_h = 15, 100
paddleA_pos, paddleB_pos = win_height//2 - (paddle_h//2), win_height//2 - (paddle_h//2)
ball_posX, ball_posY = win_width//2 , win_height // 2
dirtX = random.randint(0,1)
dirtY = random.randint(0,1)
ball_speedX = ball_speed if dirtX else (-1 * ball_speed)
ball_speedY = ball_speed if dirtY else (-1 * ball_speed)

# Score
score_a, score_b = 0, 0
font = pygame.font.SysFont("Courier", 30)
text = "Player A: 0  Player B: 0"
text_veiw = font.render(text, 1, WHITE)
win.blit(text_veiw, (150, 200))

# Main loop
while True:
    win.fill(BLACK)
    
    # Movement
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    if key[pygame.K_UP] and paddleB_pos > 0:
        paddleB_pos -= paddle_speed
    elif key[pygame.K_DOWN] and paddleB_pos < 600 - paddle_h:
        paddleB_pos += paddle_speed
    if key[pygame.K_w] and paddleA_pos > 0:
        paddleA_pos -= paddle_speed
    elif key[pygame.K_s] and paddleA_pos < 600 - paddle_h:
        paddleA_pos += paddle_speed
            
    
    # Paddle
    pygame.draw.rect(win, WHITE, (20, paddleA_pos, paddle_w, paddle_h))
    pygame.draw.rect(win, WHITE, (win_width - (20 + paddle_w), paddleB_pos, paddle_w, paddle_h))
    
    # Ball
    pygame.draw.circle(win, WHITE, (ball_posX, ball_posY), 15, 0)
    ball_posX += ball_speedX
    ball_posY += ball_speedY
    
    # Ball Vs Wall Collusion
    if ball_posX >= 800:
        ball_posX, ball_posY = win_width//2 , win_height // 2
        dirtY = random.randint(0,1)
        ball_speedX = -1 * ball_speedX
        ball_speedY = ball_speed if dirtY else (-1 * ball_speed)
        score_a += 1
        text = "Player A: " + str(score_a) + " Player B: " + str(score_b)
    elif ball_posX <= 0:
        ball_posX, ball_posY = win_width//2 , win_height // 2
        dirtY = random.randint(0,1)
        ball_speedX = -1 * ball_speedX
        ball_speedY = ball_speed if dirtY else (-1 * ball_speed)
        score_b += 1
        text = "Player A: " + str(score_a) + "  Player B: " + str(score_b)
    if (score_a >= 10 or score_b >= 10):
        sys.exit() 
    text_veiw = font.render(text, 1, WHITE)
    win.blit(text_veiw, (150, 40))
    if ball_posY >= 600:
        ball_speedY *= -1
        winsound.PlaySound("./audio/default.wav", winsound.SND_ASYNC)
    elif ball_posY <= 0:
        ball_speedY *= -1
        winsound.PlaySound("./audio/default.wav", winsound.SND_ASYNC)
    
    # Ball Vs Paddle Collusion
        # 50 or 750 =  (0 or window_wid) - 20 - paddle_wid - ball_radius
    if ball_posX >= 750 and ball_posY > paddleB_pos and ball_posY < paddleB_pos + paddle_h: 
        ball_speedX *= -1
        winsound.PlaySound("./audio/tone_8.wav", winsound.SND_ASYNC)
    elif ball_posX <= 50 and ball_posY > paddleA_pos and ball_posY < paddleA_pos + paddle_h: 
        ball_speedX *= -1
        winsound.PlaySound("./audio/tone_8.wav", winsound.SND_ASYNC)
    pygame.display.update()
    fpsClock.tick(FPS)
