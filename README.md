# TD3 MSCI: Les basiques du code: un Puissance4

Le but de ce TD est d'explorer des basiques de code. <br/>
Pour cela, nous allons coder un puissance 4. <br/>
Je donnerai des instructions pas à pas au début. <br/>
Ensuite, vous allez ré-utiliser les concepts pour aller plus loin.

On va écrire des tests, ils vont nous aider à s'assurer que tout fonctionne bien, ou repérer une erreur tôt.<br/>
Il est complètement normal de faire des erreurs dans le domaine du code.

Puissance 4 est un jeu avec une grille de 6 colonnes et 7 rangées. </br>
A tour de rôle, les joueurs mettent une pièce de leur couleur dans une colonne. <br/>
Le 1er joueur à aligner 4 pièces de sa couleur horizontalement, verticalement ou diagonalement gagne. <br/>
Si la grille est remplie et qu'aucune ligne de 4 pièces n'est faite, il y a match nul.

## Installation

### Sur Mac/Linux :
```bash
chmod +x scripts/setup.sh
./scripts/setup.sh
uv run pytest
```

### Sur Windows:

#### WSL (recommandé) -> Utilisez l'installation Mac/Linux

#### Windows terminal

```bash
scripts\setup.bat
uv run pytest
```

### PyCharm

Si vous avez PyCharm, cliquez droit sur le dossier "src/" -> "Mark directory as" -> "Sources Root"

## Partie 1: Coder le puissance4

Pour vérifier que tout est bien installé, faites tourner les tests avec la commande:
```bash
uv run pytest
```

Vous devriez voir que 3 tests ont été trouvés, qu'1 est vert et 2 sont rouges.

### 1.1. Implémenter le cas simple: retourner une grille vide

Notre jeu doit afficher la grille. Par exemple <br/>
"<br/>
|      |<br/>
|      |<br/>
|      |<br/>
|      |<br/>
|      |<br/>
|      |<br/>
|      |<br/>
"

Pour une grille vide, ou <br/>
"<br/>
|      |<br/>
|      |<br/>
|      |<br/>
|      |<br/>
|      |<br/>
| O    |<br/>
| OX   |<br/>
"

Pour une grille ou les joueurs ont joué 2 fois dans la colonne 2, et une fois dans la colonne 3.

On regarde tests/test_connect4.py
```
def test_display_board__empty():
    """Testing the display of an empty board"""
    # Given
    game = connect4.Connect4()
    expected_board = """
|      |
|      |
|      |
|      |
|      |
|      |
|      |
"""

    # When
    board = game.display_board()

    # Then
    assert board == expected_board
```

Le test exécute game.display_board(), et s'attend à cette grille vide.<br/>
On va changer connect4.py pour qu'il retourne le résultat attendu

connect4.py
```python
class Connect4:
    def display_board(self):
        board = """
|      |
|      |
|      |
|      |
|      |
|      |
|      |
"""
        return board
```

### 1.2. Jouer 1 coup

On veut pouvoir jouer. <br/>
Pour cela, le code doit se rappeler où sont les pièces. <br/>
Dans connect4.py, on créer self._board, une variable qui sait quels jetons sont placés
```python
class Connect4:
    def __init__(self):
        self._board = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]
```

Si le joueur 1 joue dans la colonne 2, on voudrait que `self._board` devienne:
la fonction `display_board` retourne le text attendu. Le test passe
```
self._board == [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
]
```
(Remarquez le **1** dans la dernière rangée)

Ajoutez le test le test
```
def test_play_column():
    # Given
    game = connect4.Connect4()
    expected_board = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
    ]

    # When
    game.play_column(2)

    # Then
    pprint(" --- Grille Enregistrée ---", game._board)
    assert game._board == expected_board
```

En tapant `pytest -s` On voit:<br/>
"<br/>
' --- Grille Enregistrée ---'<br/>
[[0, 0, 0, 0, 0, 0],<br/>
 [0, 0, 0, 0, 0, 0],<br/>
 [0, 0, 0, 0, 0, 0],<br/>
 [0, 0, 0, 0, 0, 0],<br/>
 [0, 0, 0, 0, 0, 0],<br/>
 [0, 0, 0, 0, 0, 0],<br/>
 [0, 0, 0, 0, 0, 0]]<br/>
"

