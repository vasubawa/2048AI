import pygame
from game import Game
from gui import GUI
from utils import load_highscore, save_highscore

def main():
    pygame.init()
    highscore = load_highscore()
    game = Game()
    gui = GUI(game, highscore)

    running = True
    while running:
        direction = gui.get_user_input()
        if direction == "quit":
            running = False
        elif direction == "restart":
            game.reset()
            gui.score = 0
        elif direction and not game.game_over:
            game.move(direction)
            if game.score > gui.highscore:
                gui.highscore = game.score
                save_highscore(gui.highscore)
        gui.update()
        if game.game_over:
            gui.display_game_over()
            # Wait for restart or quit
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        waiting = False
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                        game.reset()
                        gui.score = 0
                        waiting = False
                    if event.type == pygame.MOUSEBUTTONUP:
                        if gui.drawRestartButton().collidepoint(event.pos):
                            game.reset()
                            gui.score = 0
                            waiting = False
    pygame.quit()

if __name__ == "__main__":
    main()