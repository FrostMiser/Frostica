from sqlalchemy.orm import sessionmaker

from common.database import db_engine
from common.world import world, get_tile, get_tile_id, get_tile_from
from models.player import Player
from models.tile import Tile


def _is_traversable(x, y, session):
    return get_tile_from(x, y, session).traversable


def _move(player, session, x=0, y=0):
    traversable = _is_traversable(player.x + x, player.y + y, session)
    if traversable:
        player.x += x
        player.y += y
    return traversable


direction_dict = {
    'north': [0, -1],
    'south': [0, 1],
    'east': [1, 0],
    'west': [-1, 0]
}


def _move_direction(player, session, direction):
    if _move(player, session, *direction_dict[direction]):
        return f"you move {direction}\n"
    else:
        x, y = direction_dict[direction]
        return f"you can't traverse (move over) {get_tile_from(player.x + x, player.y + y, session).name}\n"


def run_command(message, message_content):
    session_maker = sessionmaker(bind=db_engine)
    session = session_maker()
    player = session.query(Player).get(message.author.id)

    direction = ''.join(message_content.split(" ")[1:]) if len(message_content.split(" ")) > 1 else None

    if direction in direction_dict:
        response = _move_direction(player, session, direction)
    else:
        return ("You must say which direction you want to use with !use <direction>.\n"
                "valid directions are north, east, south, and west.")

    session.commit()

    current_tile_id = get_tile_id(player.x, player.y)
    current_tile = get_tile(current_tile_id, session)

    response += f"`> you are at x: {player.x}, y: {player.y} ({current_tile.name})`"
    return response
