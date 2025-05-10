import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Window size
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Colors (RGB)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Create the game window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Football Game - Multiplayer Mode")

# Player properties
player_radius = 20
player1_x = 200
player1_y = 300
player2_x = 600
player2_y = 300
player1_score = 0
player2_score = 0

# Ball properties
ball_radius = 10
ball_x = 400
ball_y = 300
ball_speed_x = 0
ball_speed_y = 0

# Field boundaries
field_left = 100
field_right = 700
field_top = 50
field_bottom = 550

# Ball control properties
ball_control_distance = 30
ball_control_speed_modifier = 1.5

# Goals
goal_width = 100
goal_height = 200
goal_y = 200

# Game clock
clock = pygame.time.Clock()

def reset_ball():
    global ball_x, ball_y, ball_speed_x, ball_speed_y
    ball_x = 400
    ball_y = 300
    ball_speed_x = 0
    ball_speed_y = 0

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Player 1 movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player1_x > field_left + player_radius:
        player1_x -= 5
    if keys[pygame.K_d] and player1_x < field_right - player_radius:
        player1_x += 5
    if keys[pygame.K_w] and player1_y > field_top + player_radius:
        player1_y -= 5
    if keys[pygame.K_s] and player1_y < field_bottom - player_radius:
        player1_y += 5

    # Player 2 movement
    if keys[pygame.K_LEFT] and player2_x > field_left + player_radius:
        player2_x -= 5
    if keys[pygame.K_RIGHT] and player2_x < field_right - player_radius:
        player2_x += 5
    if keys[pygame.K_UP] and player2_y > field_top + player_radius:
        player2_y -= 5
    if keys[pygame.K_DOWN] and player2_y < field_bottom - player_radius:
        player2_y += 5

    # Ball movement
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with field boundaries
    if ball_x - ball_radius < field_left or ball_x + ball_radius > field_right:
        ball_speed_x *= -1
    if ball_y - ball_radius < field_top or ball_y + ball_radius > field_bottom:
        ball_speed_y *= -1

    # Ball collision with player 1
    if (
        player1_x - player_radius < ball_x < player1_x + player_radius
        and player1_y - player_radius < ball_y < player1_y + player_radius
    ):
        # Add ball control mechanics here (e.g., controlling the ball's direction based on player proximity)
        ball_speed_x = (player1_x - ball_x) / 10
        ball_speed_y = (player1_y - ball_y) / 10

    # Ball collision with player 2
    if (
        player2_x - player_radius < ball_x < player2_x + player_radius
        and player2_y - player_radius < ball_y < player2_y + player_radius
    ):
        # Add ball control mechanics here (e.g., controlling the ball's direction based on player proximity)
        ball_speed_x = (player2_x - ball_x) / 10
        ball_speed_y = (player2_y - ball_y) / 10

    # Ball collision with goals
    if (
        field_left < ball_x < field_left + goal_width
        and goal_y < ball_y < goal_y + goal_height
    ):
        reset_ball()
        player2_score += 1

    if (
        field_right - goal_width < ball_x < field_right
        and goal_y < ball_y < goal_y + goal_height
    ):
        reset_ball()
        player1_score += 1

    # Clear the screen
    window.fill(WHITE)

    # Draw the football field
    pygame.draw.rect(window, GREEN, (field_left, field_top, field_right - field_left, field_bottom - field_top))

    # Draw the center line
    pygame.draw.line(window, WHITE, (WINDOW_WIDTH // 2, field_top), (WINDOW_WIDTH // 2, field_bottom), 5)

    # Draw the left goal post
    pygame.draw.rect(window, BLACK, (field_left - 5, goal_y, 5, goal_height))

    # Draw the right goal post
    pygame.draw.rect(window, BLACK, (field_right, goal_y, 5, goal_height))

    # Draw player 1 as a red circle
    pygame.draw.circle(window, RED, (int(player1_x), int(player1_y)), player_radius)

    # Draw player 2 as a blue circle
    pygame.draw.circle(window, BLUE, (int(player2_x), int(player2_y)), player_radius)

    # Draw the ball as a white circle
    pygame.draw.circle(window, WHITE, (int(ball_x), int(ball_y)), ball_radius)

    # Display scores
    font = pygame.font.SysFont(None, 36)
    player1_score_text = font.render("Player 1: " + str(player1_score), True, BLACK)
    player2_score_text = font.render("Player 2: " + str(player2_score), True, BLACK)
    window.blit(player1_score_text, (50, 10))
    window.blit(player2_score_text, (WINDOW_WIDTH - 180, 10))

    # Update the display
    pygame.display.update()

    # Set the frame rate
    clock.tick(60)