On a joué en colonne 2, mais nous ne l'avons pas écrit dans self._board. <br/>
Mettez ce code dans connect4.py
```python
class Connect4:
    ...
    def play_column(self, col):
        # [1]: accède à la rangée numéro 1
	# Puis [col] accède à la colonne choisit
        self._board[1][col - 1]
```
En tapant `pytest -s` On voit:<br/>
"<br/>
' --- Grille Enregistrée ---'<br/>
[[0, 0, 0, 0, 0, 0],<br/>
 [0, 0, 1, 0, 0, 0],<br/>
 [0, 0, 0, 0, 0, 0],<br/>
 [0, 0, 0, 0, 0, 0],<br/>
 [0, 0, 0, 0, 0, 0],<br/>
 [0, 0, 0, 0, 0, 0],<br/>
 [0, 0, 0, 0, 0, 0]]<br/>
"

Ce n'était pas la grille qu'on voulait ! Le jeton est en rangée 6 et en colonne 3 !<br/>
Que s'est-t-il passé ?
- En jouant au puissance 4, la pièce tombe en bas, donc pas dans la première rangée, mais la 7ème
- Python numérote ses listes à partir de 0 (pour de bonnes raisons théoriques)

```python
class Connect4:
    ...
    def play_column(self, col):
        self._board[6][col - 1]
```
En tapant `pytest -s` On voit:<br/>
"<br/>
' --- Grille Enregistrée ---'<br/>
[[0, 0, 0, 0, 0, 0],<br/>
 [0, 0, 0, 0, 0, 0],<br/>
 [0, 0, 0, 0, 0, 0],<br/>
 [0, 0, 0, 0, 0, 0],<br/>
 [0, 0, 0, 0, 0, 0],<br/>
 [0, 0, 0, 0, 0, 0],<br/>
 [0, 1, 0, 0, 0, 0]]<br/>
"

C'est bien ce qu'on voulait.

### 1.2. Jouer 2 coups

Là, on joue systématiquement la pièce à la rangée du bas. <br/>
Si elle est occupée, il faut que la pièce se pose au-dessus. <br/>
Il faut aussi se rappeler qui était le joueur à jouer.

Ajouter le test suivant, dans test_connect4.py
```python
def test_play_column__2_plays():
    # Given
    game = connect4.Connect4()
    expected_board = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
    ]

    # When
    game.play_column(2)
    game.play_column(2)

    # Then
    pprint(" --- Grille Enregistrée, play 2 columns ---")
    pprint(game._board)
    assert game._board == expected_board
```

Maintenant, on va jouer la 1ère rangée disponible:
```python
    def play_column(self, col):
        last_row = 6
        while self._board[last_row][col-1] != 0:
            last_row = last_row - 1

        self._board[last_row][col - 1] = 1
```

On lance `uv run pytest -s`<br/>
On voit:<br/>
"<br/>
' --- Grille Enregistrée, play 2 columns ---'<br/>
[[0, 0, 0, 0, 0, 0],<br/>
 [0, 0, 0, 0, 0, 0],<br/>
 [0, 0, 0, 0, 0, 0],<br/>
 [0, 0, 0, 0, 0, 0],<br/>
 [0, 0, 0, 0, 0, 0],<br/>
 [0, 1, 0, 0, 0, 0],<br/>
 [0, 1, 0, 0, 0, 0]]<br/>
"

On a joué au bon endroit, mais toujours pour le joueur 1. <br/>
Il faut mémoriser qui est le joueur à jouer:

connect4.py
```python
```
class Connect4:
    def __init__(self):
        ....
        self._current_player = 1

    ...
    def play_column(self, col):
        last_row = 6
        while self._board[last_row][col-1] != 0:
            last_row = last_row - 1

        self._board[last_row][col - 1] = self._current_player
        self._current_player = 2 if self._current_player == 1 else 1
```

On lance `uv run pytest -s`<br/>
Le test passe

### 1.3. Afficher le résultat

Maintenant, on veut afficher "self._board" proprement aux joueurs. <br/>
On va créer `result`, le texte à retourner. <br/>

Pour créer le test, changer, dans test_connect4.py `def tst_display_board__after_some_plays` -> `def test_display_board__after_some_plays` <br/>
(On transforme "tst_" en "test_". Ainsi, "pytest" sait que c'est un test à lancer) <br/>

Chaque ligne va commencer et terminer par "|". On ajoute "\n" pour préciser un retour à la ligne

connect4.py
```python
    def display_board(self):
        result = ""
        for row in self._board:
            result += "\n|"
            for cell in row:
                if cell == 0:
                    result += " "
                elif cell == 1:
		    # A vous de remplir
		    pass
            result += "|"

        return result + "\n"
