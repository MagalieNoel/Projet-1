# ======================== main.py ========================

import pygame
import sys
from config import FPS, LIVES, SCREEN_WIDTH, SCREEN_HEIGHT, BALL_SPEED_X, BALL_SPEED_Y, BRICKS, ball_dict, paddle_dict, PADDLE_Y
from window import draw_window, show_game_over_message, show_win_message
from game   import move_ball, bounce_walls, check_floor, move_paddle, check_paddle_collision, check_brick_collision, check_win
from bricks import generate_bricks

pygame.init()
clock = pygame.time.Clock()
running = True

# Génération initiale des briques
BRICKS.extend(generate_bricks())


# ======================== PARTIE 5.1 ========================
# TODO : Fonction pour recommencer une partie
# Cette fonction est appelée quand le joueur appuie sur R
# après une fin de partie (Game Over ou victoire).
#
# Elle doit :
# 1. Remettre la balle au centre de l'écran
# 2. Réinitialiser sa vitesse (dx = BALL_SPEED_X, dy = BALL_SPEED_Y)
# 3. Réinitialiser les vies à LIVES et le score à 0
# 4. Remettre la raquette au centre
# 5. Vider la liste BRICKS avec BRICKS.clear()
# 6. Régénérer les briques avec BRICKS.extend(generate_bricks())

def restart_game():
    pass  # À compléter


# ======================== PARTIE 5.2 ========================
# TODO : Boucle principale du jeu
# Structure générale de la boucle while running :
#
#   1. Réguler la vitesse (clock.tick)
#
#   2. Parcourir les événements pygame.event.get() :
#      - pygame.QUIT   → mettre running = False
#      - pygame.KEYDOWN :
#          * pygame.K_r → si la partie est terminée (game_over ou victoire),
#                         appeler restart_game()
#
#   3. Détecter l'état de fin de partie :
#      - game_over = ball_dict["lives"] <= 0
#      - victoire  = check_win()
#      - Si l'un des deux est vrai :
#          * Afficher le bon message (show_game_over_message ou show_win_message)
#          * Ne pas exécuter le reste de la logique (utiliser continue)
#
#   4. Appeler les fonctions de jeu dans cet ordre :
#      - move_paddle()
#      - move_ball()
#      - bounce_walls()
#      - check_paddle_collision()
#      - check_brick_collision()
#
#   5. Gérer la chute de la balle :
#      Si check_floor() retourne True :
#          - Enlever une vie : ball_dict["lives"] -= 1
#          - Replacer la balle au centre et réinitialiser sa vitesse
#            (sans réinitialiser le score ni les briques)
#
#   6. Afficher la fenêtre : draw_window()

while running:
    clock.tick(FPS)

    # ── Événements ──────────────────────────────────────────
    for event in pygame.event.get():
        pass  # À compléter

    # ── État de fin de partie ────────────────────────────────
    pass  # À compléter

    # ── Logique du jeu ───────────────────────────────────────
    pass  # À compléter

    # ── Chute de la balle ────────────────────────────────────
    pass  # À compléter

    draw_window()

pygame.quit()
sys.exit()
