from .models import GameStatus

import json
import random

from fastapi import FastAPI

app = FastAPI()

move_choices = ['up', 'down', 'left', 'right']

@app.get('/')
def read_root():
    '''returns the json stored at the root level directory if it exists, otherwise just apiversion'''
    try:
        with open('battlesnake-info.json', 'r') as fo:
            battlesnake_info = json.load(fo)
            return battlesnake_info 
    except FileNotFoundError:
        return {'apiversion' : 1}

@app.post('/start', summary="this endpoint receives a request at the start of a match")
def save_start_info(info : GameStatus):
    '''dumps info param to a file (startinfo.json), returns a 200 status code'''
    with open("startinfo.json", "w") as fo:
        json.dump(info.dict(), fo) 

    return "ok" 

@app.post('/end', summary="this endpoint receives a request at the end of a match")
def save_end_info(info : GameStatus):
    '''dumps info param to a file (endinfo.json), returns a 200 status code'''
    with open("endinfo.json", "w") as fo:
        json.dump(info.dict(), fo)

    return "ok"

@app.post('/move',
summary="this endpoint receives a request every turn, expects a JSON Object with a 'move' key and an optional 'shout' key as a response")
def make_move(info : GameStatus):
    '''saves info to a file called turn{turn_number}.json, returns random move'''
    with open(f"turn{info.turn}.json", "w") as fo:
        json.dump(info.dict(), fo)

    return {
        "move" : random.choice(move_choices),
    } 