
infile = open("Luck5dataSheet.py","r") # just change luck# to 1-5

Legendary = 0
Rare = 0
uncommon = 0
common = 0
Nothing = 0
    
    
loot = infile.readline().strip()
while loot != "-1" :
    if loot == "Legendary" :
        Legendary += 1
    elif loot == "Rare" :   
        Rare += 1
    elif loot == "uncommon" :
        uncommon += 1
    elif loot == "common" :
        common += 1
    elif loot == "Nothing" :
        Nothing += 1
    loot = infile.readline().strip()

print("Legendary drops: ", Legendary)
print("Rare drops: ", Rare)
print("Uncommon drops: ", uncommon)
print("Common drops: ", common)
print("Nothing drops: ", Nothing)

    
