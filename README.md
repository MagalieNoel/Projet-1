[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/SIL8K1es)
# Projet – Casse-briques 🧱 (INF1007)

## Directives
:alarm_clock: **Date de remise** : à définir par l'enseignant

:mailbox_with_mail: **Remise** : sur GitHub

---

## Introduction

Dans ce projet, vous aurez comme tâche de compléter une version simplifiée du jeu **Casse-briques** (Breakout).

Le Casse-briques est un jeu d'arcade dans lequel le joueur contrôle une raquette pour faire rebondir une balle et détruire toutes les briques affichées en haut de l'écran. L'objectif est de **détruire toutes les briques sans laisser la balle tomber** en dehors de l'écran.

Le joueur dispose de **3 vies**. Une vie est perdue lorsque la balle touche le bas de l'écran. La partie se termine lorsque toutes les vies sont perdues, ou lorsque toutes les briques sont détruites (victoire !).

> **Contrôles :**
> - **Flèche gauche / Flèche droite** : déplacer la raquette
> - **R** : recommencer la partie (après un Game Over ou une victoire)

> **Système de points :** les briques du haut valent plus que celles du bas.
> La rangée bleue (haut) rapporte **5 points** par brique, et la rangée verte (bas) **1 point**.
> Les rangées intermédiaires valent 4, 3 et 2 points de haut en bas.

Afin de simplifier votre travail, **l'interface graphique et la structure générale du jeu sont déjà fournies**. Votre tâche consiste à implémenter la logique du jeu :
- le chargement des images et l'initialisation des objets,
- la génération de la grille de briques,
- le déplacement de la balle et de la raquette,
- les rebonds et les collisions,
- la gestion du score, des vies et du redémarrage.

> **Pour lancer le jeu, vous devez exécuter le fichier `main.py`.**

---

## Installations requises

Ce projet nécessite l'utilisation de la bibliothèque **pygame**.

Assurez-vous que votre environnement conda est activé :

```bash
conda activate INF1007
```

Installez ensuite pygame :

```bash
pip install -U pygame
```

---

## Structure du projet

```plaintext
2026E-PR01-main/
├── assets/
│   ├── background.png
│   ├── ball.png
│   ├── paddle.png
│   ├── brick_blue.png
│   ├── brick_red.png
│   ├── brick_orange.png
│   ├── brick_yellow.png
│   └── brick_green.png
├── ball.py
├── paddle.py
├── bricks.py
├── config.py
├── game.py
├── window.py
└── main.py
```

## Description des fichiers

