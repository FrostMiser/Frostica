import random

from common.helpers import drain_player_hunger_and_thirst, get_hunger_and_thirst_warnings
from common.world import get_tile_from
from models.item import Item
from models.player import Player
from models.player_inventory import PlayerInventory


def run_command(message, session):
    player = session.query(Player).filter(Player.id == message.author.id).first()

    if not player.main_hand_item or not player.main_hand_item.can_chop:
        return 'You don\'t have anything equipped that you can chop with.'

    tile = get_tile_from(player.x, player.y, session)
    if not tile.can_chop:
        response = 'You didn\'t find anything here, maybe try somewhere else.'
    else:
        item_lookup_results = session.query(Item).filter(Item.chop_drop_chance > 0).all()
        possible_items = {item.id: item.chop_drop_chance for item in item_lookup_results}

        chopped_item_id = random.choices(list(possible_items.keys()), possible_items.values())[0]
        chopped_item = session.query(Item).filter(Item.id == chopped_item_id).first()

        player_inventory = session.query(PlayerInventory).filter(PlayerInventory.player_id == message.author.id,
                                                                 PlayerInventory.item_id == chopped_item.id).first()
        drain_player_hunger_and_thirst(player)

        if player_inventory:
            player_inventory.item_amount += 1
        else:
            player.inventory.append(PlayerInventory(player_id=player.id, item_id=chopped_item.id, item_amount=1))
        response = ':evergreen_tree: {} chopped a tree and found a {}'.format(player.name, chopped_item.name)
        response += get_hunger_and_thirst_warnings(player)
    return response
