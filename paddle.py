# ======================== paddle.py ========================

import pygame
from config import PADDLE_WIDTH, PADDLE_HEIGHT, PADDLE_Y, SCREEN_WIDTH, paddle_dict

# ======================== PARTIE 1.3 ========================
# TODO : Charger l'image de la raquette et la redimensionner
# - L'image se trouve dans assets/paddle.png
# - Redimensionner avec pygame.transform.scale(image, (PADDLE_WIDTH, PADDLE_HEIGHT))
# - Stocker le résultat dans la variable « paddle_img »
img = pygame.image.load("assets/paddle.png")
paddle_img = pygame.transform.scale(img, (PADDLE_WIDTH, PADDLE_HEIGHT))  # À remplacer par l'image chargée et redimensionnée


# ======================== PARTIE 1.4 ========================
# TODO : Initialiser les valeurs dans le dictionnaire « paddle_dict »
# La raquette doit apparaître centrée horizontalement, en bas de l'écran.
#
# Clés à initialiser :
# - "x" : position horizontale (centrée dans l'écran)
# - "y" : position verticale fixe (utiliser PADDLE_Y)

paddle_dict.update({
    # À compléter
    "x": (SCREEN_WIDTH / 2) - PADDLE_WIDTH / 2,
    "y": PADDLE_Y
})
