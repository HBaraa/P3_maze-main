#Project 3   MacGyver

OpenClassrooms project 3
    Le projet 3 consiste à  la création d'un jeu de labyrithe 2D en utilisant la bibliothéque pygame pour l'affichage, le controle des mouvements et la génération de la boucle de jeu. Dans ce jeu, l'objectif est d'aider MacGyver à s'échapper en trouvant trois objets; un aiguille, un tube plastique et l'éther, générés aléatoirement dans le labyrinthe pour créer une seringue et endormir le gardien.
    Le jeu comporte un seul niveau qui définit les emplacements des murs , de MacGyver et de gardien. Cette structure est affichée sur une fenétre créée en utilisant pygame et Les trois objets seront répartis aléatoirement dans le labyrinthe et changeront d’emplacement si l'utilisateur ferme le jeu et le relance. 
    MacGyver sera contrôlé par les touches directionnelles du clavier pour se déplacer de case en case, avec 15 cases sur la longueur d'une fenétre du jeu de forme carré de 15 sprites de longueur et il récupèrera un objet simplement en se déplaçant dessus.
    Le joueur gagne si MacGyver récupére les trois objets et trouve la sortie et il perd s'il n'arrive pas à avoir tous les objets.
    
#Installation:
    Installation de python
    Création de dossier de projet
        &cd C:/Users
        &mkdir répertoire_de_travail
    Initialisation d'un repo Git
        &git init
    Téléchargement des ressources qui contient certains éléments graphiques nécessaires au jeu dans le repo de projet
    Création de l'environnement virtuel
        &python  -m  venv  .venv
    Activation de l'environnement virtuel
        &source .venv/Scripts/activate
    Intallation de pygame
        &pip install pygame
    Installation de fichier requirements
        &pip install -r requirements.txt
    création de fichier .gitignore
        &touch .gitignore

#Usage:
Pour utiliser ce programme vous devez avoir déjà installé python et cloné le repo sur votre machine locale puis vous pouvez l'utiliser en suivant ces commandes pour lancer le jeu:

    &cd C:/Users/répertoire_de_travail
    &python  -m  venv  .venv
    &source .venv/Scripts/activate
    pip install -r requirements.txt
    pip install pygame
    python main.py







    
    
