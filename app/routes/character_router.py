
import requests
from flask import Blueprint
from flask import request
from flask import render_template, redirect, url_for

#from pymongo import ASCENDING
from app.databases import db
from app.models.character import Character

character_bp = Blueprint("character",__name__)

CHARACTER_URL = '​https://rickandmortyapi.com/api/character'
urlx ="https://rickandmortyapi.com/api/character"

def retrieve_id():
    id_list = []
    for n in range(1,3):
        payload ={"page":n}
        rsp= requests.get(urlx,params=payload)
        data = rsp.json()
        id_list =[x['id']  for x in data['results']]

    return id_list

def populate_character(id):
    rsp= requests.get(f'{urlx}/{str(id)}')
    data = rsp.json()
    
    id_ibj = data['id']
    name = data['name']
    status = data['status']
    species = data['species']
    type_ch = data['type']
    gender = data['gender']
    origin = data['origin']['name']
    location = data['location']['name']
    image = data['image']
    episode = data['episode']
    lista =[]
    for url_episode in episode:
        rsp= requests.get(url_episode)
        data = rsp.json()
        #lista =data['name']
        lista.append(data['name'])
    print(type(lista),"tipo")
    return  Character(id_ibj, name, status, species, type_ch, gender, origin, location, image,lista)

@character_bp.route("/character/list")
def get_all():
    from pymongo import ASCENDING
    character_list = db.character.find().sort('id',ASCENDING)
    return render_template('character/list-character.html',character_list_vw=character_list)

@character_bp.route("/character/save", methods=["GET","POST"])
def save_data():
    if request.method == 'POST':
        for id in retrieve_id():
            new_character = populate_character(id)
            db.character.insert_one(new_character.to_json())

        return redirect(url_for('character.get_all'))

    return render_template('character/create-character.html')

@character_bp.route("/character/details/<int:id>", methods=["GET"])
def show_details(id):
    #found_character = db.character.find_one({"id":int(id)})
    found_character = db.character.find_one({"id":id})

    return render_template('character/details-character.html',obj=found_character)

@character_bp.route("/character/test", methods=["GET"])
def prueba():
    return render_template('character/list-character.html')
