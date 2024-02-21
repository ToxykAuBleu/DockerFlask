from flask import Flask, request, render_template, redirect, url_for, jsonify
import psycopg2
import time

app = Flask(__name__)

# Connexion à la base de données
def dbConnect():
    try:
        # Les paramètres de connexion sont passés en dur pour l'exemple.
        # Dans un environnement de dév pûr/de production, il faut les stocker dans un fichier de configuration.
        with psycopg2.connect(host="db", database="postgres", user="postgres", password="postgres" ) as conn:
            print("Connecté à la base de données")
            return conn
    except (Exception, psycopg2.Error) as error:
        print("Erreur lors de la connexion à la base de données: ", error)
        print("Nouvelle tentative de connexion dans 5 secondes")
        time.sleep(5)
        return dbConnect()
# Initialisation de la connexion
# Note: la variable est donc gloable, on peut y accéder dans toutes les fonctions grâce au mot-clé global
conn = dbConnect()

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/newCD', methods=['POST'])
def new_CD():
    global conn

    # Récupération des données du formulaire
    title = request.form['input-title']
    auteur = request.form['input-auteur']
    genre = request.form['input-genre']
    prix = request.form['input-price']
    
    # Initialisation de la requête
    cursor = conn.cursor()
    sql = "INSERT INTO CD (Titre, Auteur, Genre, Prix) VALUES (%s, %s, %s, %s)"
    valeurs = (title, auteur, genre, prix)

    # Exécution de la requête
    try:
        cursor.execute(sql, valeurs)
        conn.commit()
    except (Exception, psycopg2.Error) as error:
        conn.rollback()
        print("Erreur lors de l'insertion du CD: ", error)
    
    # Fermeture du curseur et redirection
    cursor.close()
    return redirect(url_for('index'))

@app.route('/getCD', methods=['GET'])
def get_CD():
    global conn

    # Initialisation de la requête
    response = {}
    sql = "SELECT * FROM CD;"
    cursor = conn.cursor()

    # Exécution de la requête
    cursor.execute(sql) 
    result = cursor.fetchall()
    for row in result:
        response[row[0]] = {
            "Titre": row[1],
            "Artiste": row[2],
            "Genre": row[3],
            "Prix": row[4]
        }

    # Fermeture du curseur et retour de la réponse
    cursor.close()
    return response

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")