# world/THPS3/__init__.py

import settings
import typing
from .options import MyGameOptions  # the options we defined earlier
from .items import mygame_items  # data used below to add items to the World
from .locations import mygame_locations  # same as above
from worlds.AutoWorld import World
from BaseClasses import Region, Location, Entrance, Item, RegionType, ItemClassification


class MyGameItem(Item):  # or from Items import MyGameItem
    game = "THPS3"  # name of the game/world this item is from


class MyGameLocation(Location):  # or from Locations import MyGameLocation
    game = "THPS3"  # name of the game/world this location is in


class MyGameSettings(settings.Group):
    class RomFile(settings.SNESRomPath):
        """Insert help text for host.yaml here."""

    rom_file: RomFile = RomFile("MyGame.sfc")


class MyGameWorld(World):
    """Tony Hawk's Pro Skater 3 is a skateboarding game for the PSx."""
    game = "THPS3"  # name of the game/world
    options_dataclass = MyGameOptions  # options the player can set
    options: MyGameOptions  # typing hints for option results
    settings: typing.ClassVar[MyGameSettings]  # will be automatically assigned from type hint
    topology_present = True  # show path to required location checks in spoiler

    # ID of first item and location, could be hard-coded but code may be easier
    # to read with this as a property.
    base_id = 1234
    # instead of dynamic numbering, IDs could be part of data

    # The following two dicts are required for the generation to know which
    # items exist. They could be generated from json or something else. They can
    # include events, but don't have to since events will be placed manually.
    item_name_to_id = {name: id for
                       id, name in enumerate(mygame_items, base_id)}
    location_name_to_id = {name: id for
                           id, name in enumerate(mygame_locations, base_id)}

    # Items can be grouped using their names to allow easy checking if any item
    # from that group has been collected. Group names can also be used for !hint
    item_name_groups = {
        "weapons": {"sword", "lance"},
    }