from BaseClasses import Location

base_location_id = 3300000


class THPS3Location(Location):
    game: str = "THPS3"

class LocationData:
	def __init__(self, region, name, location_id)
		self.region: str = region
		self.name: str = name
		self.short_location_id: int = location_id
		self.location_id: int = location_id + base_location_id

location_table = {
		#Foundry level 00
	"Foundry High Score": LocationData("Foundry", "Foundry High Score", 0x10),
	"Foundry Pro Score": LocationData("Foundry", "Foundry Pro Score", 0x11),
	"Foundry Sick Score": LocationData("Foundry", "Foundry Sick Score", 0x12),
	"Foundry SKATE": LocationData("Foundry", "Foundry SKATE", 0x13),
	"Foundry Valves": LocationData("Foundry", "Foundry Valves", 0x14),
	"Foundry Press": LocationData("FoundryGrind", "Foundry Press", 0x15),
	"Foundry Cannonball Over Halfpipe": LocationData("FoundryCannonball", "Foundry Cannonball Over Halfpipe", 0x16),
	"Foundry Control Booth": LocationData("FoundryGrind", "Foundry Control Booth", 0x17),
	"Foundry Secret Tape": LocationData("Foundry", "Foundry Secret Tape", 0x18),
	"Foundry 100 Percent": LocationData("FoundryFinal", "Foundry 100 Percent", 0x19),
	"Foundry SP Press": LocationData("Foundry", "Foundry SP Press", 0x1A),
	"Foundry SP Catwalk": LocationData("Foundry", "Foundry SP Catwalk", 0x1B),
	"Foundry SP Back Balcony": LocationData("Foundry", "Foundry SP Back Balcony", 0x1C),
	"Foundry SP Right Pipe": LocationData("Foundry", "Foundry SP Right Pipe", 0x1D),
	"Foundry SP Back Door": LocationData("Foundry", "Foundry SP Back Door", 0x1E),
	"Foundry Deck": LocationData("Foundry", "Foundry Deck", 0x1F),
		#Los Angeles level 01
	"LA High Score": LocationData("LA", "LA High Score", 0x20),
	"LA Pro Score": LocationData("LA", "LA Pro Score", 0x21),
	"LA Sick Score": LocationData("LA", "LA Sick Score", 0x22),
	"LA SKATE": LocationData("LA", "LA SKATE", 0x23),
	"LA Transformers": LocationData("LA", "LA Transformers", 0x24),
	"LA Electric Rail": LocationData("LAGrind", "LA Electric Rail", 0x25),
	"LA Elevator Grind": LocationData("LAGrind", "LA Elevator Grind", 0x26),
	"LA Kickflip Over Lobby": LocationData("LAKickflip", "LA Kickflip Over Lobby", 0x27),
	"LA Secret Tape": LocationData("LA", "LA Secret Tape", 0x28),
	"LA 100 Percent": LocationData("LAFinal", "LA 100 Percent", 0x29),
	"LA SP Quarterpipe Powerline": LocationData("LA", "LA Quarterpipe Powerline", 0x2A),
	"LA SP Highway": LocationData("LA", "LA Highway", 0x2B),
	"LA SP Theater": LocationData("LA", "LA Theater", 0x2C),
	"LA SP 4": LocationData("LA", "LA SP 4", 0x2D), #need better name
	"LA SP 5": LocationData("LA", "LA SP 5", 0x2E), #need better name
	"LA Deck": LocationData("LA", "LA Deck", 0x2F),
		#Rio de Janeiro level 02
	"Rio Medal": LocationData("Rio", "Rio Medal", 0x30),
	#"Rio Silver": LocationData("Rio", "Rio Silver", 0x31),
	#"Rio Gold": LocationData("Rio", "Rio Gold", 0x32),
	"Rio SP Quicksilver Powerline": LocationData("Rio", "Rio SP Quicksilver Powerline", 0x3A),
	"Rio SP Quicksilver": LocationData("Rio", "Rio SP Quicksilver", 0x3B),
	"Rio SP Middle Powerline": LocationData("Rio", "Rio SP Middle Powerline", 0x3C),
	"Rio SP Alley": LocationData("Rio", "Rio SP Alley", 0x3D),
	"Rio SP Balcony": LocationData("Rio", "Rio SP Balcony", 0x3E),
	"Rio Deck": LocationData("Rio", "Rio Deck", 0x3F)#,
	#REMEMBER TO UNCOMMENT THE COMMA
}

location_descriptions = {
    "Foundry High Score": "High Score of 10,000 points in Foundry",
    "Foundry Pro Score": "Pro Score of 40,000 points in Foundry",
    "Foundry Sick Score": "Sick Score of 100,000 points in Foundry",
	"Foundry SKATE": "Collect the SKATE letters in Foundry",
	"Foundry Valves": "Unjam the 5 valves in Foundry",
	"Foundry Press": "Activate the press in Foundry",
	"Foundry Cannonball": "Cannonball over the halfpipe in Foundry",
	"Foundry Control Booth": "Grind the control booth at the back of Foundry",
	"Foundry Secret Tape": "Find the secret tape high up in Foundry",
	"Foundry 100 Percent": "All goals, stats, and deck in Foundry",
	"Foundry SP Press": "Stat Point above the press in Foundry",
	"Foundry SP Catwalk": "Stat Point on the left side of the catwalk in Foundry",
	"Foundry SP Back Balcony": "Stat Point above the control booth on the left side of the balcony in Foundry",
	"Foundry SP Right Pipe": "Stat Point on right pipe near start in Foundry",
	"Foundry SP Back Door": "Stat Point by the back door behind the control booth in Foundry",
	"Foundry Deck": "Deck found at center of catwalks in Foundry",
    "Foundry":
        """
        The group of all items in Foundry, the first level.
		"""
}