from models.player import Player
from common.world import world
from configuration import settings

import json
from pathlib import Path


def initialize_player(name, player_id, session):
    player = session.query(Player).filter(Player.id == player_id).first()
    if not player:
        player = Player(id=player_id, name=name)
        session.add(player)
        player.x = settings.player['starting_x']
        player.y = settings.player['starting_y']
        player.health = settings.player['starting_health']
        player.max_health = settings.player['starting_max_health']
        player.thirst = settings.player['starting_thirst']
        player.max_thirst = settings.player['starting_max_thirst']
        player.mana = settings.player['starting_mana']
        player.max_mana = settings.player['starting_max_mana']
        session.commit()
    return player


def initialize_world():
    if not world['tiles']:
        world_file_path = Path(__file__).resolve().parent.parent.joinpath('configuration', 'world.json')
        if world_file_path.exists():
            world_file = open(world_file_path, 'r')
            world['tiles'] = json.loads(world_file.read())
        else:
            raise Exception('World file not found. Check /configuration/world.json')