```

Obtenez que le test passe.

### 1.4. Déterminer si un joueur a gagné: cas vertical

Etant donné un `board`, on veut savoir si un jouer a gagné. <br/>
On va créer une fonction `get_winner_id` valant 0 si pas de vainqueur, 1 si 1 a gagné, etc. <br/>

Créons d'abord un test simple. <br/>
Créons une partie ou le joueur 1 à gagner avec la 1ère verticale

test_connect4.py
```python
def test_get_winner_id__vertical_case():
    """Player 1 will play 4 times in column 2,
    Player 2 will play 3 times in column 3,
    -> Player 1 wins
    """
    
    # Given
    game = connect4.Connect4()

    # When
    # Each player played 3 times
    game.play_column(2)
    game.play_column(3)
    game.play_column(2)
    game.play_column(3)
    game.play_column(2)
    game.play_column(3)

    # No winner for now
    winner = game.get_winner_id()
    assert winner == 0

    game.play_column(2)
    # Player 1 wone
    winner = game.get_winner_id()
    assert winner == 1
```

Pour cela, on va vérifier, pour chaque colonne, si on a 4 jetons de la même valeur qui se suivent

connect4.py
```python
    def get_winner_id(self):
        for column_id in range(6):
            last_row = 6
            while (
                # Si le jeton ici est 0, il n'y a pas de jetons de joueur après
                self._board[last_row][column_id] != 0
                # Si la rangée est inférieure à 3, il ne reste que 3 rangée,
                # On ne peut plus faire 4 à la suite
                and last_row >= 3
            ):
                player_id = self._board[last_row][column_id]
                # Ce joueur a-t-il 4 jetons à la suite
                has_4_in_a_row =  all(
                    player_id == self._board[last_row - i][column_id]
                    for i in range(4)
                )
                if has_4_in_a_row:
                    return player_id
                else:
                    last_row -= 1

        return 0
```

Le test doit passer

### 1.5. Déterminer si un joueur a gagné: cas horizontal

A vous de jouer. <br/>
Ecrivez un test avec un cas de victoire horizontale. <br/>
Ecrivez le code qui le vérifie.

A la fin, votre fonction `get_winner_id` est peut-être longue et complexe.
On va "refactorer", i.e. ré-organiser le code pour qu'il soit plus facile à comprendre. <br/>

Reorganiser la fonction `get_winner_id` de cette façon
```python
def get_winner_id(self):
    player_id = self._get_vertical_winner_id()
    if player_id != 0:
        return player_id

    player_id = self._get_horizontal_winner_id()
    if player_id != 0:
        return player_id

    return 0
```
        
### 1.6. Déterminer si un joueur a gagné: cas diagonaux

Faites le même travail pour une victoire diagonale vers haut droite, puis vers haut gauche.
   
### 1.7. Faire tourner le jeu complètement

Regarder le code main.py:
- Il crée un jeu connect4
- Tant qu'il n'y a pas de gagnant, demande à l'utilisateur de jouer
- display result

Créer une fonction `display_result` qui dit "Joueur 1 a gagné" si le joueur 1 a gagné, "Joueur 2 a gagné" si le joueur 2 a gagné.

Maintenant vous pouvez jouer au puissance 4 en faisant:
```bash
uv run python main.py
```

### 1.8. Cas limites

Que se passe-t-il si  un joueur essaie de jouer dans la colonne 9 (qui n'existe pas) ? <br/>
Que se passe-t-il si  un joueur essaie de jouer dans la colonne 1, qui serait déjà pleine ? <br/>

Ajouter des vérifications, dans play_column, pour éviter qu'un joueur joue un coup illégal.


### 1.9. Partie nulle

On veut que le jeu s'arrête et affiche "Partie nulle" si toute la grille a été remplie, et qu'il n'y a pas de vainqueur. <br/>

Comment faites-vous ?<br/>
Du coup, faites-le.