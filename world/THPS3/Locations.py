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
	"LA SP Quarterpipe Powerline": LocationData("LA", "LA SP Quarterpipe Powerline", 0x2A),
	"LA SP Highway": LocationData("LA", "LA SP Highway", 0x2B),
	"LA SP Theater": LocationData("LA", "LA SP Theater", 0x2C),
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
	"Rio Deck": LocationData("Rio", "Rio Deck", 0x3F),
		#Suburbia level 03
	"Suburbia High Score": LocationData("Suburbia", "Suburbia High Score", 0x40),
	"Suburbia Pro Score": LocationData("Suburbia", "Suburbia Pro Score", 0x41),
	"Suburbia Sick Score": LocationData("Suburbia", "Suburbia Sick Score", 0x42),
	"Suburbia SKATE": LocationData("Suburbia", "Suburbia SKATE", 0x43),
	"Suburbia Appliances": LocationData("Suburbia", "Suburbia Appliances", 0x44),
	"Suburbia Dishes": LocationData("Suburbia", "Suburbia Dishes", 0x45),
	"Suburbia Ice Cream Man": LocationData("Suburbia", "Suburbia Ice Cream Man", 0x46),
	"Suburbia 360 Flip The Weathervane": LocationData("Suburbia360Flip", "Suburbia 360 Flip The Weathervane", 0x47),
	"Suburbia Secret Tape": LocationData("Suburbia", "Suburbia Secret Tape", 0x48),
	"Suburbia 100 Percent": LocationData("SuburbiaFinal", "Suburbia 100 Percent", 0x49),
	"Suburbia SP Flat Roof": LocationData("Suburbia", "Suburbia SP Flat Roof", 0x4A),
	"Suburbia SP Powerline": LocationData("Suburbia", "Suburbia SP Powerline", 0x4B),
	"Suburbia SP Above Mobile Home": LocationData("Suburbia", "Suburbia SP Above Mobile Home", 0x4C),
	"Suburbia SP 4": LocationData("Suburbia", "Suburbia SP 4", 0x4D), #need better name
	"Suburbia SP Mobile Home": LocationData("Suburbia", "Suburbia SP Mobile Home", 0x4E),
	"Suburbia Deck": LocationData("Suburbia", "Suburbia Deck", 0x4F),
		#Airport 04
	"Airport High Score": LocationData("Airport", "Airport High Score", 0x50),
	"Airport Pro Score": LocationData("Airport", "Airport Pro Score", 0x51),
	"Airport Sick Score": LocationData("Airport", "Airport Sick Score", 0x52),
	"Airport SKATE": LocationData("Airport", "Airport SKATE", 0x53),
	"Airport Flags": LocationData("AirportGrind", "Airport Flags", 0x54),
	"Airport Lost Luggage": LocationData("Airport", "Airport Lost Luggage", 0x55),
	"Airport Nosebluntslide Sign": LocationData("AirportNosebluntslide", "Airport Nosebluntslide Sign", 0x56),
	"Airport Grind The Plane": LocationData("AirportGrind", "Airport Grind The Plane", 0x57),
	"Airport Secret Tape": LocationData("Airport", "Airport Secret Tape", 0x58),
	"Airport 100 Percent": LocationData("AirportFinal", "Airport 100 Percent", 0x59),
	"Airport SP Light": LocationData("Airport", "Airport SP Light", 0x5A),
	"Airport SP Escalator Light": LocationData("Airport", "Airport SP Escalator Light", 0x5B),
	"Airport SP Metal Detector": LocationData("Airport", "Airport SP Metal Detector", 0x5C),
	"Airport SP Sign": LocationData("Airport", "Airport SP Sign", 0x5D), #need better name
	"Airport SP Rail": LocationData("Airport", "Airport SP Rail", 0x5E),
	"Airport Deck": LocationData("Airport", "Airport Deck", 0x5F),
		#Skater Island level 05
	"Skater Island Medal": LocationData("Skater Island", "Skater Island Medal", 0x60),
	#"Skater Island Silver": LocationData("Skater Island", "Skater Island Silver", 0x61),
	#"Skater Island Gold": LocationData("Skater Island", "Skater Island Gold", 0x62),
	"Skater Island SP Doorway Gap": LocationData("Skater Island", "Skater Island SP Doorway Gap", 0x6A),
	"Skater Island SP Halfpipe": LocationData("Skater Island", "Skater Island SP Halfpipe", 0x6B),
	"Skater Island SP Doorway Rail": LocationData("Skater Island", "Skater Island SP Doorway Rail", 0x6C),
	"Skater Island SP THPS3 Sign": LocationData("Skater Island", "Skater Island SP THPS3 Sign", 0x6D),
	"Skater Island SP Pool": LocationData("Skater Island", "Skater Island SP Pool", 0x6E),
	"Skater Island Deck": LocationData("Skater Island", "Skater Island Deck", 0x6F),
		#Canada 06
	"Canada High Score": LocationData("Canada", "Canada High Score", 0x70),
	"Canada Pro Score": LocationData("Canada", "Canada Pro Score", 0x71),
	"Canada Sick Score": LocationData("Canada", "Canada Sick Score", 0x72),
	"Canada SKATE": LocationData("Canada", "Canada SKATE", 0x73),
	"Canada Totem Poles": LocationData("Canada", "Canada Totem Poles", 0x74),
	"Canada Blow Up Tree": LocationData("Canada", "Canada Blow Up Tree", 0x75),
	"Canada Nosegrind Tree": LocationData("CanadaNosegrind", "Canada Nosegrind Tree", 0x76),
	"Canada Ollie Over Pool": LocationData("Canada", "Canada Ollie Over Pool", 0x77),
	"Canada Secret Tape": LocationData("Canada", "Canada Secret Tape", 0x78),
	"Canada 100 Percent": LocationData("CanadaFinal", "Canada 100 Percent", 0x79),
	"Canada SP Rooftop": LocationData("Canada", "Canada SP Rooftop", 0x7A),
	"Canada SP Banner": LocationData("Canada", "Canada SP Banner", 0x7B),
	"Canada SP Train Tracks": LocationData("Canada", "Canada SP Train Tracks", 0x7C),
	"Canada SP Park Rail": LocationData("Canada", "Canada SP Park Rail", 0x7D), 
	"Canada SP Ramp": LocationData("Canada", "Canada SP Ramp", 0x7E),
	"Canada Deck": LocationData("Canada", "Canada Deck", 0x7F),
		#Tokyo level 07
	"Tokyo Medal": LocationData("Tokyo", "Tokyo Medal", 0x80),
	#"Tokyo Silver": LocationData("Tokyo", "Tokyo Silver", 0x81),
	#"Tokyo Gold": LocationData("Tokyo", "Tokyo Gold", 0x82),
	"Tokyo SP Glass": LocationData("Tokyo", "Tokyo SP Glass", 0x8A),
	"Tokyo SP Left Quarterpipe": LocationData("Tokyo", "Tokyo SP Left Quarterpipe", 0x8B),
	"Tokyo SP Bridge": LocationData("Tokyo", "Tokyo SP Bridge", 0x8C),
	"Tokyo SP Hologram": LocationData("Tokyo", "Tokyo SP Hologram", 0x8D),
	"Tokyo SP Right Rail": LocationData("Tokyo", "Tokyo SP Right Rail", 0x8E),
	"All Goals and Medals": LocationData("AllFinal", "All Goals and Medals", 0x8F),
		#Downhill level 08
	"Downhill SP Trees": LocationData("Downhill", "Downhill SP Trees", 0x90),
	"Downhill SP Grind 1": LocationData("Downhill", "Downhill SP Grind 1", 0x91),
	"Downhill SP Grind 2": LocationData("Downhill", "Downhill SP Grind 2", 0x92),
	"Downhill SP Grind 3": LocationData("Downhill", "Downhill SP Grind 3", 0x93),
	"Downhill SP Grind 4": LocationData("Downhill", "Downhill SP Grind 4", 0x94),
	"Downhill SP Grind 5": LocationData("Downhill", "Downhill SP Grind 5", 0x95),
	"Downhill SP Grind 6": LocationData("Downhill", "Downhill SP Grind 6", 0x96),
	"Downhill SP Grind 7": LocationData("Downhill", "Downhill SP Grind 7", 0x97),
	"Downhill SP Grind 8": LocationData("Downhill", "Downhill SP Grind 8", 0x98),
	"Downhill SP Grind 9": LocationData("Downhill", "Downhill SP Grind 9", 0x99)
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
	"Foundry Deck": "Deck found at center of the catwalks in Foundry",
    "Foundry":
        """
        The group of all items in Foundry, the first level.
		"""
}