from BaseClasses import Location

base_location_id = 3300000


class THPS3Location(Location):
    game: str = "THPS3"

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
	"Foundry SP Left Balcony": "Stat Point above the control booth on the left side of the balcony in Foundry",
	"Foundry SP Right Pipe": "Stat Point on right pipe near start in Foundry",
	"Foundry SP Back Door": "Stat Point by the back door behind the control booth in Foundry",
	"Foundry Deck": "Deck found at center of catwalks in Foundry",
    "Foundry":
        """
        The group of all items in Foundry, the first level.
		"""
}