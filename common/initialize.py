from sqlalchemy.orm import sessionmaker
from models.player import Player
from common.database import db_engine


def initialize_player(name, player_id):
    session_maker = sessionmaker(bind=db_engine)
    session = session_maker()
    player = session.query(Player).filter(Player.id == player_id).first()
    if not player:
        new_player = Player(id=player_id, name=name)
        session.add(new_player)
        session.commit()
