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

# Create the game window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Football Game - Single Player Mode")

# Player properties
player_radius = 20
player_x = 400
player_y = 300

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

# AI player properties
ai_player_radius = 18
ai_player_speed = 3

# Goals
goal_width = 100
goal_y = 50
left_goal_x = 100
right_goal_x = 700

# Scoring
player_score = 0
ai_player_score = 0

# Game clock
clock = pygame.time.Clock()

def reset_ball():
    global ball_x, ball_y, ball_speed_x, ball_speed_y
    ball_x = 400
    ball_y = 300
    ball_speed_x = 0
    ball_speed_y = 0

# AI player initial position
ai_player_x = random.randint(field_left + ai_player_radius, field_right - ai_player_radius)
ai_player_y = random.randint(field_top + ai_player_radius, field_bottom - ai_player_radius)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > field_left + player_radius:
        player_x -= 5
    if keys[pygame.K_RIGHT] and player_x < field_right - player_radius:
        player_x += 5
    if keys[pygame.K_UP] and player_y > field_top + player_radius:
        player_y -= 5
    if keys[pygame.K_DOWN] and player_y < field_bottom - player_radius:
        player_y += 5

    # AI player movement towards the ball
    dx = ball_x - ai_player_x
    dy = ball_y - ai_player_y
    distance_to_ball = (dx ** 2 + dy ** 2) ** 0.5

    if distance_to_ball > ball_control_distance:
        ai_player_speed_x = (dx / distance_to_ball) * ai_player_speed
        ai_player_speed_y = (dy / distance_to_ball) * ai_player_speed
    else:
        ai_player_speed_x = dx * ball_control_speed_modifier
        ai_player_speed_y = dy * ball_control_speed_modifier

    ai_player_x += ai_player_speed_x
    ai_player_y += ai_player_speed_y

    # Ball movement
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with field boundaries
    if ball_x - ball_radius < field_left or ball_x + ball_radius > field_right:
        ball_speed_x *= -1
    if ball_y - ball_radius < field_top or ball_y + ball_radius > field_bottom:
        ball_speed_y *= -1

    # Ball collision with player
    if (
        player_x - player_radius < ball_x < player_x + player_radius
        and player_y - player_radius < ball_y < player_y + player_radius
    ):
        ball_speed_x = (player_x - ball_x) / 10
        ball_speed_y = (player_y - ball_y) / 10

    # Ball collision with AI player
    if (
        ai_player_x - ai_player_radius < ball_x < ai_player_x + ai_player_radius
        and ai_player_y - ai_player_radius < ball_y < ai_player_y + ai_player_radius
    ):
        ball_speed_x = (ai_player_x - ball_x) / 10
        ball_speed_y = (ai_player_y - ball_y) / 10

    # Ball collision with goals
    if (
        left_goal_x < ball_x < left_goal_x + goal_width
        and goal_y < ball_y < goal_y + field_top
    ):
        ai_player_score += 1
        reset_ball()

    if (
        right_goal_x < ball_x < right_goal_x + goal_width
        and goal_y < ball_y < goal_y + field_top
    ):
        player_score += 1
        reset_ball()

    # Clear the screen
    window.fill(WHITE)

    # Draw the football field
    pygame.draw.rect(window, GREEN, (field_left, field_top, field_right - field_left, field_bottom - field_top))

    # Draw the goals
    pygame.draw.rect(window, WHITE, (left_goal_x, goal_y, goal_width, field_top))
    pygame.draw.rect(window, WHITE, (right_goal_x, goal_y, goal_width, field_top))

    # Draw the player as a red circle
    pygame.draw.circle(window, RED, (int(player_x), int(player_y)), player_radius)

    # Draw the AI player as a blue circle
    pygame.draw.circle(window, BLUE, (int(ai_player_x), int(ai_player_y)), ai_player_radius)

    # Draw the ball as a white circle
    pygame.draw.circle(window, WHITE, (int(ball_x), int(ball_y)), ball_radius)

    # Display scores
    font = pygame.font.SysFont(None, 36)
    player_score_text = font.render("Player Score: " + str(player_score), True, BLACK)
    ai_player_score_text = font.render("AI Player Score: " + str(ai_player_score), True, BLACK)
    window.blit(player_score_text, (50, 10))
    window.blit(ai_player_score_text, (WINDOW_WIDTH - 200, 10))

    # Update the display
    pygame.display.update()

    # Set the frame rate
    clock.tick(60)