- **assets/** : contient toutes les images utilisées par le jeu.

- **config.py** : constantes globales du jeu :
  - dimensions de la fenêtre (`SCREEN_WIDTH`, `SCREEN_HEIGHT`),
  - paramètres de la balle (`BALL_SIZE`, `BALL_SPEED_X`, `BALL_SPEED_Y`),
  - paramètres de la raquette (`PADDLE_WIDTH`, `PADDLE_HEIGHT`, `PADDLE_Y`, `PADDLE_SPEED`),
  - paramètres des briques (`BRICK_ROWS`, `BRICK_COLS`, `BRICK_WIDTH`, `BRICK_HEIGHT`, `BRICK_PADDING`, `BRICK_COLORS`, `BRICK_POINTS`),
  - nombre de vies (`LIVES`),
  - structures globales (`BRICKS`, `ball_dict`, `paddle_dict`).

- **ball.py** : charge l'image de la balle et initialise `ball_dict`.

- **paddle.py** : charge l'image de la raquette et initialise `paddle_dict`.

- **bricks.py** : charge les images des briques et définit `generate_bricks()`.

- **game.py** : contient toute la logique du jeu : déplacement, rebonds, collisions, victoire.

- **window.py** : initialise la fenêtre pygame et gère l'affichage (fond, balle, raquette, briques, score, messages).

- **main.py** : point d'entrée du programme, contient la boucle principale.

---

## Système de coordonnées

La coordonnée `(0, 0)` se trouve en **haut à gauche** de l'écran. L'axe `x` va vers la droite et l'axe `y` va vers le bas.

```
(0,0) ──────────────────────► x
  │    [briques]
  │
  │
  │         ●  ← balle
  │
  │        ════  ← raquette
  ▼
  y
```

### Notion de vitesse : `dx` et `dy`

La balle se déplace grâce à deux variables de vitesse :
- `dx` : déplacement horizontal à chaque image. Positif = vers la droite, négatif = vers la gauche.
- `dy` : déplacement vertical à chaque image. Positif = vers le bas, négatif = vers le haut.

Pour faire rebondir la balle sur un mur vertical (gauche ou droit), on inverse `dx` (`dx *= -1`).
Pour faire rebondir la balle sur un mur horizontal (plafond ou raquette), on inverse `dy` (`dy *= -1`).

---

# Travail à réaliser

Vous devez compléter les parties indiquées par `TODO` dans les fichiers **ball.py**, **paddle.py**, **bricks.py**, **game.py** et **main.py**.

> [!IMPORTANT]
> L'affichage et la structure générale sont entièrement fournis.
> Prenez le temps de lire et comprendre le code existant avant d'ajouter vos modifications.

---

## PARTIE 1 : La balle et la raquette

### 1.1 : Chargement de l'image de la balle

Dans le fichier `ball.py`, chargez l'image de la balle et redimensionnez-la.

**Indications :**
- L'image se trouve dans `assets/ball.png`.
- Chargez-la avec `pygame.image.load(...)`.
- Redimensionnez-la avec `pygame.transform.scale(image, taille)`.
- La taille finale doit correspondre à la constante `BALL_SIZE`.
- Stockez le résultat dans la variable `ball_img`.

---

### 1.2 : Initialisation du dictionnaire `ball_dict`

Toujours dans `ball.py`, initialisez le dictionnaire `ball_dict` qui contient l'état courant de la balle.

**Clés à initialiser :**
- `"x"` : position horizontale de départ — balle centrée dans l'écran : `SCREEN_WIDTH // 2`.
- `"y"` : position verticale de départ — balle centrée dans l'écran : `SCREEN_HEIGHT // 2`.
- `"dx"` : vitesse horizontale initiale (utiliser `BALL_SPEED_X`).
- `"dy"` : vitesse verticale initiale (utiliser `BALL_SPEED_Y`).
- `"lives"` : nombre de vies (utiliser `LIVES`).
- `"score"` : score initial (`0`).

---

### 1.3 : Chargement de l'image de la raquette

Dans `paddle.py`, chargez et redimensionnez l'image de la raquette (`assets/paddle.png`).

- La taille finale doit correspondre à `(PADDLE_WIDTH, PADDLE_HEIGHT)`.
- Stockez le résultat dans `paddle_img`.

---

### 1.4 : Initialisation du dictionnaire `paddle_dict`

Dans `paddle.py`, initialisez `paddle_dict`.

**Clés à initialiser :**
- `"x"` : position horizontale pour centrer la raquette : `(SCREEN_WIDTH - PADDLE_WIDTH) // 2`.
- `"y"` : position verticale fixe (utiliser `PADDLE_Y`).

---

## PARTIE 2 : La grille de briques

### 2.1 : Génération des briques (fonction `generate_bricks`)

Dans `bricks.py`, complétez la fonction `generate_bricks()`.

Cette fonction doit retourner une **liste de dictionnaires**, un par brique, en utilisant une **compréhension de liste imbriquée** (double boucle `for row ... for col` dans la même expression `[...]`).

> [!NOTE]
> Le début de `bricks.py` (avant votre TODO) charge déjà toutes les images de briques dans un
> dictionnaire appelé `brick_images`. Par exemple, `brick_images["blue"]` contient l'image
> de la brique bleue. Vous pouvez l'utiliser directement dans votre compréhension de liste.

**Chaque dictionnaire doit contenir :**
```python
{
    "x"      : BRICK_OFFSET_LEFT + col * (BRICK_WIDTH + BRICK_PADDING),
    "y"      : BRICK_OFFSET_TOP  + row * (BRICK_HEIGHT + BRICK_PADDING),
    "width"  : BRICK_WIDTH,
    "height" : BRICK_HEIGHT,
    "color"  : BRICK_COLORS[row],
    "image"  : brick_images[BRICK_COLORS[row]],
    "active" : True,
    "points" : BRICK_POINTS[row]
}
```

**Exemple de structure attendue (à compléter vous-même) :**
```python
def generate_bricks():
    return [
        { ... }
        for row in range(BRICK_ROWS)
        for col in range(BRICK_COLS)
    ]
```

> `row` correspond à la rangée (0 = rangée du haut, `BRICK_ROWS - 1` = rangée du bas).
> `col` correspond à la colonne (0 = colonne de gauche, `BRICK_COLS - 1` = colonne de droite).

---

## PARTIE 3 : Physique et déplacements

### 3.1 : Déplacement de la balle (`move_ball`)

Dans `game.py`, complétez `move_ball()`.

À chaque appel, la balle avance dans sa direction actuelle :
- Ajouter `dx` à `x`.
- Ajouter `dy` à `y`.

---

### 3.2 : Rebonds sur les murs et le plafond (`bounce_walls`)

Complétez `bounce_walls()`.

La balle rebondit lorsqu'elle atteint un bord :
- **Bord gauche** (`x <= 0`) : inverser `dx` (`ball_dict["dx"] *= -1`).
- **Bord droit** (`x + BALL_SIZE[0] >= SCREEN_WIDTH`) : inverser `dx`.
- **Plafond** (`y <= 0`) : inverser `dy` (`ball_dict["dy"] *= -1`).

> Le bas de l'écran n'est pas géré ici — c'est le rôle de `check_floor`.

---

### 3.3 : Détection du sol (`check_floor`)

Complétez `check_floor()`.

- Retourner `True` si le bas de la balle (`ball_dict["y"] + BALL_SIZE[1]`) est supérieur ou égal à `SCREEN_HEIGHT`.
- Retourner `False` sinon.

---

### 3.4 : Déplacement de la raquette (`move_paddle`)

Complétez `move_paddle()`.

La fonction `pygame.key.get_pressed()` retourne l'état de toutes les touches du clavier sous forme d'une liste. On peut tester si une touche est maintenue enfoncée comme ceci :

```python
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:   # flèche gauche maintenue
    ...
if keys[pygame.K_RIGHT]:  # flèche droite maintenue
    ...
```

> Contrairement aux événements `KEYDOWN` utilisés dans d'autres projets, `get_pressed()` détecte
> les touches **maintenues** — c'est ce qu'on veut pour un déplacement continu.

**À implémenter :**
- **Flèche gauche** : diminuer `x` de `PADDLE_SPEED`.
- **Flèche droite** : augmenter `x` de `PADDLE_SPEED`.
- Empêcher la raquette de sortir de l'écran :
  - `x` minimum : `0`
  - `x` maximum : `SCREEN_WIDTH - PADDLE_WIDTH`

> Astuce : `paddle_dict["x"] = max(0, min(paddle_dict["x"], SCREEN_WIDTH - PADDLE_WIDTH))`

---

## PARTIE 4 : Collisions

### 4.1 : Collision balle / raquette (`check_paddle_collision`)

Complétez `check_paddle_collision()`.

1. Créez un rectangle pour la balle : `(ball_dict["x"], ball_dict["y"], BALL_SIZE[0], BALL_SIZE[1])`.
2. Créez un rectangle pour la raquette : `(paddle_dict["x"], paddle_dict["y"], PADDLE_WIDTH, PADDLE_HEIGHT)`.
3. Utilisez `rects_collide(r_balle, r_raquette)` pour tester le chevauchement.
4. En cas de collision :
   - Inversez `dy` (`ball_dict["dy"] *= -1`).
   - Forcez `dy` à être négatif : `ball_dict["dy"] = -abs(ball_dict["dy"])`.

> **Pourquoi forcer `dy` négatif ?** Si la balle entre dans la raquette avec `dy` déjà positif,
> l'inverser la ferait rebondir vers le bas — et elle resterait coincée à l'intérieur de la raquette,
> alternant indéfiniment. Forcer `-abs(dy)` garantit que la balle repart toujours vers le haut.

---

### 4.2 : Collision balle / briques (`check_brick_collision`)

Complétez `check_brick_collision()`.

Parcourez `BRICKS`. Pour chaque brique dont `active == True` :

1. Créez les rectangles de la balle et de la brique.
2. Testez la collision avec `rects_collide(...)`.
3. En cas de collision :
   - Marquez la brique inactive : `brick["active"] = False`.
   - Ajoutez les points au score : `ball_dict["score"] += brick["points"]`.
   - Inversez `dy` : `ball_dict["dy"] *= -1`.
   - Arrêtez la boucle avec `break` pour ne toucher qu'une seule brique à la fois.

---

### 4.3 : Vérification de la victoire (`check_win`)

Complétez `check_win()`.

- Retourner `True` si **toutes** les briques ont `active == False`.
- Retourner `False` sinon.

> Astuce : utilisez `all()` avec une expression génératrice.
> Exemple : `all(not brick["active"] for brick in BRICKS)`

---

## PARTIE 5 : Boucle principale et redémarrage

### 5.1 : Fonction `restart_game()`

Dans `main.py`, complétez `restart_game()`.

Elle doit remettre le jeu dans son état initial :

1. Remettre la balle au centre : `ball_dict["x"] = SCREEN_WIDTH // 2` et `ball_dict["y"] = SCREEN_HEIGHT // 2`.
2. Réinitialiser `dx` à `BALL_SPEED_X` et `dy` à `BALL_SPEED_Y`.
3. Réinitialiser `lives` à `LIVES` et `score` à `0`.
4. Remettre la raquette au centre : `paddle_dict["x"] = (SCREEN_WIDTH - PADDLE_WIDTH) // 2`.
5. Vider la liste de briques avec `BRICKS.clear()`.
6. Régénérer les briques avec `BRICKS.extend(generate_bricks())`.

> [!IMPORTANT]
> Utilisez `BRICKS.clear()` puis `BRICKS.extend(...)` plutôt que `BRICKS = generate_bricks()`.
> En Python, écrire `BRICKS = ...` crée une **nouvelle variable locale** et ne modifie pas la liste
> globale utilisée par les autres fichiers. `clear()` et `extend()` modifient la liste existante
> en place, ce qui permet à `window.py` et `game.py` de voir les changements.

---

### 5.2 : Boucle principale (`while running`)

Complétez la boucle dans `main.py`.

**Étape 1 – Gestion des événements (`pygame.event.get`)** :
- `pygame.QUIT` : mettre `running = False`.
- `pygame.KEYDOWN` + touche `R` (`pygame.K_r`) : appeler `restart_game()` si la partie est terminée (game over ou victoire).

**Étape 2 – Détection de fin de partie** :
- Si `ball_dict["lives"] <= 0` : afficher `show_game_over_message()` puis passer à l'itération suivante avec `continue`.
- Si `check_win()` retourne `True` : afficher `show_win_message()` puis `continue`.

> **À quoi sert `continue` ?** Il saute immédiatement au prochain tour de la boucle `while`,
> sans exécuter le reste du code en dessous. Cela permet de figer le jeu en attendant que
> le joueur appuie sur R, sans planter ni continuer à déplacer la balle.

**Étape 3 – Logique du jeu** (dans cet ordre) :
```
move_paddle()
move_ball()
bounce_walls()
check_paddle_collision()
check_brick_collision()
```

**Étape 4 – Chute de la balle** :
- Si `check_floor()` retourne `True` :
  - Enlever une vie : `ball_dict["lives"] -= 1`.
  - Replacer la balle au centre : `ball_dict["x"] = SCREEN_WIDTH // 2`, `ball_dict["y"] = SCREEN_HEIGHT // 2`.
  - Réinitialiser la vitesse : `ball_dict["dx"] = BALL_SPEED_X`, `ball_dict["dy"] = BALL_SPEED_Y`.
  - Ne pas toucher au score ni aux briques.

**Étape 5** : appeler `draw_window()`.

---

# Barème de correction

Le projet est noté sur **20 points**.

| **Partie**                                      | **Tâche**                                                                    | **Points** |
| ----------------------------------------------- | ---------------------------------------------------------------------------- | ---------- |
| **PARTIE 1 : La balle et la raquette**          |                                                                              | **/4**     |
| 1.1 : Image de la balle                         | Image chargée depuis `assets/`                                               | 0.5        |
|                                                 | Image redimensionnée avec `BALL_SIZE`                                        | 0.5        |
| 1.2 : `ball_dict`                               | Position initiale correcte (centre de l'écran)                               | 0.5        |
|                                                 | `dx` et `dy` correctement initialisés                                        | 0.5        |
|                                                 | `lives` et `score` correctement initialisés                                  | 0.5        |
| 1.3 : Image de la raquette                      | Image chargée et redimensionnée                                              | 0.5        |
| 1.4 : `paddle_dict`                             | Position initiale correcte (centrée, bonne hauteur)                          | 0.5        |
|                                                 | Clés `"x"` et `"y"` présentes                                                | 0.5        |
| **PARTIE 2 : La grille de briques**             |                                                                              | **/4**     |
| 2.1 : `generate_bricks()`                       | Utilisation d'une compréhension de liste imbriquée                           | 1          |
|                                                 | Positions `x` et `y` calculées correctement                                  | 1          |
|                                                 | Clés `active`, `points`, `color`, `image` présentes et correctes             | 1          |
|                                                 | Nombre de briques correct (`BRICK_ROWS * BRICK_COLS`)                        | 1          |
| **PARTIE 3 : Physique et déplacements**         |                                                                              | **/5**     |
| 3.1 : `move_ball()`                             | Mise à jour de `x` et `y` avec `dx` et `dy`                                  | 1          |
| 3.2 : `bounce_walls()`                          | Rebond sur le bord gauche et droit (inversion de `dx`)                       | 1          |
|                                                 | Rebond sur le plafond (inversion de `dy`)                                    | 1          |
| 3.3 : `check_floor()`                           | Détection correcte du bas de l'écran                                         | 1          |
| 3.4 : `move_paddle()`                           | Déplacement gauche/droite avec les flèches                                   | 0.5        |
|                                                 | Clampement correct (la raquette ne sort pas de l'écran)                      | 0.5        |
| **PARTIE 4 : Collisions**                       |                                                                              | **/5**     |
| 4.1 : `check_paddle_collision()`                | Création correcte des rectangles                                             | 0.5        |
|                                                 | Utilisation de `rects_collide`                                               | 0.5        |
|                                                 | Inversion de `dy` et protection contre le blocage (`-abs(dy)`)               | 1          |
| 4.2 : `check_brick_collision()`                 | Parcours des briques actives uniquement                                      | 0.5        |
|                                                 | Désactivation de la brique et ajout des points                               | 1          |
|                                                 | Inversion de `dy` et `break` après la première collision                     | 1          |
| 4.3 : `check_win()`                             | Utilisation de `all()` et détection correcte de la victoire                  | 0.5        |
| **PARTIE 5 : Boucle principale et redémarrage** |                                                                              | **/2**     |
| 5.1 : `restart_game()`                          | Réinitialisation complète (balle, raquette, vies, score, briques)            | 1          |
| 5.2 : Boucle principale                         | Gestion de `pygame.QUIT` et de la touche `R`                                 | 0.5        |
|                                                 | Gestion correcte de Game Over et victoire (affichage + `continue`)           | 0.5        |
| **Total**                                       |                                                                              | **/20**    |
