import pygame
import sys

# import the font module
import pygame.font
# Initialize the font module
pygame.font.init()
# create a font object, you can change the font size and style according to your preference.
font_style = pygame.font.Font(None, 30)


# Initialize Pygame
pygame.init()

# Set the dimensions of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Pong Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Paddle dimensions
paddle_width = 20
paddle_height = 100

# Ball dimensions
ball_width = 20

# Initial paddle and ball positions
paddle1_pos = [0, (size[1]/2) - (paddle_height/2)]
paddle2_pos = [size[0] - paddle_width, (size[1]/2) - (paddle_height/2)]
ball_pos = [size[0]/2, size[1]/2]

# Paddle and ball speeds
paddle_speed = 5
ball_speed_x = 5
ball_speed_y = 5

# Score
score1 = 0
score2 = 0

while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
            sys.exit()

    # --- Game logic should go here
    keys = pygame.key.get_pressed()

    # Move paddle 1
    if keys[pygame.K_w]:
        paddle1_pos[1] -= paddle_speed
    if keys[pygame.K_s]:
        paddle1_pos[1] += paddle_speed

    # Move paddle 2
    if keys[pygame.K_UP]:
        paddle2_pos[1] -= paddle_speed
    if keys[pygame.K_DOWN]:
        paddle2_pos[1] += paddle_speed

    # Move ball
    ball_pos[0] += ball_speed_x
    ball_pos[1] += ball_speed_y

    # Check for ball collision with top and bottom of screen
    if ball_pos[1] <= 0 or ball_pos[1] >= size[1] - ball_width:
        ball_speed_y = -ball_speed_y

    # Check for ball collision with paddle 1
    if (ball_pos[0] <= paddle_width) and (paddle1_pos[1] <= ball_pos[1] <= paddle1_pos[1] + paddle_height):
        ball_speed_x = -ball_speed_x
    elif ball_pos[0] <= 0:
        ball_pos = [size[0]/2, size[1]/2]
        score2 += 1
        
    # Check for ball collision with paddle 2
    if (ball_pos[0] >= size[0] - paddle_width - ball_width) and (paddle2_pos[1] <= ball_pos[1] <= paddle2_pos[1] + paddle_height):
        ball_speed_x = -ball_speed_x
    elif ball_pos[0] >= size[0]:
        ball_pos = [size[0]/2, size[1]/2]
        score1 += 1

    # Keep paddles on screen
    if paddle1_pos[1] < 0:
        paddle1_pos[1] = 0
    elif paddle1_pos[1] > size[1] - paddle_height:
        paddle1_pos[1] = size[1] - paddle_height
    if paddle2_pos[1] < 0:
        paddle2_pos[1] = 0
    elif paddle2_pos[1] > size[1] - paddle_height:
        paddle2_pos[1] = size[1] - paddle_height
        
    # --- Drawing code should go here
    screen.fill((0, 0, 0)) # Fill the screen with black color
    # Draw the paddles
    pygame.draw.rect(screen, (255, 255, 255), (paddle1_pos[0], paddle1_pos[1], paddle_width, paddle_height))
    pygame.draw.rect(screen, (255, 255, 255), (paddle2_pos[0], paddle2_pos[1], paddle_width, paddle_height))
    # Draw the ball
    pygame.draw.circle(screen, (255, 255, 255), (int(ball_pos[0]), int(ball_pos[1])), int(ball_width/2))
    
        # Draw scores
    score1_text = font_style.render("Player 1: " + str(score1), True, white)
    screen.blit(score1_text, (50, 50))
    score2_text = font_style.render("Player 2: " + str(score2), True, white)
    screen.blit(score2_text, (size[0]-250, 50))
    
    # --- Go ahead and update the screen.
    pygame.display.flip()
    
    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()

