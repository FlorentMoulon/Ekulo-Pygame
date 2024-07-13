# Ekulo : échapper au labyrinthe

Ekulo est un jeu générateur de labyrinthes en Python, conçu pour offrir une expérience captivante où les joueurs naviguent à travers des labyrinthes générés aléatoirement. 
Ce projet est développé par Florent MOULON, Maxime TERRASSE et Aymen BELKASMI.

# Images
**jeu :**
![Image du jeu](Image-jeu.png)

**menu :**
![Image du menu](Image-menu.png)

## Fonctionnalités
- Génération aléatoire de labyrinthes.
- Conversion des labyrinthes en images.
- Interface graphique pour naviguer dans les labyrinthes.
- Système de score et de niveaux.
- Texture pack éditable


## Prérequis
- Python 3.6 ou supérieur.
- **Bibliothèques Python:** *PIL*, *pygame*, *tkinter*.


## Installation
#### Clonez le dépôt:
```bash
git clone https://github.com/votre-utilisateur/ekulo.git
cd ekulo
```

#### Installez les dépendances:
```bash
pip install -r requirements.txt
```

## Structure du Projet
- **Ekulo.py:** Point d'entrée principal du jeu. Gère l'interface graphique et la logique du jeu.
- **mazegenerator.py:** Contient les fonctions pour générer les labyrinthes.
- **mazeimage.py:** Gère la conversion des labyrinthes en images et le chargement des textures.
