from charachter import Player
from item import Item
from room import Room

rooms = {
    "dungeon" : Room(
        "Dungeon",
         "Ye find yeself in yon dungeon. Ye see a SCROLL. Behind ye SCROLL is a FLASK. Obvious exits are NORTH, SOUTH, and DENNIS"
        ),
    "parapets" : Room(
        "Parapets",
        "You arrive at parapets. Ye see a rope. Obvious exits are SOUTH."
        ),
    "embankment" : Room(
        "Embankment",
        "Or maybe a chasm. You can't decide which. Anyway, ye spies a TRINKET. Obvious exits are NORTH."
    ),
    "Dennis" : Room(
        "Dennis",
        "Ye arrive at Dennis. He wears a sporty frock coat and a long jimber jam. He paces about nervously. Obvious exits are NOT DENNIS."
    )
}

# Link rooms together
rooms["dungeon"].north_to = rooms["parapets"]
rooms["dungeon"].south_to = rooms["embankment"]
rooms["dungeon"].dennis_to = rooms["Dennis"]
rooms["parapets"].south_to = rooms["dungeon"]
rooms["embankment"].north_to = rooms["dungeon"]
rooms["Dennis"].not_dennis_to = rooms["dungeon"]

player = Player(current_room=rooms["dungeon"])
print(player.current_room.description)

while True:

    input_ = raw_input("What wouldst thou deau? ").lower()

    if getattr(player.current_room, input_ + "_to"):
        player.current_room = getattr(player.current_room, input_ + "_to")
        print(player.current_room.description)