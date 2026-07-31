import pygame
import time


def main():


    SCREEN_WIDTH=960
    SCREEN_HEIGHT = 480
    pygame.init()    # Prepare the PyGame module for use
    main_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    # Load an image to draw. Substitute your own.
    # PyGame handles gif, jpg, png, etc. image types.
    ball = pygame.image.load("ball.png")


    BALL_WIDTH = 105
    BALL_HEIGHT =106
    
    # Create a font for rendering text
    my_font = pygame.font.SysFont("Courier", 16)


    t0 = pygame.time.Clock()


    xpos = 100
    ypos=120
    yinc = 12
    xinc= 4


    while True:




        # Look for an event from keyboard, mouse, joystick, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:   # Window close button clicked?
            break                    # Leave game loop


        # Do other bits of logic for the game here
        t0.tick (60)


        # Completely redraw the surface, starting with background
        main_surface.fill((0, 200, 255))


        # Put a red rectangle somewhere on the surface
        main_surface.fill((255,0,0), (300, 100, 150, 90))


        # Copy our image to the surface, at this (x,y) posn
        #print (xpos, ypos)
        main_surface.blit(ball, (xpos, ypos))


        ypos += yinc
    
        if ypos > (SCREEN_HEIGHT - BALL_HEIGHT)  or ypos <= 0:
            yinc = -yinc


        xpos += xinc
    
        if xpos > (SCREEN_WIDTH - BALL_WIDTH) or xpos <= 0:
            xinc = -xinc
        
        elif ev.type == pygame.KEYUP:   # Key Pressed and released?
            if ev.key == pygame.K_UP:   # got keyboard up arrow
                if yinc >= 0 :        # increase size of increment
                    yinc+=3
                else:
                    yinc -=3
                if xinc >= 0 :
                    xinc+=1
                else:
                    xinc -=1
            elif ev.key == pygame.K_DOWN:   # got keyboard down arrow
                if yinc == 0 :        # can't get smaller
                    pass
                elif yinc> 0:
                    yinc -=3
                else:
                    yinc +=3
                if xinc == 0 :        # can't get smaller
                    pass
                elif xinc> 0:
                    xinc -=1
                else:
                    xinc +=1





        # Make a new surface with an image of the text
        the_text = my_font.render("Ball Demo", True, (0,0,0))
        # Copy the text surface to the main surface
        main_surface.blit(the_text, (10, 10))


        # Now that everything is drawn, put it on display!
        pygame.display.flip()


    pygame.quit()




main()
