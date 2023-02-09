import pygame
import random

def main():

    # Initialize the game engine
    pygame.init()

    # Define colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    # Set the width and height of the screen (width, height)
    size = (700, 500)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Subway Surf Football")

    # Loop until the user clicks the close button
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # Define the player
    player_width = 40
    player_height = 60
    player_x = 350
    player_y = 400
    player_speed = 5

    # Define the opponent player
    opponent_width = 40
    opponent_height = 60
    opponent_x = random.randint(0, 700)
    opponent_y = -60
    opponent_speed = 5

    # Define the ball
    ball_width = 20
    ball_height = 20
    ball_x = player_x + player_width // 2 - ball_width // 2
    ball_y = player_y - ball_height
    ball_speed = 5
    ball_held = True

    # Define the barriers
    barrier_width = 20
    barrier_height = 80
    barrier_list = []
    for i in range(3):
        x = random.randint(0, 700)
        y = random.randint(0, 300)
        barrier = [x, y, barrier_width, barrier_height]
        barrier_list.append(barrier)

    # Define the team mates
    teammate_width = 40
    teammate_height = 60
    teammate_list = []
    for i in range(3):
        x = random.randint(0, 700)
        y = random.randint(0, 300)
        teammate = [x, y, teammate_width, teammate_height]
        teammate_list.append(teammate)

    # Game loop
    while not done:
        # Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # Clear the screen
        screen.fill(WHITE)

        # Draw the player
        player = pygame.Rect(player_x, player_y, player_width, player_height)
        pygame.draw.rect(screen, BLUE, player)

        # Draw the opponent player
        opponent = pygame.Rect(opponent_x, opponent_y, opponent_width, opponent_height)
        pygame.draw.rect(screen, RED, opponent)

        # Draw the ball
        ball = pygame.Rect(ball_x, ball_y, ball_width, ball_height)
        pygame.draw.rect(screen, BLACK, ball)

        # Draw the barriers
        for barrier in barrier_list:
            pygame.draw.rect(screen, GREEN, barrier)


        #Check if the ball is held by the player
        if ball_held:
            ball_x = player_x + player_width // 2 - ball_width // 2
            ball_y = player_y - ball_height
        else:
            ball_y -= ball_speed

        # Move the opponent player
        opponent_y += opponent_speed

        # Check if the ball and opponent player collide
        if opponent.colliderect(ball):
            ball_held = True

        # Check if the ball and a barrier collide
        for barrier in barrier_list:
            if ball.colliderect(barrier):
                ball_held = True

        # Check if the ball and a teammate collide
        for teammate in teammate_list:
            if ball.colliderect(teammate):
                ball_held = False
                ball_speed += 5

        # Get the keys pressed
        keys = pygame.key.get_pressed()

        # Move the player left and right
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed

        # Make sure the player stays within the screen boundaries
        if player_x <= 0:
            player_x = 0
        if player_x >= 700 - player_width:
            player_x = 700 - player_width

        # Make sure the opponent player stays within the screen boundaries
        if opponent_y > 500:
            opponent_y = -60
            opponent_x = random.randint(0, 700)

        # Update the screen
        pygame.display.flip()

        # Limit to 60 frames per second
        clock.tick(60)

        # Close the game window
        pygame.quit()


if __name__ == "__main__":
    main()