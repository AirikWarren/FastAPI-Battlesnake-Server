from typing import List
from typing import Optional
from pydantic import BaseModel

class Coordinates(BaseModel):
    x : int
    y : int

class BattleSnake(BaseModel):
    ''' What you're all here for 
    - **id** - Unique identifier for this Battlesnake in the context of the current Game.
    - **name** - Name given to this Battlesnake by its author.
    - **health** - Health value of this Battlesnake, between 0 and 100 inclusively.
    - **body** - List of Coordinates representing this Battlesnake's location on the game board. This List is ordered from head to tail.
    - **latency** - The previous response time of this Battlesnake, in milliseconds. "0" means the Battlesnake timed out and failed to respond.
    - **head** - Coordinates for this Battlesnake's head. Equivalent to the first element of the body list.
    - **length** -  Length of this Battlesnake from head to tail. Equivalent to the length of the body list.
    - **shout** - Message shouted by this Battlesnake on the previous turn.
    - **squad** - The squad that the Battlesnake belongs to. Used to identify squad members in Squad Mode games.
    '''
    id : str
    name : str
    health : int
    body : List[Coordinates]
    latency : str
    head : Coordinates 
    length : int
    shout : Optional[str]
    squad : Optional[str]

class Game(BaseModel):
    ''' Info about config / meta info on a game 
    - **id** - A unique identifier for this Game.
    - **ruleset** - Information about the ruleset being used to run this game.
    - **timeout** - How much time a snake has to respond to requests for this Game.
    '''
    id : str
    ruleset : dict
    timeout : int

class GameBoard(BaseModel):
    ''' Represents the game board, traditional cartesian grid (ie. positive-y axis = up, positive-x axis = right) rather than a y-inverted grid 
    you might assume
    - **height** - Height of the game board.
    - **width** - Width of the game board.
    - **food** - List of Coordinates representing food locations on the game board.
    - **hazards** - List of Coordinates representing hazardous locations on the game board. These will only appear in some game modes.
    - **snakes** - List of Battlesnake Objects representing all Battlesnakes remaining on the game board.
    '''
    height : int
    width : int
    food : List[Coordinates]
    hazards : Optional[List[Coordinates]]
    snakes : Optional[List[BattleSnake]]

class GameStatus(BaseModel):
    '''Info about all the game state, sent to the server at the /start, /move, and /end endpoints and with every request

    - **game** - Game Object describing the game being played.
    - **turn** - Turn number of the game being played (0 for new games)
    - **board** - Board Object describing the game board on this turn
    - **you** - Battlesnake Object describing your Battlesnake.
    '''
    game : Game
    turn : int
    board : GameBoard
    you : BattleSnake