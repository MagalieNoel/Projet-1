# ======================== window.py ========================

import pygame
from config import (
    SCREEN_WIDTH, SCREEN_HEIGHT,
    BRICKS, ball_dict, paddle_dict
)
from ball   import ball_img
from paddle import paddle_img

# Initialisation de la fenêtre
GAME_WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Casse-briques")

# Chargement du fond
background_img = pygame.image.load("assets/background.png")
background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))


# ======================== AFFICHAGE ========================
# (Ces fonctions sont entièrement fournies — ne pas les modifier)

def draw_window():
    """Dessine tous les éléments du jeu à chaque image."""
    GAME_WINDOW.blit(background_img, (0, 0))

    # Briques actives
    for brick in BRICKS:
        if brick["active"]:
            GAME_WINDOW.blit(brick["image"], (brick["x"], brick["y"]))

    # Raquette
    GAME_WINDOW.blit(paddle_img, (paddle_dict["x"], paddle_dict["y"]))

    # Balle
    GAME_WINDOW.blit(ball_img, (ball_dict["x"], ball_dict["y"]))

    # Affichage du score et des vies
    font = pygame.font.SysFont(None, 40)
    score_text = font.render(f"Score : {ball_dict['score']}", True, (255, 255, 255))
    lives_text = font.render(f"Vies : {ball_dict['lives']}", True, (255, 255, 255))
    GAME_WINDOW.blit(score_text, (10, 10))
    GAME_WINDOW.blit(lives_text, (SCREEN_WIDTH - 130, 10))

    pygame.display.update()


def show_game_over_message():
    """Affiche un écran de fin de partie."""
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    overlay.set_alpha(200)
    overlay.fill((0, 0, 0))
    GAME_WINDOW.blit(overlay, (0, 0))

    font_big  = pygame.font.SysFont(None, 80)
    font_small = pygame.font.SysFont(None, 36)

    title = font_big.render("Game Over", True, (220, 50, 50))
    hint  = font_small.render("Appuyez sur R pour recommencer", True, (200, 200, 200))
    score = font_small.render(f"Score final : {ball_dict['score']}", True, (255, 220, 50))

    GAME_WINDOW.blit(title, title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)))
    GAME_WINDOW.blit(score, score.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20)))
    GAME_WINDOW.blit(hint,  hint.get_rect(center=(SCREEN_WIDTH  // 2, SCREEN_HEIGHT // 2 + 70)))

    pygame.display.update()


def show_win_message():
    """Affiche un écran de victoire."""
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    overlay.set_alpha(200)
    overlay.fill((0, 0, 0))
    GAME_WINDOW.blit(overlay, (0, 0))

    font_big  = pygame.font.SysFont(None, 80)
    font_small = pygame.font.SysFont(None, 36)

    title = font_big.render("Vous avez gagne !", True, (50, 220, 100))
    hint  = font_small.render("Appuyez sur R pour rejouer", True, (200, 200, 200))
    score = font_small.render(f"Score final : {ball_dict['score']}", True, (255, 220, 50))

    GAME_WINDOW.blit(title, title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)))
    GAME_WINDOW.blit(score, score.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20)))
    GAME_WINDOW.blit(hint,  hint.get_rect(center=(SCREEN_WIDTH  // 2, SCREEN_HEIGHT // 2 + 70)))

    pygame.display.update()
