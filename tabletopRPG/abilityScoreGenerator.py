def genRandomAbilityScore() :
    from diceBag import dice

    dice = dice()
    dieCast = []
    stat = 0
    abilityScore = []

    while len(abilityScore) < 6 :
    # Generate Ability Scores
        for i in range(4) :
        # Roll four d6 - append to dieCast then remove the lowest roll
            roll = dice.d6()
            dieCast.append(roll)
        dieCast.remove(min(dieCast))
        stat = sum(dieCast)
        abilityScore.append(stat)
        dieCast = []

    return abilityScore





def main() :
    abilityScore = []
    print("0 = Use Preset Ability Scores")
    print("1 = Randomize my Ability Scores")

    x = int(input(""))
    if x == 1 :
        abilityScore = genRandomAbilityScore()
        print(abilityScore, " - Randomized Ability Scores")
    else :
        abilityScore = [15,14,13,12,10,8]
        print(abilityScore, " - Preset Ability Scores")

    

main()
