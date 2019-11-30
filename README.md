# tabletopRPG
Goal:
Automate core processes of tabletop RPGs



Includes:

Python package to generate a DnD character with either randomized stats or the per-Character Creation rules default stats.

diceBag.py is a class object that includes 7 methods for throwing a pseudorandom dice: d4, d6, d8, d10, d12, d20, and d100.

classes.py is a work in progress that establishes a character class to be associated after character generation. It includes getter's for private stats, attributes, conditions and hitDie related to a character.

abilityScoreGenerator.py is a working Character Generator that promps the option choose the default stat allotment or iterate through the Character Creation rules to generate a character with randomized stats within the 5ed rules.

lib.py is a separate copy of abilityScoreGenerator.py for testing class integrations.

Folders included npcNames and RPG Scripts. npcNames includes data of male and female sample names from various fantasy races for a work in progress NPC generator to be integrated with lib for automated full character NPC's.

RPG Scripts includes experimental loot table functions for item drop rates.
