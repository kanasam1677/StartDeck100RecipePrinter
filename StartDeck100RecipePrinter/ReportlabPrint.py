import dataclasses

@dataclasses.dataclass(frozen=True)
class DeckData:
    deckNum:str
    title:str
    description:str
    cardListFilePath:str
