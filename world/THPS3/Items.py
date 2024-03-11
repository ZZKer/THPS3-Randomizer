from typing import Optional
from BaseClasses import ItemClassification, Item

base_thps3_item_id = 3300000

class THPS3Item(Item):
    def __init__(self, name: str, classification: ItemClassification, code: Optional[int], player: int):
        super().__init__(name, classification, code, player)

class ItemData:
    def __init__(self, id: int, classification: ItemClassification):
        self.classification = classification
        self.id = None if id is None else id + base_thps3_item_id
        self.table_index = id

item_table = {
	"Level Key": ItemData(0x0F, ItemClassification.progression),	#need  8
	#Goals will be pre-filled
	"Goal Point": ItemData(0x10, ItemClassification.progression),	#need 50
	"Stat Point": ItemData(0x11, ItemClassification.useful),		#need 50
	#Medals will be pre-filled
	"Medal": ItemData(0x12, ItemClassification.progression),		#need 3
	#Pre-filled for 3 Gold Victory
	#"Gold Medal": ItemData(0x14, ItemClassification.progression),	#need 3
	"Deck": ItemData(0x3C, ItemClassification.filler),				#need  7
	"Gymnast Plant": ItemData(0xB4, ItemClassification.filler),
	"Eggplant": ItemData(0xB5, ItemClassification.filler),
	"180 Rock N Roll": ItemData(0xB6, ItemClassification.filler),
	"Mute Invert": ItemData(0xB7, ItemClassification.filler),
	"Nosebluntslide": ItemData(0xB8, ItemClassification.progression),#1 of 4
	"Bluntslide": ItemData(0xB9, ItemClassification.useful),
	"Impossible": ItemData(0xBA, ItemClassification.useful),
	"Inward Heelflip": ItemData(0xBB, ItemClassification.useful),
	"Heelflip": ItemData(0xBC, ItemClassification.useful),
	"Varial Heelflip": ItemData(0xBD, ItemClassification.useful),
	"Pop Shove It": ItemData(0xBE, ItemClassification.useful),
	"Varial Kickflip": ItemData(0xBF, ItemClassification.useful),
	"Kickflip": ItemData(0xC0, ItemClassification.progression),		#2 of 4
	"Hardflip": ItemData(0xC1, ItemClassification.useful),
	"Nosegrab": ItemData(0xC2, ItemClassification.useful),
	"Method": ItemData(0xC3, ItemClassification.useful),
	"Cannonball": ItemData(0xC4, ItemClassification.progression),	#3 of 4
	"Del Mar Indy": ItemData(0xC5, ItemClassification.useful),
	"Airwalk": ItemData(0xC6, ItemClassification.useful),
	"Stalefish": ItemData(0xC7, ItemClassification.useful),
	"Melon": ItemData(0xC8, ItemClassification.useful),
	"One Foot Japan": ItemData(0xC9, ItemClassification.useful),
	"Sal Flip": ItemData(0xCA, ItemClassification.useful),
	"Fingerflip": ItemData(0xCB, ItemClassification.useful),
	"360 Flip": ItemData(0xCC, ItemClassification.progression),		#4 of 4
	"Varial": ItemData(0xCD, ItemClassification.useful),
	"Rocket Air": ItemData(0xCE, ItemClassification.useful),
	"Crossbone": ItemData(0xCF, ItemClassification.useful),
	"Tailgrab": ItemData(0xD0, ItemClassification.useful),
	"Benihana": ItemData(0xD1, ItemClassification.useful),
	"The 900": ItemData(0xDF, ItemClassification.useful),
	"1234 Air": ItemData(0xE0, ItemClassification.useful),
	"Double Kickflip to Indy": ItemData(0xE1, ItemClassification.useful),
	"The Fandangle II": ItemData(0xE2, ItemClassification.useful),
	"Hang Ten": ItemData(0xE3, ItemClassification.useful),
	"Wireframe Trap": ItemData(0xF0, ItemClassification.trap)
}

event_table = {
}