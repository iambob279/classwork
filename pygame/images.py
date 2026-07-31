import pygame
import time


def main():
    pygame.init()
    main_surface = pygame.display.set_mode((480, 240))
    ball = pygame.image.load("ball.png")
    my_font = pygame.font.SysFont("Courier", 16)
    frame_count = 0
    frame_rate = 0
    t0 = time.process_time()

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break

        frame_count += 1
        if frame_count % 500 == 0:
            t1 = time.process_time()
            delta_time = t1 - t0  # Calculate the time difference
            if delta_time > 0:  # Check if the time difference is greater than zero
                frame_rate = 500 / delta_time
            else:
                frame_rate = 0  # Or some other default value, like 0
            t0 = t1
        
        xpos = 100
        ypos=120
        main_surface.fill((0, 200, 255))
        main_surface.fill((255, 0, 0), (300, 100, 150, 90))
        main_surface.blit(ball, (xpos, ypos))
        the_text = my_font.render("Frame = {0},  rate = {1:.2f} fps".format(frame_count, frame_rate), True, (0, 0, 0))
        main_surface.blit(the_text, (10, 10))

        yinc = 12
        xinc= 4



        if ev.type == pygame.KEYUP:   # Key Pressed and released?
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



        pygame.display.flip()

    pygame.quit()


main()
