from common.helpers import get_item_by_name
from configuration import settings  # pylint: disable=no-name-in-module
from models.item import Item
from models.recipe import Recipe
from models.recipe_ingredient import RecipeIngredient
from models.tile import Tile


def run_command(message, session):
    if message.author.id not in settings.general['admins']:
        response = 'You must be an admin to use this command.'
    else:
        _populate_items(session)
        _populate_tiles(session)
        _populate_recipes(session)
        response = 'Setup complete.'
    return response


def _populate_items(session):
    session.query(Item).delete()

    # ToDo Move this to configuration
    # 1 - 200 mined items
    session.add(Item(id=1, name='magic ore', mine_drop_chance=5))
    session.add(Item(id=2, name='stone', forage_drop_chance=10, mine_drop_chance=100))
    # session.add(Item(id=3, name='iron ore', mine_drop_chance=15))
    # session.add(Item(id=4, name='gold ore', mine_drop_chance=5))
    # session.add(Item(id=5, name='copper ore', mine_drop_chance=10))
    # session.add(Item(id=6, name='lead ore', mine_drop_chance=10))
    # session.add(Item(id=7, name='nickel ore', mine_drop_chance=7))
    # session.add(Item(id=8, name='tin ore', mine_drop_chance=8))
    # session.add(Item(id=9, name='silver ore', mine_drop_chance=3))
    # session.add(Item(id=10, name='platinum ore', mine_drop_chance=1))
    # session.add(Item(id=11, name='zinc ore', mine_drop_chance=7))

    # session.add(Item(id=12, name='unrefined diamond', mine_drop_chance=1))
    # session.add(Item(id=13, name='unrefined ruby', mine_drop_chance=2))
    # session.add(Item(id=14, name='unrefined topaz', mine_drop_chance=2))
    # session.add(Item(id=15, name='unrefined sapphire', mine_drop_chance=2))
    # session.add(Item(id=16, name='unrefined jade', mine_drop_chance=2))
    # session.add(Item(id=17, name='unrefined amber', mine_drop_chance=2))
    # session.add(Item(id=18, name='unrefined lapis lazuli', mine_drop_chance=2))
    # session.add(Item(id=19, name='unrefined turquoise', mine_drop_chance=2))
    # session.add(Item(id=20, name='unrefined amethyst', mine_drop_chance=2))
    # session.add(Item(id=21, name='unrefined emerald', mine_drop_chance=2))
    # session.add(Item(id=22, name='unrefined opal', mine_drop_chance=2))
    # session.add(Item(id=23, name='unrefined quartz', mine_drop_chance=2))
    # session.add(Item(id=24, name='unrefined peridot', mine_drop_chance=2))
    # session.add(Item(id=25, name='unrefined onyx', mine_drop_chance=2))

    # 201 - 400 foraged items
    session.add(Item(id=201, name='stick', forage_drop_chance=10))
    session.add(Item(id=202, name='strawberry', forage_drop_chance=15, edible=True, hunger_satisfaction=1,
                     thirst_satisfaction=2))
    session.add(Item(id=203, name='grapefruit', forage_drop_chance=4, edible=True, hunger_satisfaction=4,
                     thirst_satisfaction=7))
    session.add(Item(id=204, name='pineapple', forage_drop_chance=4, edible=True, hunger_satisfaction=7,
                     thirst_satisfaction=10))
    session.add(Item(id=205, name='cucumber', forage_drop_chance=4, edible=True, hunger_satisfaction=7,
                     thirst_satisfaction=7))
    session.add(Item(id=206, name='blueberry', forage_drop_chance=40, edible=True, hunger_satisfaction=1,
                     thirst_satisfaction=1))
    session.add(Item(id=207, name='cherry', forage_drop_chance=20, edible=True, hunger_satisfaction=1,
                     thirst_satisfaction=2))
    session.add(Item(id=208, name='banana', forage_drop_chance=7, edible=True, hunger_satisfaction=2))
    session.add(Item(id=209, name='orange', forage_drop_chance=7, edible=True, hunger_satisfaction=2,
                     thirst_satisfaction=3))
    session.add(Item(id=210, name='pear', forage_drop_chance=7, edible=True, hunger_satisfaction=2,
                     thirst_satisfaction=3))
    session.add(Item(id=211, name='carrot', forage_drop_chance=10, edible=True, hunger_satisfaction=2))
    session.add(Item(id=212, name='broccoli', forage_drop_chance=5, edible=True, hunger_satisfaction=7))
    session.add(Item(id=213, name='spinach', forage_drop_chance=5, edible=True, hunger_satisfaction=1))
    session.add(Item(id=214, name='cauliflower', forage_drop_chance=1, edible=True, hunger_satisfaction=9))
    session.add(Item(id=215, name='radish', forage_drop_chance=2, edible=True, hunger_satisfaction=9))
    session.add(Item(id=216, name='lemon', forage_drop_chance=2, edible=True, hunger_satisfaction=2,
                     thirst_satisfaction=1))
    session.add(Item(id=217, name='watermelon', forage_drop_chance=1, edible=True, hunger_satisfaction=5,
                     thirst_satisfaction=15))
    session.add(Item(id=218, name='lettuce', forage_drop_chance=5, edible=True, hunger_satisfaction=1,
                     thirst_satisfaction=2))
    session.add(Item(id=219, name='salad', edible=True, hunger_satisfaction=15,
                     thirst_satisfaction=30))

    # 401 - 600 hunting items
    session.add(Item(id=401, name='rat meat', hunt_drop_chance=100, chop_drop_chance=1))
    session.add(Item(id=402, name='rat fur', hunt_drop_chance=100, chop_drop_chance=1))
    session.add(Item(id=403, name='chicken meat', hunt_drop_chance=5))
    session.add(Item(id=404, name='feather', hunt_drop_chance=5))
    session.add(Item(id=405, name='boar meat', hunt_drop_chance=1))
    session.add(Item(id=406, name='boar hide', hunt_drop_chance=1))
    session.add(Item(id=407, name='turkey meat', hunt_drop_chance=1))

    # 601 - 800 wood chopping items
    session.add(Item(id=601, name='wood', chop_drop_chance=100))

    # 801 - 1200 crafted items, tools, armor, etc
    session.add(Item(id=801, name='basic pickaxe', equipable=True, can_mine=True))
    session.add(Item(id=802, name='basic axe', equipable=True, can_chop=True))
    session.add(Item(id=803, name='basic hunting knife', equipable=True, can_hunt=True))
    session.commit()


