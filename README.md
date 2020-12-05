# Project 3 MacGyver

OpenClassrooms project 3 Le projet 3 consiste à la création d'un jeu de labyrithe 2D en utilisant la bibliothéque pygame pour l'affichage, le controle des mouvements et la génération de la boucle de jeu.
Dans ce jeu, l'objectif est d'aider MacGyver à s'échapper en trouvant trois objets; un aiguille, un tube plastique et l'éther, générés aléatoirement dans le labyrinthe pour créer une seringue et endormir le gardien.
Le jeu comporte un seul niveau qui définit les emplacements des murs , de MacGyver et de gardien. Cette structure est affichée sur une fenétre créée en utilisant pygame et Les trois objets seront répartis aléatoirement dans le labyrinthe et changeront d’emplacement si l'utilisateur ferme le jeu et le relance. MacGyver sera contrôlé par les touches directionnelles du clavier pour se déplacer de case en case, avec 15 cases sur la longueur d'une fenétre du jeu de forme carré de 15 sprites de longueur et il récupèrera un objet simplement en se déplaçant dessus. Le joueur gagne si MacGyver récupére les trois objets et trouve la sortie et il perd s'il n'arrive pas à avoir tous les objets.

## Installation

- Installer python 3.8
- Cloner le projet depuis le [repository Github](https://github.com/HBaraa/P3_maze-main)
- A la racine du projet :

```bash
python -m venv .venv  # ou python3 -m venv .venv
source .venv/Scripts/activate  # .venv/bin/activate on linux
pip install -r requirements.txt  # installation des dépendances
```

## Usage

Pour utiliser ce programme vous devez avoir déjà installé python et cloné le repo sur votre machine locale puis vous pouvez l'utiliser en suivant ces commandes pour lancer le jeu:
```python
python main.py
```
