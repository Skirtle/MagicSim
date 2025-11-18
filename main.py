from dataclasses import dataclass, field

@dataclass
class Card:
    name: str
    card_types: list[str] = field(default_factory=list[str])
    card_subtypes: list[str] = field(default_factory=list[str])
    
    
@dataclass
class CreatureCard(Card):
    ...
    
    
    
if __name__ == "__main__":
    bear = CreatureCard("Bear")
    
    print(bear)