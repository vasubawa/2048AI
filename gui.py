import pygame
from utils import COLORS

class GUI:
    def __init__(self, game, highscore, size=500):
        self.game = game
        self.size = size
        self.cell_size = size // game.size
        self.screen = pygame.display.set_mode((size, size + 80))
        pygame.display.set_caption("2048")
        self.font = pygame.font.SysFont("arial", 32, bold=True)
        self.score_font = pygame.font.SysFont("arial", 24, bold=True)
        self.highscore = highscore
        self.score = 0

    def get_user_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    return "up"
                elif event.key == pygame.K_DOWN:
                    return "down"
                elif event.key == pygame.K_LEFT:
                    return "left"
                elif event.key == pygame.K_RIGHT:
                    return "right"
                elif event.key == pygame.K_r:
                    return "restart"
            if event.type == pygame.MOUSEBUTTONUP:
                if self.drawRestartButton().collidepoint(event.pos):
                    return "restart"
        return None

    def update(self):
        self.screen.fill(COLORS['bg'])
        for i in range(self.game.size):
            for j in range(self.game.size):
                value = self.game.grid[i][j]
                rect = pygame.Rect(j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size)
                color = COLORS.get(value, COLORS['other'])
                pygame.draw.rect(self.screen, color, rect)
                pygame.draw.rect(self.screen, COLORS['bg'], rect, 4)
                if value:
                    text_color = COLORS['darkText'] if value < 8 else COLORS['lightText']
                    text = self.font.render(str(value), True, text_color)
                    text_rect = text.get_rect(center=rect.center)
                    self.screen.blit(text, text_rect)
        # Draw player score and high score
        player_score_text = self.score_font.render(f"Player Score: {self.game.score}", True, (0,0,0))
        self.screen.blit(player_score_text, (10, self.size + 10))
        highscore_text = self.score_font.render(f"High Score: {self.highscore}", True, (0,0,0))
        highscore_rect = highscore_text.get_rect()
        highscore_x = self.size - highscore_rect.width - 10
        self.screen.blit(highscore_text, (highscore_x, self.size + 10))
        # Draw restart button
        self.drawRestartButton()
        pygame.display.flip()

    def drawRestartButton(self):
        button_rect = pygame.Rect(self.size//2 - 50, self.size + 40, 100, 40)
        pygame.draw.rect(self.screen, (119, 110, 101), button_rect, border_radius=8)
        text = self.score_font.render("Restart", True, (255, 255, 255))
        text_rect = text.get_rect(center=button_rect.center)
        self.screen.blit(text, text_rect)
        return button_rect

    def display_game_over(self):
        overlay = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        overlay.fill((255, 255, 255, 180))
        self.screen.blit(overlay, (0, 0))
        text = self.font.render("Game Over!", True, (255, 0, 0))
        text_rect = text.get_rect(center=(self.size // 2, self.size // 2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(2000)
        
        
        
