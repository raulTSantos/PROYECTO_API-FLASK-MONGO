
import requests
from flask import Blueprint
from flask import request
from flask import render_template, redirect, url_for

from app.databases import db
from app.models.character import Character

character_bp = Blueprint("character",__name__)

CHARACTER_URL ="​https://rickandmortyapi.com/api/character"

def retrieve_id():
    for n in range(1,3):
        rsp= requests.get(f"/{CHARACTER_URL}/?page={n}")
        data = rsp.json()
        #id_list =[x['id']  for x in data['results']]
        for x in data['results']:
            return x['id'] 
    return 0

#get_character_values
def populate_character():
    id = retrieve_id()
    rsp= requests.get(f"/{CHARACTER_URL}/{id}")
    data = rsp.json()

    id = data['id'],
    name = data['name'],
    status = data['status'],
    species = data['species'],
    type = data['type'],
    gender = data['gender'],
    origin = data['origin']['name'],
    location = data['location']['name'],
    image = data['image']

    return  Character(id, name, status, species, type, gender, origin, location, image)


@character_bp.route("/character/list")
def get_all():
    character_list = db.character.find()
    return render_template('list-character.html',character_list_vw=character_list)

@character_bp.route("/character/save", methods=["POST"])
def save_data():
    if request.method == 'POST':
        new_character = populate_character()
        db.character.insert_one(new_character.to_jason())
        return redirect(url_for('character_bp.get_all'))

    return render_template('xcreate-character.html')

@character_bp.route("/character/test", methods=["GET"])
def prueba():
    return render_template('character/list-character.html')