def _populate_tiles(session):
    session.query(Tile).delete()

    # This tile shouldn't exist normally, the ID for this tile is set for parts of the world without a tile in
    # common.world.get_tile_id
    session.add(Tile(id=-1, name='barrier', display_emoji='🚫', traversable=False))

    # All other tiles for the world
    session.add(Tile(id=0, name='snow covered mountains', display_emoji='🗻', can_hunt=True,
                     can_mine=True, hunger_drain_amount=15, thirst_drain_amount=15))
    session.add(Tile(id=1, name='flat snow', display_emoji='⬜', can_hunt=True,
                     hunger_drain_amount=1, thirst_drain_amount=2))
    session.add(Tile(id=2, name='water', display_emoji='🔷', traversable=False))
    session.add(Tile(id=3, name='trees', display_emoji='🌲', can_chop=True,
                     can_forage=True, can_hunt=True, hunger_drain_amount=1, thirst_drain_amount=1))
    session.add(Tile(id=4, name='mountains', display_emoji='⛰️', can_hunt=True, can_mine=True,
                     hunger_drain_amount=10, thirst_drain_amount=10))
    session.commit()


def _populate_recipes(session):
    session.query(Recipe).delete()
    session.query(RecipeIngredient).delete()

    # Basic Pickaxe
    basic_pickaxe = Recipe(id=1, name='basic pickaxe', item=get_item_by_name('basic pickaxe', session))
    session.add(basic_pickaxe)

    basic_pickaxe_ingredient_1 = RecipeIngredient(recipe_id=basic_pickaxe.id, item=get_item_by_name('stone', session),
                                                  item_amount=7)
    session.add(basic_pickaxe_ingredient_1)
    basic_pickaxe_ingredient_2 = RecipeIngredient(recipe_id=basic_pickaxe.id, item=get_item_by_name('stick', session),
                                                  item_amount=4)
    session.add(basic_pickaxe_ingredient_2)
    session.commit()

    # Basic axe
    basic_axe = Recipe(id=2, name='basic axe', item=get_item_by_name('basic axe', session))
    session.add(basic_axe)

    basic_axe_ingredient_1 = RecipeIngredient(recipe_id=basic_axe.id, item=get_item_by_name('stone', session),
                                              item_amount=5)
    session.add(basic_axe_ingredient_1)
    basic_axe_ingredient_2 = RecipeIngredient(recipe_id=basic_axe.id, item=get_item_by_name('stick', session),
                                              item_amount=4)
    session.add(basic_axe_ingredient_2)

    # Basic hunting knife
    basic_hunting_knife = Recipe(id=3, name='basic hunting knife',
                                 item=get_item_by_name('basic hunting knife', session))
    session.add(basic_hunting_knife)

    basic_hunting_knife_ingredient_1 = RecipeIngredient(recipe_id=basic_hunting_knife.id,
                                                        item=get_item_by_name('stone', session),
                                                        item_amount=4)
    session.add(basic_hunting_knife_ingredient_1)
    basic_hunting_knife_ingredient_2 = RecipeIngredient(recipe_id=basic_hunting_knife.id,
                                                        item=get_item_by_name('stick', session),
                                                        item_amount=2)
    session.add(basic_hunting_knife_ingredient_2)

    # Salad
    salad = Recipe(id=4, name='salad',
                   item=get_item_by_name('salad', session))
    session.add(salad)

    salad_ingredient_1 = RecipeIngredient(recipe_id=salad.id,
                                          item=get_item_by_name('lettuce', session),
                                          item_amount=4)
    session.add(salad_ingredient_1)
    salad_ingredient_2 = RecipeIngredient(recipe_id=salad.id,
                                          item=get_item_by_name('spinach', session),
                                          item_amount=2)
    session.add(salad_ingredient_2)

    salad_ingredient_3 = RecipeIngredient(recipe_id=salad.id,
                                          item=get_item_by_name('carrot', session),
                                          item_amount=1)
    session.add(salad_ingredient_3)

    session.commit()
