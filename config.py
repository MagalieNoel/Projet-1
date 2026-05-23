# ======================== config.py ========================

# Dimensions de la fenêtre
SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600

# Images par seconde
FPS = 60

# ── Raquette ────────────────────────────────────────────────
PADDLE_WIDTH  = 120
PADDLE_HEIGHT = 18
PADDLE_Y      = SCREEN_HEIGHT - 55   # position verticale fixe (en bas)
PADDLE_SPEED  = 8

# ── Balle ───────────────────────────────────────────────────
BALL_SIZE     = (24, 24)
BALL_SPEED_X  = 5    # vitesse horizontale initiale
BALL_SPEED_Y  = -6   # vitesse verticale initiale (négative = vers le haut)

# ── Briques ─────────────────────────────────────────────────
BRICK_ROWS       = 5
BRICK_COLS       = 10
BRICK_WIDTH      = 65
BRICK_HEIGHT     = 22
BRICK_PADDING    = 7           # espace entre les briques
BRICK_OFFSET_TOP = 80          # distance depuis le haut de l'écran
# décalage horizontal pour centrer la grille
BRICK_OFFSET_LEFT = (SCREEN_WIDTH - BRICK_COLS * BRICK_WIDTH - (BRICK_COLS - 1) * BRICK_PADDING) // 2

# Couleurs (une par rangée, du haut vers le bas)
BRICK_COLORS  = ["blue","red", "orange", "yellow", "green"]
# Points accordés par brique (même ordre que BRICK_COLORS)
BRICK_POINTS  = [5, 4, 3, 2, 1]

# ── Vies ────────────────────────────────────────────────────
LIVES = 3

# ── État global du jeu ──────────────────────────────────────
# Ces structures seront remplies dans ball.py, paddle.py et bricks.py
BRICKS      = []   # liste de dictionnaires représentant chaque brique
ball_dict   = {}   # sera rempli dans ball.py
paddle_dict = {}   # sera rempli dans paddle.py
