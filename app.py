import pygame
import sys
import pyttsx3
from parse import parse_text_string


# initialize text to speech
text_speech = pyttsx3.init()


# Initialize pygame
pygame.init()

# Window dimensions
window_width = 800
window_height = 600

# Create the window
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Image Display")

# Load images
background_image = pygame.image.load("./assets/windows.jpg")
image1 = pygame.image.load("./assets/blue.jpg")
image2 = pygame.image.load("./assets/pink.jpg")

# Resize images to fit the screen
background_image = pygame.transform.scale(
    background_image, (window_width, window_height))
image1 = pygame.transform.scale(image1, (window_width // 2, window_height))
image2 = pygame.transform.scale(image2, (window_width // 2, window_height))

# Load font for text
font = pygame.font.Font(None, 36)

# Load JSON array
with open('script.txt', 'r') as f:
    script_str = f.read()
script = parse_text_string(script_str)


# Initialize variables for loop control
index = 0
next_time = 0

# Main loop
running = True
while running:
    current_time = pygame.time.get_ticks()  # Get current time in milliseconds

    # Check if it's time to switch to the next object in the array
    if index < len(script):
        # Load properties from the current object in JSON array
        text = script[index]['text']
        blue = "B" in script[index]['character']
        pink = "P" in script[index]['character']
        length = script[index]['length']

        # Create text surface
        text_surface = font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.center = (window_width // 2, window_height - 30)

        index += 1
    else:
        running = False
        continue

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    window.fill((0, 0, 0))

    # Draw the background image
    window.blit(background_image, (0, 0))

    # Draw images based on JSON object properties
    if blue:
        window.blit(image1, (0, 0))
    if pink:
        window.blit(image2, (window_width // 2, 0))

    # Draw text
    window.blit(text_surface, text_rect)

    # Update the display
    pygame.display.flip()

    text_speech.say(text)
    text_speech.runAndWait()

# Quit pygame
pygame.quit()
sys.exit()
