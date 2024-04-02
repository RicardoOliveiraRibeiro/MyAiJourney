import pygame
import sys
import math

# Initialize pygame
pygame.init()

# Set screen dimensions
screen_width = 1080  # Width of the screen
screen_height = 720  # Height of the screen
screen = pygame.display.set_mode((screen_width, screen_height))  # Create the screen surface
pygame.display.set_caption("Car Game")  # Set the window title

# Load background image
background_image = pygame.image.load("Track.png")
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))  # Resize background image

# Load car image
car_image = pygame.image.load("car.png")
car_image = pygame.transform.scale(car_image, (187 // 50, 255 // 50))  # Resize car image
car_original = car_image  # Save original car image

# Define initial car position and angle
car_x = (screen_width - car_image.get_width()) // 2
car_y = screen_height - car_image.get_height() - 20
car_angle = 90  # Initial angle (facing upwards)

# Define car speed and angular velocity
car_speed = 5
angular_velocity = 5  # Degrees turned per frame

# Define keys state
keys_state = {'left': False, 'right': False}

# Define color intervals for red and cyan
RED_LOWER = (200, 0, 0)   # Lower bound for red (in RGB format)
RED_UPPER = (255, 100, 100)  # Upper bound for red (in RGB format)

CYAN_LOWER = (120, 190, 190)  # Lower bound for cyan (in RGB format)
CYAN_UPPER = (170, 255, 255)  # Upper bound for cyan (in RGB format)

# Function to check if a color is within a specified range
def is_color_in_range(color, lower_bound, upper_bound):
    return lower_bound[0] <= color[0] <= upper_bound[0] and \
           lower_bound[1] <= color[1] <= upper_bound[1] and \
           lower_bound[2] <= color[2] <= upper_bound[2]

# Function to get the color of the pixel under the car
def get_car_pixel_color():
    return background_image.get_at((int(car_x), int(car_y)))

# Main game loop
running = True
debug_timer = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                keys_state['left'] = True
            elif event.key == pygame.K_d:
                keys_state['right'] = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                keys_state['left'] = False
            elif event.key == pygame.K_d:
                keys_state['right'] = False

    # Update car angle based on key presses
    if keys_state['left']:
        car_angle += angular_velocity
    if keys_state['right']:
        car_angle -= angular_velocity

    # Calculate new car position based on angle
    car_radians = math.radians(car_angle)  # Convert angle to radians
    car_dx = car_speed * math.cos(car_radians)  # Calculate change in x direction
    car_dy = -car_speed * math.sin(car_radians)  # Calculate change in y direction (negative because y-axis is inverted)
    car_x += car_dx
    car_y += car_dy

    # Rotate car image based on angle
    rotated_car = pygame.transform.rotate(car_original, car_angle)

    # Get color of pixel under the car
    car_pixel_color = get_car_pixel_color()

    # Check for collision with red border
    if is_color_in_range(car_pixel_color, RED_LOWER, RED_UPPER):
        print("You hit the red border! Game Over!")
        running = False

    # Check for collision with cyan finish line
    if is_color_in_range(car_pixel_color, CYAN_LOWER, CYAN_UPPER):
        print("You reached the finish line! You win!")
        running = False

    # Fill the screen with the background image
    screen.blit(background_image, (0, 0))

    # Draw the rotated car
    screen.blit(rotated_car, (car_x, car_y))

    # Update the display
    pygame.display.flip()

    # Limit frame rate
    pygame.time.Clock().tick(60)

    # Debug: Print color of the pixel under the car every 0.1 seconds
    debug_timer += 1
    if debug_timer >= 6:  # Print every 0.1 seconds (6 frames at 60 FPS)
        debug_timer = 0
        print("Color under car:", car_pixel_color)

# Quit pygame
pygame.quit()
sys.exit()
