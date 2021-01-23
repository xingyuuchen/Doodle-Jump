import pygame
from doodle import Doodle
from screen import Screen
from floor import Floor


def mainLoop():
    Floor.setLastHeight(0)

    screen = Screen('images/bg.jpg')
    X = screen.getWindowX()
    Y = screen.getWindowY()
    doodle = Doodle('images/cxy.png', 'piepie', X, Y, 180, 250)

    screen.setDoodle(doodle)

    clock = pygame.time.Clock()
    while True:
        clock.tick(Screen.getFps())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("exit game.")
                pygame.quit()
                exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    doodle.setMovingDir(-1)
                    print("left")
                elif event.key == pygame.K_RIGHT:
                    doodle.setMovingDir(1)
                    print("right")
            elif event.type == pygame.KEYUP:
                doodle.setMovingDir(0)

        screen.step()

        if not doodle.isAlive():
            return True



if __name__ == '__main__':
    pygame.init()
    while True:
        print("new game")
        if not mainLoop():
            break