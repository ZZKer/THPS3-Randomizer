from BaseClasses import ItemClassification, Item

class THPS3Item(Item):
    def __init__(self, name: str, classification: ItemClassification, code: Optional[int], player: int):
        super().__init__(name, classification, code, player)

