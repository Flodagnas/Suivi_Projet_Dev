<p align="center">
  <a href="https://docs.python.org/fr/3.8/" target="_blank"><img src="https://logo.clearbit.com/python.org" width="100"></a>&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://www.sqlite.org/docs.html" target="_blank"><img src="https://cdn.icon-icons.com/icons2/2107/PNG/512/file_type_sqlite_icon_130153.png" width="100"></a>&nbsp;&nbsp;&nbsp;
</p>

# Suivi Projet Dev

# Énoncé

Créer un serveur de matchmaking. Ce serveur permettera de faire jouer 2 joueurs en réseau, sur le jeu Puissance 4.

## Fonctionnalités demandées
### Modèle de données :
- Une file d’attente, contenant pour chaque attendant :
    - le moyen de communiquer avec lui (IP et port par exemple)
    - un pseudo
    - la date à laquelle il est entrée dans la file
- Des matchs, contenant pour chacun :
    - le moyen de communiquer avec le joueur 1
    - le moyen de communiquer avec le joueur 2
    - le plateau de jeu
    - si le match est fini
    - s'il y a eu victoire du joueur 1, du joueur 2 ou égalité
- Des tours, contenant pour chacun :
    - la liaison avec le match
    - qui a joué : le joueur 1 ou le joueur 2
    - l’information du coup joué (en fonction du jeu choisi)

### Le serveur de Matchmaking contient :
- Le lien avec la base de données
- Un système de socket avec les actions suivantes :
    - arrivé d’un client dans la file d’attente (réception)
    - début d’un match (envoie)
    - réception d’un tour (réception puis envoie)
    - fin d’un match (envoie)
- Une vérification constante de la file d’attente et création de matchs en fonction
- Une logique de jeu.

### Le logiciel client contient :
- Un système de socket avec les actions suivantes :
    - entrée en file d’attente (envoie)
    - début d’un match (réception)
    - jouer un coup (envoie)
    - prendre en compte le coup adverse (réception)
    - fin d’un match (réception)
- Une partie de la logique du jeu choisis.
- Une IMH pour pouvoir jouer

## Liens utiles

- Documentation technique pour <strong>Python</strong>: https://docs.python.org/fr/3.8/ </br>
- Documentation technique pour <strong>sqlite</strong>: https://www.sqlite.org/docs.html </br>
- Lien vers le <strong>Trello</strong>: https://trello.com/b/KLYcQYM4


## Groupe
- Florian Dagnas
- Mathias Leroy  

---
<p align="center">
    <strong> YNOV NANTES - B2 - 2022</strong>
</p>
