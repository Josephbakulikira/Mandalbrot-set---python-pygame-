import pygame
import os

os.environ['SDL_VIDEO_CENTERED'] = '1' # for full screen

width, height = 1920,1080
win = (width, height)
screen = pygame.display.set_mode(win)
xaxis = width/1.80 + 150
yaxis = height/2
scale = 450 # mandakbrot size
iterations = 60 # the more iterations you make the better resolustion you'll get

def main():


    for iy in range(int(height/2+1)):
        for ix in range(width):
            z = 0+0j
            c = complex(float(ix-xaxis)/scale, float(iy-yaxis)/scale)
            x=c.real
            y=c.imag
            y2=y*y
            q=(x-0.25)**2+y2
            if not(q*(q+(x-0.25))<y2/4.0 or (x+1.0)**2 + y2 <0.0625):
                 for i in range(iterations):

                     z = z**2+c
                     if abs(z) > 2:
                        v = 765*i/iterations
                        if v > 510:
                            color = (255, 255, v%255)
                        elif v > 255:
                            color = (100,v%255 , 255)
                        else:
                            color = (0, 0, v%255)
                        break
                     else:

                         color = (0, 0, 0)

            screen.set_at((ix, iy), color)
            screen.set_at((ix, height-iy), color)

    pygame.display.update()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        # if keys[pygame.K_LEFT]: # We can check if a key is pressed like this
        #     print("ok1")
        # if keys[pygame.K_RIGHT]:
        #     print("ok2")
        # if keys[pygame.K_UP]:
        #     iterations = iterations + 5
        #     pygame.diplay.update()
        # if keys[pygame.K_DOWN]:
        #
        #     pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()
