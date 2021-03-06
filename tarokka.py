import random

def main():
    deck = [
        "The Abjurer\n- A magical shield of protection surrounds those proficient in spellcasting.\n> All spellcasters gain +2 to AC.",
        "The Anarchist\n- The anarchy of battle turns the worst strike into the strongest.\n> A natural attack roll of a 1 or 2 now also counts as a critical hit.",
        "The Artifact\n-Magical items glow with an even greater strength.\n> All magical weapons and armor gain an additional +1 to attack, damage, or armor class.",
        "The Beast\n- The ferosity of the beast lies in the hearts of all beings.\n> All creatures have +2 to melee attack rolls but are -2 to AC.",
        "The Berserker\n- The thin form of desperation flows through, sustaining itself on gold or blood.\n> At the beginning of the encounter, all creatures lose 3d6 gold pieces. If they do not have this gold, they instead take 1d6 damage.",
        "The Bishop\n- The blessing of the king's priest touches those worthy.\n> Three random creatures gain +1d4 radiant damage on attack rolls.",
        "The Broken One\n- Weariness fills even the stoutest forms.\n> All creatures gain -2 to melee attacks.",
        "The Charlatan\n- All hold within them the recognition that they know nothing.\n> Any time a creature casts a spell it must roll 1d20. On a 5 or below, the spell fails.",
        "The Conjurer\n- Ethereal servants fill the area, mirroring the violence around them.\n> All creatures have advantage on melee attacks.",
        "The Darklord\n- The death knight's cold touch caresses instruments of violence.\n> All melee attacks gain +1d6 necrotic damage",
        "The Dictator\n- After the battle few can remember the shout that changed the tide.\n> Any creature may take a standard action to give another creature a free melee attack.",
        "The Diviner\n- The eye of wisdom aims spells not at one's enemy but where that enemy is going to be.\n> All spellcasters gain +2 to spell attacks and the DCs of their spells increase by 2.",
        "The Donjon\n- Fear not death, fear the cage.\n> A random creature must make a DC 13 intelligence saving throw. On a failure, they are removed from play. They may repeat this saving throw at the end of each of their turns. On a successful save, they return to their original position.",
        "The Druid\n- Barbed vines reach from the earth, seeking the living and the blood within.\n> Any creature that moves on its turn takes 1d4 points of damage.",
        "The Elementalist\n- Spells of elemental power blaze with chaotic might.\n> Any spell that inflicts damage does an additional 1d6 damage and gains an additional damage type.\nRoll 1d4:\n1. fire\n2. cold.\n3. lightning\n4. bludgeoning.",
        "The Enchanter\n- The gleam of a blue rune infuses iron with the weave.\n> Any metal armor gains an additional +2 AC.",
        "The Evoker\n- Flames burn ever brighter for those able to wield it.\n> Any fire damage does an additional 1d6 fire damage.",
        "The Executioner\n- The blade of the executioner's axe remains ever sharp.\n> Creatures may critically hit on an 18, 19, or 20.",
        "The Ghost\n- The tormented souls of the dead take pleasure in the failures of the living.\n> Any creature that misses an attack takes 1d6 psychic damage.",
        "The Guild Member\n- A payment to the guild returns dividends on the battlefield.\n> Creatures may sacrifice ten gold pieces for +4 damage on attacks or five gold pieces for a +2 bonus to attack.",
        "The Healer\n- The touch of light burns brighter in the darkest shadows.\n> All healing spells gain +1d6 extra healing.",
        "The Hooded One\n- The blade strikes deepest in those who cannot see it coming.\n> At the beginning of combat, one random creature must make a DC 13 charisma check or become blinded. They may make a new saving throw at the end of each of their turns. On a successful saving throw they are no longer blinded.",
        "The Horseman\n- The spectral mount drives hard for those able to ride it.\n> Any creature that moves up to fifteen feet closer to an enemy before attacking gains +1d6 damage on melee attacks.",
        "The Illusionist\n- Who can say which blade is real and which is but a figment of the imagination?\n> Intelligent creatures that can see take 1d6-3 psychic damage at the beginning of each of their turns.",
        "The Innocent\n- The bulwark is strongest for those who seek not the blood of their foes.\n> Creatures that do not harm other creatures on their turn gain +5 AC until the beginning of their next turn.",
        "The Marionette\n- The strings of destiny move all exactly where they are meant to be.\n> At the beginning of each round, a random creature takes a full turn under the control of either a random player (if a monster) or the DM (if a PC). This does not count as their normal turn.",
        "The Mercenary\n- Those who take money for blood find themselves either rich or dead.\n> When a creature reduces another creature to zero hit points it gains 3d6 gold pieces.",
        "The Merchant\n- The gleam of the merchant's eyes speak to rewards given at a cost.\n> At the beginning of the encounter, a creature may sacrifice a gemstone worth at least 10 gold pieces to gain +2 to attack, +2 to AC, or +1d6 damage.",
        "The Miser\n- The fear of loss eclipses the rewards of success.\n> During its first turn in combat a creature may spend an action to bury or hide 10 gold pieces. If it does so, it gains +2 to AC and saving throws for five minutes.",
        "The Missionary\n- The prayers of the commoner releases a divine light.\n> All living creatures gain 1d6 temporary hit points.",
        "The Mists\n- The mists turn all enemies into the shadows of doubt.\n> All creatures take -2 to attack creatures more than five feet away from them.",
        "The Monk\n- The strongest armor is the resolution of the heart and mind.\n> All unarmored or cloth-wearing creatures gain +2 to AC and saving throws.",
        "The Myrmidon\n- What is steel compared to the hand that wields it?\n> Any creature attacking with a two-handed weapon gains +1d6 damage.",
        "The Necromancer\n- The elements of all magics become death in the end.\n> All magical attacks gain +1d6 necrotic damage.",
        "The Paladin\n- The blade of the righteous burns bright.\n> All melee attacks gain +1d6 radiant damage.",
        "The Philanthropist\n- Selfless souls seek those of greatest potential.\n> Three random creatures gain 3d6 gold pieces and +2 to AC and saving throws for the next five minutes.",
        "The Priest\n- The light of the gods burns in the priest's eyes.\n> All spell damage gains +1d6 extra radiant damage.",
        "The Raven\n- Those who give the raven its due find reward in the deed.\n> Any creature that reduces another creature to zero hit points gains +2d6 temporary hit points.",
        "The Rogue\n- All become thieves in desperation.\n> All creatures gain +1d6 damage when attacking an enemy within 5 feet of an ally.",
        "The Seer\n- Those who see the wisdom of elders know where best to strike.\n> At the beginning of combat, all creatures must make a DC 13 Wisdom check. Those that succeed gain +2 to attack.",
        "The Shepherd\n- The most meager might succeed when guided by a caring hand.\n> Three random creatures gain advantage on skill checks.",
        "The Soldier\n- Iron and wood will never betray you.\n> Any creature using a shield gains +2 to AC.",
        "The Swashbuckler\n- The swiftest blade draws the brightest blood.\n> All creatures gain +1d6 damage when attacking with a finesse weapon.",
        "The Tax Collector\n- All must pay the tax collector in the end.\n> On their first turn, as a bonus action, a creature must sacrifice 1% of its total gold holdings or take -2 to AC, attacks, and saving throws.",
        "The Tempter\n- The tempter trades blood for blood.\n> A creature may take 1d4 damage in order to inflict 1d6 extra damage on their next attack.",
        "The Thief\n- The swiftest hand returns with the greatest rewards.\n> Once per turn, on a successful melee attack, the attacker may make a DC 13 dexterity (slight of hand) check to steal a random trinket from the enemy.",
        "The Torturer\n- Pain brings the mightiest ruler to its knees.\n> All creatures take 1d4 damage at the beginning of their turns.",
        "The Trader\n- A ghostly grinning figure holds a glowing weapon in one hand with his other palm out awaiting payment.\n> At the beginning of their first turn in combat, a creature may sacrifice an item worth no less than 10 gold pieces to gain a +2 weapon of their choice. This weapon disappears after five minutes.",
        "The Traitor\n- Treachery lies buried deep in the soul.\n> At the beginning of combat, a random creature must make a DC 13 wisdom saving throw or be dominated by a random enemy.",
        "The Transmuter\n- Who is to say what true form one might have when the winds of chaos roar.\n> A random creature must make a DC 13 constitution saving throw. On a failure, the creature turns into a trinket. The creature cannot be harmed while in this form. The creature returns to its normal form at the end of its next turn.",
        "The Warrior\n- The way of the warrior is a resolute acceptance of death.\n> All creatures gain +2 to attack and +1d6 damage when attacking with strength-based melee weapon attacks.",
        "The Wizard\n- Magic lies deep in all things, binding us to the will of the universe.\n> All spell attacks gain +2 to spell attacks, +1d6 force damage to spell damage, and DCs increase by 2."
    ]
    highDeck = [
        "The Artifact\n-Magical items glow with an even greater strength.",
        "The Beast\n- The ferosity of the beast lies in the hearts of all beings.",
        "The Broken One\n- Weariness fills even the stoutest forms.",
        "The Darklord\n- The death knight's cold touch caresses instruments of violence.",
        "The Donjon\n- Fear not death, fear the cage.",
        "The Executioner\n- The blade of the executioner's axe remains ever sharp.",
        "The Ghost\n- The tormented souls of the dead take pleasure in the failures of the living.",
        "The Horseman\n- The spectral mount drives hard for those able to ride it.",
        "The Innocent\n- The bulwark is strongest for those who seek not the blood of their foes.",
        "The Marionette\n- The strings of destiny move all exactly where they are meant to be.",
        "The Mists\n- The mists turn all enemies into the shadows of doubt.",
        "The Raven\n- Those who give the raven its due find reward in the deed.",
        "The Seer\n- Those who see the wisdom of elders know where best to strike.",
        "The Tempter\n- The tempter trades blood for blood."
    ]
    commonDeck = [
        "The Abjurer\n- A magical shield of protection surrounds those proficient in spellcasting.",
        "The Anarchist\n- The anarchy of battle turns the worst strike into the strongest.",
        "The Berserker\n- The thin form of desperation flows through, sustaining itself on gold or blood.",
        "The Bishop\n- The blessing of the king's priest touches those worthy.",
        "The Charlatan\n- All hold within them the recognition that they know nothing.",
        "The Conjurer\n- Ethereal servants fill the area, mirroring the violence around them.",
        "The Dictator\n- After the battle few can remember the shout that changed the tide.",
        "The Diviner\n- The eye of wisdom aims spells not at one's enemy but where that enemy is going to be.",
        "The Druid\n- Barbed vines reach from the earth, seeking the living and the blood within.",
        "The Elementalist\n- Spells of elemental power blaze with chaotic might.",
        "The Enchanter\n- The gleam of a blue rune infuses iron with the weave.",
        "The Evoker\n- Flames burn ever brighter for those able to wield it.",
        "The Guild Member\n- A payment to the guild returns dividends on the battlefield.",
        "The Healer\n- The touch of light burns brighter in the darkest shadows.",
        "The Hooded One\n- The blade strikes deepest in those who cannot see it coming.",
        "The Illusionist\n- Who can say which blade is real and which is but a figment of the imagination?",
        "The Mercenary\n- Those who take money for blood find themselves either rich or dead.",
        "The Merchant\n- The gleam of the merchant's eyes speak to rewards given at a cost.",
        "The Miser\n- The fear of loss eclipses the rewards of success.",
        "The Missionary\n- The prayers of the commoner releases a divine light.",
        "The Monk\n- The strongest armor is the resolution of the heart and mind.",
        "The Myrmidon\n- What is steel compared to the hand that wields it?",
        "The Necromancer\n- The elements of all magics become death in the end.",
        "The Paladin\n- The blade of the righteous burns bright.",
        "The Philanthropist\n- Selfless souls seek those of greatest potential.",
        "The Priest\n- The light of the gods burns in the priest's eyes.",
        "The Rogue\n- All become thieves in desperation.",
        "The Shepherd\n- The most meager might succeed when guided by a caring hand.",
        "The Soldier\n- Iron and wood will never betray you.",
        "The Swashbuckler\n- The swiftest blade draws the brightest blood.",
        "The Tax Collector\n- All must pay the tax collector in the end.",
        "The Thief\n- The swiftest hand returns with the greatest rewards.",
        "The Torturer\n- Pain brings the mightiest ruler to its knees.",
        "The Trader\n- A ghostly grinning figure holds a glowing weapon in one hand with his other palm out awaiting payment.",
        "The Traitor\n- Treachery lies buried deep in the soul.",
        "The Transmuter\n- Who is to say what true form one might have when the winds of chaos roar.",
        "The Warrior\n- The way of the warrior is a resolute acceptance of death.",
        "The Wizard\n- Magic lies deep in all things, binding us to the will of the universe."
    ]

    choice = input("Fortune or Combat? [f/c]: ")

    if choice.lower() == "f":
        randCommon = random.sample(commonDeck, 3)
        randHigh = random.sample(highDeck, 2)
        print("-" * 20 + "\n" + " " * 4 + "COMMON DECK\n" + "-" * 20)
        for i in randCommon:
            print(i + "\n")
        print("-" * 20 + "\n" + " " * 5 + "HIGH DECK\n" + "-" * 20)
        for i in randHigh:
            print(i + "\n")
    elif choice.lower() == "c":
        print("-" * 20 + "\n" + " " * 4 + "COMBAT DECK\n" + "-" * 20)
        print(random.choice(deck) + "\n")
    else:
        print(choice + " is not a valid choice.")

main()