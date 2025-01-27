from flask import Flask,render_template
from flask import Flask, render_template_string, render_template, jsonify
from flask import Flask, render_template, request, redirect
from flask import json
from urllib.request import urlopen
import sqlite3

app = Flask(__name__) #creating flask app name

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/resume_1')
def resume_1():
    return render_template("resume_1.html")

@app.route('/resume_2')
def resume_2():
    return render_template("resume_2.html")

@app.route('/resume_template')
def resume_template():
    return render_template("resume_template.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

# Création d'une nouvelle route pour la lecture de la BDD
@app.route("/consultation/")
def ReadBDD():
    conn = sqlite3.connect('./database.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM livres;')
    cursor.execute('SELECT * FROM contact;')
    data = cursor.fetchall()
    conn.close()
    
    # Rendre le template HTML et transmettre les données
    return render_template('read_data.html', data=data)

@app.route('/submit_contact_form', methods=['POST'])
def submit_contact_form():
    # Récupérer les données du formulaire depuis la requête POST
    nom = request.form['nom']
    email = request.form['email']
    message = request.form['message']
    
    # Connexion à la base de données
    conn = sqlite3.connect('./database.db')
    cursor = conn.cursor()
    
    # Insérer les données dans la table contact
    cursor.execute('INSERT INTO contact (name, email, message) VALUES (?, ?, ?)', (nom, email, message))
    
    # Commit les changements et ferme la connexion
    conn.commit()
    conn.close()
    
    # Redirection vers une page de confirmation ou autre
    return redirect('/confirmation')

if(__name__ == "__main__"):
    app.run()
