import pygame


def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surface_sz = 640   # Desired physical surface size, in pixels.


    # Create surface of (width, height), and its window.
    main_surface = pygame.display.set_mode((surface_sz, surface_sz))


    # Set up some data to describe a small rectangle and its color
    small_rect = (10, 20, 200, 300)# xpos, ypos, width, height
    some_color = (250, 250, 0)        # A color is a mix of (Red,                       
                                    # Green, Blue)


    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop


        # Update your game objects and data structures here...


        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        main_surface.fill((150, 100, 0))


        # Overpaint a smaller rectangle on the main surface
        main_surface.fill(some_color, small_rect)


        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()


    pygame.quit()     # Once we leave the loop, close the window.


main()
