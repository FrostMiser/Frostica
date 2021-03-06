"""Stores settings such as the database path. Rename this file to settings.py and update the values as needed."""

general = {
    'database_engine': 'sqlite:///path/to/database.db',
    'api_token': 'example',
    'admins': []  # Add numeric ID of the admin in this list. Multiple admin IDs can be added.
}

player = {
    'starting_x': 1,
    'starting_y': 1,
    'starting_health': 100,
    'starting_max_health': 100,
    'starting_thirst': 100,
    'starting_max_thirst': 100,
    'starting_mana': 0,
    'starting_max_mana': 0
}
