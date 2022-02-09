import random

def main():
    combatDeck = [
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
    itemDeck = [
        "The Avenger\n- The treasure lies in a dragon’s house, in hands once clean and now corrupted.",
        "The Paladin\n- I see a sleeping prince, a servant of light and the brother of darkness. The treasure lies with him.",
        "The Soldier\n- Go to the mountains. Climb the white tower guarded by golden knights.",
        "The Mercenary\n- The thing you seek lies with the dead, under mountains of gold coins.",
        "The Myrmidon\n- Look for a den of wolves in the hills overlooking a mountain lake. The treasure belongs to Mother Night.",
        "The Berserker\n- Find the Mad Dog’s crypt. The treasure lies within, beneath blackened bones.",
        "The Hooded One\n- I see a faceless god. He awaits you at the end of a long and winding road, deep in the mountains.",
        "The Dictator\n- I see a throne fit for a king.",
        "The Torturer\n- There is a town where all is not well. There you will find a house of corruption, and within, a dark room full of still ghosts.",
        "The Warrior\n- That which you seek lies in the womb of darkness, the devil’s lair: the one place to which he must return.",
        "The Transmuter\n- Go to a place of dizzying heights, where the stone itself is alive!",
        "The Diviner\n- Look to the one who sees all. The treasure is hidden in her camp.",
        "The Enchanter\n- I see a kneeling woman—a rose of great beauty plucked too soon. The master of the marsh knows of whom I speak.",
        "The Abjurer\n- I see a fallen house guarded by a great stone dragon. Look to the highest peak.",
        "The Elementalist\n- The treasure is hidden in a small castle beneath a mountain, guarded by amber giants.",
        "The Evoker\n- Search for the crypt of a wizard ordinaire. His staff is the key.",
        "The Illusionist\n- A man is not what he seems. He comes here in a carnival wagon. Therein lies what you seek.",
        "The Necromancer\n- A woman hangs above a roaring fire. Find her, and you will find the treasure.",
        "The Conjurer\n- I see a dead village, drowned by a river, ruled by one who has brought great evil into the world.",
        "The Wizard\n- Look for a wizard’s tower on a lake. Let the wizard’s name and servant guide you to that which you seek.",
        "The Swashbuckler\n- I see the skeleton of a deadly warrior, lying on a bed of stone flanked by gargoyles.",
        "The Philanthropist\n- Look to a place where sickness and madness are bred. Where children once cried, the treasure lies still.",
        "The Merchant\n- Seek a cask that once contained the finest wine, of which not a drop remains.",
        "The Guild Member\n- I see a dark room full of bottles. It is the tomb of a guild member..",
        "The Beggar\n- A wounded elf has what you seek. He will part with the treasure to see his dark dreams fulfilled.",
        "The Thief\n- What you seek lies at the crossroads of life and death, among the buried dead.",
        "The Tax Collector\n- The Vistani have what you seek. A missing child holds the key to the treasure’s release.",
        "The Miser\n- Look for a fortress inside a fortress, in a place hidden behind fire.",
        "The Rogue\n- I see a nest of ravens. There you will find the prize.",
        "The Monk\n- The treasure you seek is hidden behind the sun, in the house of a saint.",
        "The Missionary\n- I see a garden dusted with snow, watched over by a scarecrow with a sackcloth grin. Look not to the garden but to the guardian.",
        "The Healer\n- Look to the west. Find a pool blessed by the light of the white sun.",
        "The Shepherd\n- Find the mother—she who gave birth to evil.",
        "The Druid\n- An evil tree grows atop a hill of graves where the ancient dead sleep. The ravens can help you find it. Look for the treasure there.",
        "The Anarchist\n- I see walls of bones, a chandelier of bones, and a table of bones—all that remains of enemies long forgotten.",
        "The Charlatan\n- I see a lonely mill on a precipice. The treasure lies within.",
        "The Bishop\n- What you seek lies in a pile of treasure, beyond a set of amber doors.",
        "The Traitor\n- Look for a wealthy woman. A staunch ally of the devil, she keeps the treasure under lock and key, with the bones of an ancient enemy.",
        "The Priest\n- You will find what you seek in the castle, amid the ruins of a place of supplication."
    ]
    enemyDeck = [
        "The Artifact\n- Look for an entertaining man with a monkey. This man is more than he seems.",
        "The Beast\n- A werewolf holds a secret hatred for your enemy. Use her hatred to your advantage.",
        "The Broken One\n- I see a man of faith whose sanity hangs by a thread. He has lost someone close to him.",
        "The Darklord\n- Ah, the worst of all truths: You must face the evil of this land alone!",
        "The Donjon\n- A. Search for a troubled young man surrounded by wealth and madness. His home is his prison.\n- B. Find a girl driven to insanity, locked in the heart of her dead father’s house. Curing her madness is key to your success.",
        "The Executioner\n- Seek out the brother of the devil’s bride. They call him “the lesser,” but he has a powerful soul.",
        "The Ghost\n- A. I see a fallen paladin of a fallen order of knights. He lingers like a ghost in a dead dragon’s lair.\n- B. Stir the spirit of the clumsy knight whose crypt lies deep within the castle.",
        "The Horseman\n- A. I see a dead man of noble birth, guarded by his widow. Return life to the dead man’s corpse, and he will be your staunch ally.\n- B. A man of death named Arrigal will forsake his dark lord to serve your cause. Beware! He has a rotten soul.",
        "The Innocent\n- A. I see a young man with a kind heart. A mother’s boy! He is strong in body but weak of mind. Seek him out in the village of Barovia.\n- B. Evil’s bride is the one you seek!",
        "The Marionette\n- What horror is this? I see a man made by a man. Ageless and alone, it haunts the towers of the castle.\n- B. Look for a man of music, a man with two heads. He lives in a place of great hunger and sorrow.",
        "The Mists\n- A Vistana wanders this land alone, searching for her mentor. She does not stay in one place for long. Seek her out at Saint Markovia’s abbey, near the mists.",
        "The Raven\n- Find the leader of the feathered ones who live among the vines. Though old, he has one more fight left in him.",
        "The Seer\n- Look for a dusk elf living among the Vistani. He has suffered a great loss and is haunted by dark dreams. Help him, and he will help you in return.",
        "The Tempter\n- I see a child—a Vistana. You must hurry, for her fate hangs in the balance. Find her at the lake!\n- B. I hear a wedding bell, or perhaps a death knell. It calls thee to a mountainside abbey, wherein you will find a woman who is more than the sum of her parts."
    ]
    locationDeck = [
        "The Artifact\n- He lurks in the darkness where the morning light once shone—a sacred place.",
        "The Beast\n- The beast sits on his dark throne.",
        "The Broken One\n- He haunts the tomb of the man he envied above all.",
        "The Darklord\n- He lurks in the depths of darkness, in the one place to which he must return.",
        "The Donjon\n- He lurks in a hall of bones, in the dark pits of his castle.",
        "The Executioner\n- I see a dark figure on a balcony, looking down upon this tortured land with a twisted smile.",
        "The Ghost\n- Look to the father’s tomb.",
        "The Horseman\n- He lurks in the one place to which he must return—a place of death.",
        "The Innocent\n- He dwells with the one whose blood sealed his doom, a brother of light snuffed out too soon.",
        "The Marionette\n- Look to great heights. Find the beating heart of the castle. He waits nearby.",
        "The Mists\n- The cards can’t see where the evil lurks. The mists obscure all!",
        "The Raven\n- Look to the mother’s tomb.",
        "The Seer\n- He waits for you in a place of wisdom, warmth, and despair. Great secrets are there.",
        "The Tempter\n- I see a secret place—a vault of temptation hidden behind a woman of great beauty. The evil waits atop his tower of treasure."
    ]

    choice = input("Fortune or Combat? [f/c]: ")

    if choice.lower() == "f":

        randItem = random.sample(itemDeck, 3)

        for i in range(len(randItem)):
            if (i == 0):
                # Tome of Strahd
                print("-" * 20 + "\n" + " " * 4 + "TOME OF STRAHD\n" + "-" * 20)
                print(randItem[i] + "\n")
            elif (i == 1):
                # Holy Symbol of Ravenkind
                print("-" * 20 + "\n" + " " * 4 + "HOLY SYMBOL OF RAVENKIND\n" + "-" * 20)
                print(randItem[i] + "\n")
            elif (i == 2):
                # Sunsword
                print("-" * 20 + "\n" + " " * 4 + "SUNSWORD\n" + "-" * 20)
                print(randItem[i] + "\n")

        # Strahd's Enemy
        print("-" * 20 + "\n" + " " * 4 + "STRAHD'S ENEMY\n" + "-" * 20)
        print(random.choice(enemyDeck) + "\n")

        # Strahd's Location
        print("-" * 20 + "\n" + " " * 4 + "STRAHD'S LOCATION\n" + "-" * 20)
        print(random.choice(locationDeck) + "\n")
        
    elif choice.lower() == "c":
        print("-" * 20 + "\n" + " " * 4 + "COMBAT DECK\n" + "-" * 20)
        print(random.choice(combatDeck) + "\n")
    else:
        print(choice + " is not a valid choice.")

main()