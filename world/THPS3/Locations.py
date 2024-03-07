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
	"Foundry Cannonball": LocationData("FoundryCannonball", "Foundry Cannonball", 0x16),
	"Foundry Control Booth": LocationData("FoundryGrind", "Foundry Control Booth", 0x17),
	"Foundry Secret Tape": LocationData("Foundry", "Foundry Secret Tape", 0x18),
	"Foundry 100 Percent": LocationData("FoundryFinal", "Foundry 100 Percent", 0x19),
	"Foundry SP Press": LocationData("Foundry", "Foundry SP Press", 0x1A),
	"Foundry SP Catwalk": LocationData("Foundry", "Foundry SP Catwalk", 0x1B),
	"Foundry SP Back Balcony": LocationData("Foundry", "Foundry SP Back Balcony", 0x1C),
	"Foundry SP Right Pipe": LocationData("Foundry", "Foundry SP Right Pipe", 0x1D),
	"Foundry SP Back Door": LocationData("Foundry", "Foundry SP Back Door", 0x1E),
	"Foundry Deck": LocationData("Foundry", "Foundry Deck", 0x1F),

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