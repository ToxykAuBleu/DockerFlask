# Mini projet Docker

## Présentation
Pour conclure la ressource sur l'apprentissage de Docker, nous devions réaliser un mini-projet : déploiement d'une application web Python avec une base de données PostgreSQL. Le sujet est disponible à la racine du dépôt (`sujet.pdf`).  
Vous trouverez donc dans ce dépôt un fichier `docker-compose.yml` qui contient:
- une application web Python développé avec [Flask](https://flask.palletsprojects.com/en/3.0.x/) ;
- une base de données PostgreSQL initialisé avec une structure et des données (voir section Personnalisation).  

L'application web est un minimum configuré. Elle est reliée à la base de données dans laquelle elle contient une table de CD avec quelques titres de *Pink Floyd*.  
La démo propose l'affichage du contenu de la base de données et la possibilité d'ajouter des nouveaux CD.  
Les données de la base de données sont stocées dans un volume nommé `db_data`.  
*Rappel : Vous pouvez voir la liste des volumes dans une invite de commande grâce à la commande `docker volume ls`.*

## Installation
> [!WARNING]  
> Tout le projet a été réalisé sur un poste personnel connecté à Internet et sans proxy. Si vous avez des problèmes pour le téléchargement/la construction des images Docker, référez vous à la documentation [Docker-proxy](https://docs.docker.com/network/proxy/).
### Avant toute chose:
Afin d'installer l'application sur votre machine, vous devez vous assurer que vous avez :
- Docker desktop (essayé sous version 4.27.0)
- (Optionnel) git: Utile uniquement pour mettre à jour et pour cloner le dépot

### Processus d'installation:
1. Cloner le dépôt, soit depuis une invite de commande (`git clone https://github.com/ToxykAuBleu/DockerFlask`), soit en téléchargeant le dossier ZIP.
2. Extraire l'archive (si c'est le dossier ZIP), puis déplacer vous dans le nouveau dossier avec `cd DockerFlask/`
3. Exécuter dans une ligne de commande au niveau de ce répertoire:
```bash
docker-compose -p dockerflask up --wait
```
4. Dès que l'installation des conteneurs est terminée, vous pouvez tester l'application en vous rendant à l'adresse http://localhost:5000.


## Personnalisation
Pour mieux convenir à vos besoins, voici l'arborescence de ce dépôt:  
```
DockerFlask/
├── sql/
│   └── create.sql
├── src/
│   ├── static/
│   │   └── script.js
│   ├── templates/
│   │   └── index.html
│   └── index.py
├── .env
├── docker-compose.yml
├── flask.Dockerfile
└── README.md
```
Le dossier `sql/` contient tous les scripts sql qui seront éxécuté au lancement de la base de données.  
Le dossier `src/` contient tous les fichiers de l'application Python. Le conteneur Python se démarre en exécutant le fichier `index.py`. Les sous-dossiers `static/` et `templates/` correspondent aux fichiers relatifs à l'utilisation de [Flask](https://flask.palletsprojects.com/en/3.0.x/).  
Le fichier `.env` contient toutes les informations nécessaires à l'initialisation de la base de données PostgreSQL.  
Pour faire court, vous pouvez tout modifier, sauf le nom de `index.py` sinon il faut le modifier dans `flask.Dockerfile` à la toute dernière ligne.