#Requires bidict

from bidict import bidict

PRIMARY="Pr"
SECONDARY="Se"
ATTRIBUTES="At"
SKILLS = "Sk"

ProfessionDict = bidict({"None": 0,
"Warrior": 1,
"Ranger": 2,
"Monk": 3,
"Necromancer": 4,
"Mesmer": 5,
"Elementalist": 6,
"Assassin": 7,
"Ritualist": 8,
"Paragon": 9,
"Dervish": 10})

Base64Dict = bidict({'A': 0, 'B': 1, 'C': 2, 'D': 3,
                     'E': 4, 'F': 5, 'G': 6, 'H': 7,
                     'I': 8, 'J': 9, 'K': 10, 'L': 11,
                     'M': 12, 'N': 13, 'O': 14, 'P': 15,
                     'Q': 16, 'R': 17, 'S': 18, 'T': 19,
                     'U': 20, 'V': 21, 'W': 22, 'X': 23,
                     'Y': 24, 'Z': 25, 'a': 26, 'b': 27,
                     'c': 28, 'd': 29, 'e': 30, 'f': 31,
                     'g': 32, 'h': 33, 'i': 34, 'j': 35,
                     'k': 36, 'l': 37, 'm': 38, 'n': 39,
                     'o': 40, 'p': 41, 'q': 42, 'r': 43,
                     's': 44, 't': 45, 'u': 46, 'v': 47,
                     'w': 48, 'x': 49, 'y': 50, 'z': 51,
                     '0': 52, '1': 53, '2': 54, '3': 55,
                     '4': 56, '5': 57, '6': 58, '7': 59,
                     '8': 60, '9': 61, '+': 62, '/': 63})

AttributeDict = bidict({'Fast Casting': 0, 'Illusion Magic': 1, 'Domination Magic': 2, 'Inspiration Magic': 3, 'Blood Magic': 4, 'Death Magic': 5, 'Soul Reaping': 6, 'Curses': 7, 'Air Magic': 8, 'Earth Magic': 9, 'Fire Magic': 10, 'Water Magic': 11, 'Energy Storage': 12, 'Healing Prayers': 13, 'Smiting Prayers': 14, 'Protection Prayers': 15, 'Divine Favor': 16, 'Strength': 17, 'Axe Mastery': 18, 'Hammer Mastery': 19, 'Swordsmanship': 20, 'Tactics': 21, 'Beast Mastery': 22, 'Expertise': 23, 'Wilderness Survival': 24, 'Marksmanship': 25, 'Dagger Mastery': 29, 'Deadly Arts': 30, 'Shadow Arts': 31, 'Communing': 32, 'Restoration Magic': 33, 'Channeling Magic': 34, 'Critical Strikes': 35, 'Spawning Power': 36, 'Spear Mastery': 37, 'Command': 38, 'Motivation': 39, 'Leadership': 40, 'Scythe Mastery': 41, 'Wind Prayers': 42, 'Earth Prayers': 43, 'Mysticism': 44})

SkillDict = bidict({'No Skill': 0, 'Resurrection Signet': 2, 'Signet of Capture': 3, 'Agonizing Chop': 1403, 'Axe Rake': 334, 'Axe Twist': 342, 'Cleave': 335, 'Critical Chop': 1402, 'Cyclone Axe': 330, 'Decapitate': 1696, 'Dismember': 337, 'Disrupting Chop': 340, 'Eviscerate': 338, "Executioner's Strike": 336, 'Furious Axe': 904, 'Keen Chop': 2009, 'Lacerating Chop': 849, 'Penetrating Blow': 339, 'Penetrating Chop': 1136, 'Swift Chop': 341, 'Triple Chop': 992, 'Whirling Axe': 888, 'Auspicious Blow': 905, 'Backbreaker': 358, 'Belly Smash': 350, 'Counter Blow': 357, 'Crude Swing': 353, 'Crushing Blow': 352, 'Devastating Hammer': 355, 'Earth Shaker': 354, 'Enraged Smash': 993, 'Fierce Blow': 850, 'Forceful Blow': 889, 'Hammer Bash': 331, 'Heavy Blow': 359, 'Irresistible Blow': 356, "Magehunter's Smash": 1697, 'Mighty Blow': 351, 'Mokele Smash': 1409, 'Overbearing Smash': 1410, 'Pulverizing Smash': 2008, 'Renewing Smash': 994, 'Staggering Blow': 360, 'Yeti Smash': 1137, '"I Meant to Do That!"': 2067, '"I Will Avenge You!"': 333, '"I Will Survive!"': 368, '"You Will Die!"': 1141, 'Battle Rage': 317, 'Berserker Stance': 370, 'Body Blow': 2197, "Bull's Charge": 379, "Bull's Strike": 332, 'Burst of Aggression': 1413, 'Charging Strike': 1405, 'Counterattack': 1693, 'Defy Pain': 318, 'Disarm': 2066, 'Dolyak Signet': 361, 'Dwarven Battle Stance': 375, 'Endure Pain': 347, 'Enraging Charge': 1414, 'Flail': 1404, 'Flourish': 389, "Griffon's Sweep": 327, 'Headbutt': 1406, "Leviathan's Sweep": 1134, "Lion's Comfort": 1407, 'Magehunter Strike': 1694, 'Power Attack': 322, 'Primal Rage': 831, "Protector's Strike": 326, 'Rage of the Ntouka': 1408, 'Rush': 319, 'Shield Bash': 363, 'Signet of Stamina': 1411, 'Signet of Strength': 944, 'Sprint': 349, 'Tiger Stance': 995, "Warrior's Cunning": 362, "Warrior's Endurance": 374, 'Barbarous Slice': 1416, 'Crippling Slash': 1415, 'Dragon Slash': 907, 'Final Thrust': 385, 'Galrath Slash': 383, 'Gash': 384, 'Hamstring': 320, 'Hundred Blades': 381, 'Jaizhenju Strike': 1135, 'Knee Cutter': 2010, 'Pure Strike': 328, 'Quivering Blade': 892, 'Savage Slash': 390, 'Seeking Blade': 386, 'Sever Artery': 382, 'Silverwing Slash': 1144, 'Standing Slash': 996, 'Steelfang Slash': 1702, 'Sun and Moon Slash': 851, '"Charge!"': 364, '"Fear Me!"': 366, '"None Shall Pass!"': 891, '"Retreat!"': 839, '"Shields Up!"': 367, '"To the Limit!"': 316, '"Victory Is Mine!"': 365, '"Watch Yourself!"': 348, 'Auspicious Parry': 1142, 'Balanced Stance': 371, "Bonetti's Defense": 380, 'Deadly Riposte': 388, 'Defensive Stance': 345, 'Deflect Arrows': 373, 'Desperation Blow': 323, 'Disciplined Stance': 376, 'Drunken Blow': 1133, "Gladiator's Defense": 372, 'Healing Signet': 1, "Protector's Defense": 810, 'Riposte': 387, 'Shield Stance': 378, 'Shove': 1146, "Soldier's Defense": 1699, "Soldier's Speed": 2196, "Soldier's Stance": 1698, "Soldier's Strike": 1695, 'Steady Stance': 1701, 'Thrill of Victory': 324, 'Wary Stance': 377, '"Coward!"': 869, '"For Great Justice!"': 343, '"Let\'s Get \'Em!"': 1014, '"On Your Knees!"': 906, '"You\'re All Alone!"': 1412, 'Distracting Blow': 325, 'Distracting Strike': 2194, 'Flurry': 344, 'Frenzied Defense': 1700, 'Frenzy': 346, 'Grapple': 2011, 'Skull Crack': 329, 'Storm of Swords': 1140, 'Symbolic Strike': 2195, 'Wild Blow': 321, 'Bestial Fury': 1209, 'Bestial Mauling': 1203, 'Bestial Pounce': 437, 'Brutal Strike': 444, 'Call of Haste': 415, 'Call of Protection': 412, 'Charm Animal': 411, 'Comfort Animal': 436, 'Companionship': 2141, 'Disrupting Lunge': 445, 'Edge of Extinction': 464, 'Energizing Wind': 474, 'Enraged Lunge': 1202, 'Feral Aggression': 2142, 'Feral Lunge': 439, 'Ferocious Strike': 442, 'Fertile Season': 467, 'Heal as One': 1195, "Heket's Rampage": 1728, 'Lacerate': 961, 'Maiming Strike': 438, "Melandru's Assault": 441, "Otyugh's Cry": 447, 'Poisonous Bite': 1205, 'Pounce': 1206, "Predator's Pounce": 443, 'Predatory Bond': 1194, 'Predatory Season': 470, 'Primal Echoes': 469, 'Rampage as One': 1721, 'Revive Animal': 422, 'Run as One': 811, 'Savage Pounce': 1201, 'Scavenger Strike': 440, 'Strike as One': 1468, 'Symbiosis': 468, 'Symbiotic Bond': 423, "Tiger's Fury": 454, 'Toxicity': 1472, "Viper's Nest": 1211, "Archer's Signet": 1200, 'Distracting Shot': 399, 'Dodge': 425, 'Escape': 448, 'Expert Focus': 2145, "Expert's Dexterity": 1724, 'Glass Arrows': 1199, 'Infuriating Heat': 1730, 'Lightning Reflexes': 453, "Marksman's Wager": 430, 'Oath Shot': 405, 'Point Blank Shot': 407, 'Practiced Stance': 449, 'Throw Dirt': 424, "Trapper's Focus": 946, "Trapper's Speed": 1475, 'Whirling Defense': 450, "Zojun's Haste": 1196, "Zojun's Shot": 1192, 'Arcing Shot': 1467, 'Barrage': 395, 'Body Shot': 2198, 'Broad Head Arrow': 1198, 'Burning Arrow': 1466, 'Concussion Shot': 408, 'Crippling Shot': 393, 'Crossfire': 1469, 'Debilitating Shot': 406, 'Determined Shot': 402, 'Disrupting Accuracy': 1723, 'Disrupting Shot': 2143, 'Favorable Winds': 472, 'Focused Shot': 909, "Hunter's Shot": 391, 'Keen Arrow': 1720, "Marauder's Shot": 908, "Melandru's Shot": 853, 'Needling Shot': 1197, 'Penetrating Attack': 398, 'Pin Down': 392, 'Power Shot': 394, 'Precision Shot': 400, 'Prepared Shot': 1465, 'Punishing Shot': 409, 'Rapid Fire': 2068, 'Read the Wind': 432, 'Savage Shot': 426, 'Screaming Shot': 1719, 'Seeking Arrows': 893, "Sloth Hunter's Shot": 2069, 'Splinter Shot': 852, 'Sundering Attack': 1191, 'Volley': 2144, 'Apply Poison': 435, 'Barbed Arrows': 1470, 'Barbed Trap': 458, 'Brambles': 947, 'Choking Gas': 434, 'Conflagration': 466, "Dryder's Defenses": 452, 'Dust Trap': 457, 'Equinox': 1212, 'Famine': 997, 'Flame Trap': 459, 'Frozen Soil': 471, 'Greater Conflagration': 465, 'Healing Spring': 460, 'Ignite Arrows': 431, 'Incendiary Arrows': 428, 'Kindle Arrows': 433, "Melandru's Arrows": 429, "Melandru's Resilience": 451, 'Muddy Terrain': 477, 'Natural Stride': 1727, "Nature's Renewal": 476, 'Pestilence': 870, 'Piercing Trap': 2140, 'Poison Arrow': 404, 'Poison Tip Signet': 2199, 'Quickening Zephyr': 475, 'Quicksand': 1473, 'Roaring Winds': 1725, "Scavenger's Focus": 1471, "Serpent's Quickness": 456, 'Smoke Trap': 1729, 'Snare': 854, 'Spike Trap': 461, 'Storm Chaser': 455, 'Tranquility': 1213, 'Tripwire': 1476, 'Troll Unguent': 446, 'Winnowing': 463, 'Winter': 462, 'Antidote Signet': 427, 'Called Shot': 403, 'Dual Shot': 396, 'Forked Arrow': 1722, 'Magebane Shot': 1726, 'Quick Shot': 397, "Storm's Embrace": 1474, 'Blessed Aura': 256, 'Blessed Light': 941, 'Blessed Signet': 297, 'Boon Signet': 847, 'Contemplation of Purity': 300, 'Deny Hexes': 991, 'Divine Boon': 284, 'Divine Healing': 279, 'Divine Intervention': 246, 'Divine Spirit': 310, "Healer's Boon": 1393, "Heaven's Delight": 1117, 'Holy Haste': 1685, 'Peace and Harmony': 266, 'Release Enchantments': 960, "Scribe's Insight": 1684, 'Signet of Devotion': 293, "Smiter's Boon": 2005, 'Spell Breaker': 273, 'Spell Shield': 957, 'Unyielding Aura': 268, 'Watchful Healing': 1392, 'Watchful Spirit': 255, 'Withdraw Hexes': 942, 'Cure Hex': 2003, "Dwayna's Kiss": 283, "Dwayna's Sorrow": 838, 'Ethereal Light': 959, 'Gift of Health': 1121, 'Glimmer of Light': 1686, 'Heal Area': 280, 'Heal Other': 286, 'Heal Party': 287, "Healer's Covenant": 1394, 'Healing Breeze': 288, 'Healing Burst': 1118, 'Healing Hands': 285, 'Healing Light': 867, 'Healing Ribbon': 2062, 'Healing Ring': 1262, 'Healing Seed': 274, 'Healing Touch': 313, 'Healing Whisper': 958, 'Infuse Health': 292, "Jamei's Gaze": 1120, "Karei's Healing Circle": 1119, 'Light of Deliverance': 1397, 'Live Vicariously': 291, 'Mending': 290, 'Orison of Healing': 281, 'Patient Spirit': 2061, 'Renew Life': 1263, 'Restful Breeze': 886, 'Restore Life': 314, 'Resurrection Chant': 1128, 'Signet of Rejuvenation': 887, 'Spotless Mind': 2064, 'Spotless Soul': 2065, 'Supportive Spirit': 1391, 'Vigorous Spirit': 254, 'Word of Healing': 282, 'Words of Comfort': 1396, 'Aegis': 257, 'Air of Enchantment': 1115, 'Amity': 265, 'Aura of Faith': 260, 'Aura of Stability': 2063, 'Convert Hexes': 303, 'Dismiss Condition': 1691, 'Divert Hexes': 1692, 'Draw Conditions': 311, 'Extinguish': 943, 'Guardian': 258, 'Life Attunement': 244, 'Life Barrier': 270, 'Life Bond': 241, 'Life Sheath': 1123, 'Mark of Protection': 269, 'Mend Ailment': 277, 'Mend Condition': 275, 'Mending Touch': 1401, 'Pacifism': 264, 'Pensive Guardian': 1683, 'Protective Bond': 263, 'Protective Spirit': 245, 'Purifying Veil': 2007, 'Rebirth': 306, 'Restore Condition': 276, 'Reversal of Fortune': 307, 'Reverse Hex': 848, 'Shield Guardian': 885, 'Shield of Absorption': 1399, 'Shield of Deflection': 259, 'Shield of Regeneration': 261, 'Shielding Hands': 299, 'Spirit Bond': 1114, 'Vital Blessing': 289, 'Zealous Benediction': 1687, "Balthazar's Aura": 272, "Balthazar's Pendulum": 1395, "Balthazar's Spirit": 242, 'Bane Signet': 296, 'Banish': 252, 'Castigation Signet': 2006, "Defender's Zeal": 1688, 'Holy Strike': 312, 'Holy Wrath': 249, "Judge's Insight": 267, "Judge's Intervention": 1390, "Kirin's Wrath": 1113, 'Ray of Judgment': 830, 'Retribution': 248, 'Reversal of Damage': 1400, 'Scourge Enchantment': 1398, 'Scourge Healing': 251, 'Scourge Sacrifice': 253, 'Shield of Judgment': 262, 'Signet of Judgment': 294, 'Signet of Mystic Wrath': 1689, 'Signet of Rage': 1269, 'Smite': 240, 'Smite Condition': 2004, 'Smite Hex': 302, 'Spear of Light': 1130, 'Stonesoul Strike': 1131, 'Strength of Honor': 243, 'Symbol of Wrath': 247, 'Word of Censure': 1129, "Zealot's Fire": 271, "Castigation Signet (Saul D'Alessio)": 2683, 'Empathic Removal': 1126, 'Essence Bond': 250, 'Holy Veil': 309, 'Light of Dwayna': 304, 'Martyr': 298, 'Purge Conditions': 278, 'Purge Signet': 295, 'Remove Hex': 301, 'Resurrect': 305, 'Signet of Removal': 1690, 'Succor': 308, 'Vengeance': 315, 'Awaken the Blood': 111, 'Barbed Signet': 131, 'Blood Bond': 835, 'Blood Drinker': 1076, 'Blood is Power': 119, 'Blood of the Aggressor': 902, 'Blood Renewal': 115, 'Blood Ritual': 157, "Cultist's Fervor": 806, 'Dark Bond': 138, 'Dark Fury': 147, 'Dark Pact': 133, 'Demonic Flesh': 130, 'Jaundiced Gaze': 763, 'Life Siphon': 109, 'Life Transfer': 126, 'Lifebane Strike': 1067, 'Mark of Fury': 1360, 'Mark of Subversion': 127, 'Offering of Blood': 146, 'Oppressive Gaze': 864, 'Order of Pain': 134, 'Order of the Vampire': 148, 'Ravenous Gaze': 862, 'Shadow Strike': 102, 'Signet of Agony': 145, 'Signet of Suffering': 1364, 'Soul Leech': 128, 'Spoil Victor': 1066, 'Strip Enchantment': 143, 'Touch of Agony': 158, 'Unholy Feast': 110, 'Vampiric Bite': 1077, 'Vampiric Gaze': 153, 'Vampiric Spirit': 819, 'Vampiric Swarm': 1075, 'Vampiric Touch': 156, "Wallow's Bite": 1078, 'Well of Blood': 92, 'Well of Power': 91, 'Atrophy': 2237, 'Barbs': 101, 'Cacophony': 1998, 'Chilblains': 144, 'Corrupt Enchantment': 1362, 'Defile Defenses': 2188, 'Defile Enchantments': 1070, 'Defile Flesh': 129, 'Depravity': 820, 'Desecrate Enchantments': 112, 'Enfeeble': 117, 'Enfeebling Blood': 118, 'Enfeebling Touch': 1079, 'Envenom Enchantments': 936, 'Faintheartedness': 135, 'Feast of Corruption': 151, 'Insidious Parasite': 123, 'Lingering Curse': 142, 'Malaise': 140, 'Mark of Pain': 150, 'Meekness': 1260, 'Order of Apostasy': 863, 'Pain of Disenchantment': 1359, 'Parasitic Bond': 99, 'Plague Sending': 149, 'Plague Signet': 132, 'Plague Touch': 154, 'Poisoned Heart': 840, 'Price of Failure': 103, 'Reckless Haste': 834, 'Rend Enchantments': 141, 'Rigor Mortis': 137, 'Rip Enchantment': 955, 'Shadow of Fear': 136, 'Shivers of Dread': 1071, 'Soul Barbs': 100, 'Soul Bind': 901, 'Spinal Shivers': 124, 'Spiteful Spirit': 121, 'Suffering': 108, 'Ulcerous Lungs': 1358, 'Vocal Minority': 883, 'Weaken Armor': 159, 'Weaken Knees': 822, 'Well of Darkness': 1366, 'Well of Ruin': 2236, 'Well of Silence': 1660, 'Well of Weariness': 818, 'Wither': 125, 'Animate Bone Fiend': 84, 'Animate Bone Horror': 83, 'Animate Bone Minions': 85, 'Animate Flesh Golem': 832, 'Animate Shambling Horror': 1351, 'Animate Vampiric Horror': 805, 'Aura of the Lich': 114, 'Bitter Chill': 1068, 'Blood of the Master': 120, 'Consume Corpse': 98, 'Contagion': 1356, 'Dark Aura': 116, 'Death Nova': 104, 'Deathly Chill': 89, 'Deathly Swarm': 105, 'Discord': 817, 'Feast for the Dead': 1354, 'Fetid Ground': 841, 'Infuse Condition': 139, 'Jagged Bones': 1355, 'Malign Intervention': 122, 'Necrotic Traversal': 97, 'Order of Undeath': 1352, 'Putrid Bile': 2058, 'Putrid Explosion': 95, 'Putrid Flesh': 1353, 'Rising Bile': 935, 'Rotting Flesh': 106, 'Soul Feast': 96, 'Tainted Flesh': 113, 'Taste of Death': 152, 'Taste of Pain': 1069, 'Toxic Chill': 1659, "Verata's Aura": 88, "Verata's Gaze": 87, "Verata's Sacrifice": 90, 'Vile Miasma': 828, 'Vile Touch': 155, 'Virulence': 107, 'Well of Suffering': 93, 'Well of the Profane': 94, 'Withering Aura': 1997, "Angorodon's Gaze": 2189, 'Foul Feast': 2057, "Hexer's Vigor": 2138, 'Icy Veins': 821, 'Masochism': 2139, "Reaper's Mark": 808, 'Signet of Lost Souls': 1365, 'Signet of Sorrow': 1363, 'Wail of Doom': 764, 'Gaze of Contempt': 766, "Grenth's Balance": 86, 'Aneurysm': 2055, 'Arcane Larceny': 1062, 'Arcane Thievery': 81, 'Backfire': 28, 'Blackout': 29, 'Chaos Storm': 77, 'Complicate': 932, 'Cry of Frustration': 57, 'Diversion': 30, 'Empathy': 26, "Enchanter's Conundrum": 1345, 'Energy Burn': 42, 'Energy Surge': 39, 'Guilt': 46, 'Hex Breaker': 10, 'Hex Eater Vortex': 1348, 'Ignorance': 35, 'Mind Wrack': 49, 'Mistrust': 979, 'Overload': 898, 'Panic': 52, 'Power Block': 5, 'Power Flux': 953, 'Power Leak': 24, 'Power Lock': 1994, 'Power Spike': 23, 'Price of Pride': 1655, 'Psychic Distraction': 1053, 'Shame': 51, 'Shatter Delusions': 27, 'Shatter Enchantment': 69, 'Shatter Hex': 67, 'Signet of Disruption': 860, 'Signet of Distraction': 1992, 'Signet of Weariness': 59, 'Simple Thievery': 1350, 'Spiritual Pain': 1336, 'Unnatural Signet': 934, 'Visions of Regret': 878, "Wastrel's Demise": 1335, "Wastrel's Worry": 50, "Unnatural Signet (Saul D'Alessio)": 2684, 'Arcane Languor': 804, 'Keystone Signet': 63, 'Mantra of Recovery': 13, 'Persistence of Memory': 1338, 'Power Return': 931, 'Psychic Instability': 1057, 'Stolen Speed': 880, 'Symbolic Celerity': 1340, 'Symbolic Posture': 1658, 'Symbols of Inspiration': 1339, 'Accumulated Pain': 1052, 'Air of Disenchantment': 1656, "Ancestor's Visage": 1054, 'Arcane Conundrum': 36, 'Calculated Risk': 2053, 'Clumsiness': 43, 'Confusing Images': 2137, 'Conjure Nightmare': 859, 'Conjure Phantasm': 31, 'Crippling Anguish': 54, 'Distortion': 11, 'Ethereal Burden': 45, 'Fevered Dreams': 55, 'Fragility': 19, 'Frustration': 1341, 'Illusion of Haste': 37, 'Illusion of Pain': 879, 'Illusion of Weakness': 32, 'Illusionary Weaponry': 33, 'Images of Remorse': 899, 'Imagined Burden': 76, 'Ineptitude': 47, "Kitah's Burden": 1056, 'Migraine': 53, 'Phantom Pain': 44, 'Recurring Insecurity': 1055, 'Shared Burden': 900, 'Shrinking Armor': 2054, 'Signet of Clumsiness': 1657, 'Signet of Illusions': 1346, 'Soothing Images': 56, 'Sum of All Fears': 1996, 'Sympathetic Visage': 34, 'Wandering Eye': 2056, 'Auspicious Incantation': 930, 'Channeling': 38, 'Discharge Enchantment': 1347, 'Drain Delusions': 1337, 'Drain Enchantment': 68, 'Elemental Resistance': 72, 'Energy Drain': 79, 'Energy Tap': 80, 'Ether Feast': 40, 'Ether Lord': 41, 'Ether Phantom': 1343, 'Ether Signet': 881, 'Extend Conditions': 1333, 'Feedback': 1061, 'Hex Eater Signet': 1059, 'Inspired Enchantment': 21, 'Inspired Hex': 22, 'Leech Signet': 61, "Lyssa's Aura": 813, 'Mantra of Concentration': 16, 'Mantra of Earth': 6, 'Mantra of Flame': 7, 'Mantra of Frost': 8, 'Mantra of Inscriptions': 15, 'Mantra of Lightning': 9, 'Mantra of Persistence': 14, 'Mantra of Recall': 82, 'Mantra of Resolve': 17, 'Mantra of Signets': 18, 'Physical Resistance': 73, 'Power Drain': 25, 'Power Leech': 803, 'Revealed Enchantment': 1048, 'Revealed Hex': 1049, 'Signet of Humility': 62, 'Signet of Recall': 1993, 'Spirit of Failure': 48, 'Spirit Shackles': 66, 'Tease': 1342, 'Waste Not, Want Not': 1995, 'Arcane Echo': 75, 'Arcane Mimicry': 65, 'Echo': 74, 'Epidemic': 78, 'Expel Hexes': 954, 'Hypochondria': 1334, "Lyssa's Balance": 877, 'Mirror of Disenchantment': 1349, 'Shatter Storm': 933, 'Signet of Disenchantment': 882, 'Signet of Midnight': 58, 'Web of Disruption': 1344, 'Air Attunement': 225, 'Arc Lightning': 842, 'Blinding Flash': 220, 'Blinding Surge': 1367, 'Chain Lightning': 223, 'Chilling Winds': 1368, 'Conjure Lightning': 221, 'Enervating Charge': 224, 'Gale': 162, 'Glimmering Mark': 227, 'Glyph of Swiftness': 2002, 'Gust': 843, 'Invoke Lightning': 1664, 'Lightning Bolt': 1369, 'Lightning Hammer': 865, 'Lightning Javelin': 230, 'Lightning Orb': 229, 'Lightning Strike': 222, 'Lightning Surge': 205, 'Lightning Touch': 232, 'Mind Shock': 226, 'Ride the Lightning': 836, 'Shell Shock': 2059, 'Shock': 231, 'Shock Arrow': 1082, "Storm Djinn's Haste": 1370, "Teinai's Wind": 1081, 'Thunderclap': 228, 'Whirlwind': 163, 'Windborne Speed': 160, 'Aftershock': 174, 'Armor of Earth': 165, 'Ash Blast': 1085, 'Churning Earth': 844, 'Crystal Wave': 217, "Dragon's Stomp": 1086, 'Earth Attunement': 169, 'Earthen Shackles': 2000, 'Earthquake': 170, 'Ebon Hawk': 1374, 'Eruption': 167, 'Glowstone': 1661, 'Grasping Earth': 173, 'Iron Mist': 216, 'Kinetic Armor': 166, 'Magnetic Aura': 168, 'Magnetic Surge': 2190, 'Obsidian Flame': 219, 'Obsidian Flesh': 218, 'Sandstorm': 1372, 'Shockwave': 937, 'Sliver Armor': 1084, 'Stone Daggers': 172, 'Stone Sheath': 1373, 'Stone Striker': 1371, 'Stoneflesh Aura': 1375, 'Stoning': 171, "Teinai's Crystals": 1099, 'Unsteady Ground': 1083, 'Ward Against Elements': 175, 'Ward Against Foes': 177, 'Ward Against Melee': 176, 'Ward of Stability': 938, 'Ward of Weakness': 2001, 'Aura of Restoration': 180, 'Elemental Attunement': 164, 'Energy Blast': 2193, 'Energy Boon': 837, 'Ether Prism': 1377, 'Ether Prodigy': 178, 'Ether Renewal': 181, 'Glyph of Energy': 199, 'Glyph of Lesser Energy': 200, 'Glyph of Restoration': 1376, 'Master of Magic': 1378, 'Bed of Coals': 825, 'Breath of Fire': 1094, 'Burning Speed': 823, 'Conjure Flame': 182, 'Double Dragon': 1091, 'Elemental Flame': 1663, 'Fire Attunement': 184, 'Fire Storm': 197, 'Fireball': 186, 'Flame Burst': 188, "Flame Djinn's Haste": 1381, 'Flare': 194, 'Glowing Gaze': 1379, 'Glyph of Immolation': 2060, 'Immolate': 191, 'Incendiary Bonds': 179, 'Inferno': 183, 'Lava Arrows': 824, 'Lava Font': 195, 'Liquid Flame': 845, 'Mark of Rodgort': 190, 'Meteor': 187, 'Meteor Shower': 192, 'Mind Blast': 1662, 'Mind Burn': 185, 'Phoenix': 193, "Rodgort's Invocation": 189, 'Savannah Heat': 1380, 'Searing Flames': 884, 'Searing Heat': 196, 'Smoldering Embers': 1090, 'Star Burst': 1095, "Teinai's Heat": 1093, 'Armor of Frost': 206, 'Armor of Mist': 238, 'Blurred Vision': 235, 'Conjure Frost': 207, 'Deep Freeze': 234, 'Freezing Gust': 1382, 'Frigid Armor': 1261, 'Frozen Burst': 212, 'Glowing Ice': 2192, 'Ice Prison': 210, 'Ice Spear': 214, 'Ice Spikes': 211, 'Icy Prism': 903, 'Icy Shackles': 939, 'Maelstrom': 215, 'Mind Freeze': 209, 'Mirror of Ice': 1098, 'Mist Form': 236, 'Rust': 204, 'Shard Storm': 213, 'Shatterstone': 809, 'Slippery Ground': 2191, 'Steam': 846, 'Swirling Aura': 233, "Teinai's Prison": 1097, 'Vapor Blade': 866, 'Ward Against Harm': 239, 'Water Attunement': 208, 'Water Trident': 237, "Winter's Embrace": 1999, 'Glyph of Concentration': 201, 'Glyph of Elemental Power': 198, 'Glyph of Essence': 1096, 'Glyph of Renewal': 203, 'Glyph of Sacrifice': 202, 'Second Wind': 1088, "Assassin's Remedy": 1639, 'Black Lotus Strike': 779, 'Critical Defenses': 1027, 'Critical Eye': 1018, 'Critical Strike': 1019, 'Dark Apostasy': 1029, 'Deadly Haste': 1638, "Locust's Fury": 1030, 'Malicious Strike': 1633, 'Palm Strike': 1045, 'Seeping Wound': 1034, 'Sharpen Daggers': 926, 'Shattering Assault': 1634, 'Twisting Fangs': 776, 'Unsuspecting Strike': 783, 'Way of the Assassin': 1649, 'Way of the Master': 2187, 'Black Mantis Thrust': 1024, 'Black Spider Strike': 1636, 'Blades of Steel': 1020, 'Death Blossom': 775, 'Desperate Strike': 948, 'Disrupting Stab': 1025, 'Exhausting Assault': 975, 'Falling Lotus Strike': 1990, 'Falling Spider': 778, 'Flashing Blades': 1042, 'Fox Fangs': 780, "Fox's Promise": 1640, 'Golden Fang Strike': 1988, 'Golden Fox Strike': 1637, 'Golden Lotus Strike': 1026, 'Golden Phoenix Strike': 989, 'Golden Skull Strike': 1635, 'Horns of the Ox': 777, 'Jagged Strike': 782, 'Jungle Strike': 1021, 'Leaping Mantis Sting': 1023, 'Lotus Strike': 1987, 'Moebius Strike': 781, 'Nine Tail Strike': 986, 'Repeating Strike': 976, 'Temple Strike': 988, 'Trampling Ox': 2135, 'Wild Strike': 1022, "Assassin's Promise": 1035, 'Augury of Death': 1646, 'Crippling Dagger': 1038, 'Dancing Daggers': 858, 'Dark Prison': 1044, 'Deadly Paradox': 572, 'Disrupting Dagger': 571, 'Enduring Toxin': 800, 'Entangling Asp': 784, 'Expose Defenses': 802, 'Expunge Enchantments': 990, 'Impale': 1033, 'Iron Palm': 786, 'Mantis Touch': 974, 'Mark of Death': 785, 'Mark of Insecurity': 570, "Sadist's Signet": 1991, 'Scorpion Wire': 815, 'Shadow Fang': 2052, 'Shadow Prison': 1652, 'Shameful Fear': 927, 'Shroud of Silence': 801, 'Signet of Deadly Corruption': 2186, 'Signet of Shadows': 876, 'Signet of Toxic Shock': 1647, 'Siphon Speed': 951, 'Siphon Strength': 827, 'Vampiric Assault': 1986, 'Way of the Empty Palm': 987, 'Beguiling Haze': 799, 'Blinding Powder': 973, 'Caltrops': 985, 'Dark Escape': 1037, "Death's Charge": 952, "Death's Retreat": 1651, 'Feigned Neutrality': 1641, 'Heart of Shadow': 1032, 'Hidden Caltrops': 1642, 'Mirrored Stance': 816, 'Return': 770, 'Shadow Form': 826, 'Shadow of Haste': 929, 'Shadow Refuge': 814, 'Shadow Shroud': 928, 'Shadowy Burden': 950, 'Shroud of Distress': 1031, 'Smoke Powder Defense': 2136, 'Unseen Fury': 1041, "Viper's Defense": 769, 'Way of Perfection': 1028, 'Way of the Fox': 949, 'Way of the Lotus': 977, 'Assault Enchantments': 1643, 'Aura of Displacement': 771, 'Dash': 1043, 'Lift Enchantment': 1645, 'Mark of Instability': 978, 'Recall': 925, 'Shadow Meld': 1654, 'Shadow Walk': 1650, 'Signet of Malice': 1036, 'Signet of Twilight': 1648, 'Spirit Walk': 1040, 'Swap': 1653, "Wastrel's Collapse": 1644, 'Agony': 2205, "Ancestors' Rage": 1246, 'Bloodsong': 1253, "Caretaker's Charge": 1744, 'Channeled Strike': 1225, 'Clamor of Souls': 1215, 'Cruel Was Daoshen': 1218, 'Destruction': 920, 'Destructive Was Glaive': 1732, 'Essence Strike': 1227, 'Gaze from Beyond': 1245, 'Gaze of Fury': 1734, 'Grasping Was Kuurong': 789, 'Lamentation': 916, 'Nightmare Weapon': 795, 'Offering of Spirit': 1479, 'Painful Bond': 1237, 'Renewing Surge': 1478, 'Signet of Spirits': 1239, 'Spirit Boon Strike': 1226, 'Spirit Burn': 919, 'Spirit Rift': 910, 'Spirit Siphon': 1228, 'Splinter Weapon': 792, 'Wailing Weapon': 794, "Warmonger's Weapon": 1751, 'Weapon of Aggression': 2073, 'Weapon of Fury': 1749, "Wielder's Strike": 1733, 'Destructive Was Glaive (PvP)': 3157, 'Anguish': 1745, 'Armor of Unfeeling': 1232, 'Binding Chains': 1236, 'Brutal Weapon': 1258, 'Disenchantment': 923, 'Displacement': 1249, 'Dissonance': 921, 'Dulled Weapon': 1235, 'Earthbind': 1252, 'Ghostly Weapon': 2206, 'Guided Weapon': 1259, 'Mighty Was Vorizun': 773, 'Pain': 1247, 'Restoration': 963, 'Shadowsong': 871, 'Shelter': 982, 'Signet of Ghostly Might': 1742, 'Soothing': 1266, 'Sundering Weapon': 2148, 'Union': 911, 'Vital Weapon': 1267, 'Wanderlust': 1255, 'Weapon of Quickening': 1268, 'Blind Was Mingson': 788, 'Death Pact Signet': 1481, 'Defiant Was Xinrae': 812, 'Flesh of My Flesh': 791, 'Generous Was Tsungrai': 772, 'Ghostmirror Light': 1741, 'Life': 1251, 'Lively Was Naomei': 1222, 'Mend Body and Soul': 1234, 'Mending Grip': 2202, 'Preservation': 1250, 'Protective Was Kaolai': 1219, 'Pure Was Li Ming': 2072, 'Recovery': 1748, 'Recuperation': 981, 'Rejuvenation': 2204, 'Resilient Was Xiko': 1221, 'Resilient Weapon': 787, 'Soothing Memories': 1233, 'Spirit Light': 915, 'Spirit Light Weapon': 1257, 'Spirit Transfer': 962, 'Spiritleech Aura': 2203, 'Tranquil Was Tanasen': 913, 'Vengeful Was Khanhei': 790, 'Vengeful Weapon': 964, 'Vocal Was Sogolon': 1731, 'Weapon of Remedy': 1752, 'Weapon of Shadow': 983, 'Weapon of Warding': 793, "Wielder's Boon": 1265, "Xinrae's Weapon": 1750, 'Anguished Was Lingwah': 1223, 'Attuned Was Songkai': 1220, 'Boon of Creation': 1230, 'Consume Soul': 914, 'Doom': 1264, 'Empowerment': 1747, 'Energetic Was Lee Sa': 2016, 'Explosive Growth': 1229, 'Feast of Souls': 980, 'Ghostly Haste': 1244, 'Reclaim Essence': 1482, 'Renewing Memories': 1739, 'Ritual Lord': 1217, 'Rupture Soul': 917, 'Sight Beyond Sight': 1738, 'Signet of Binding': 1743, 'Signet of Creation': 1238, 'Soul Twisting': 1240, 'Spirit Channeling': 1231, 'Spirit to Flesh': 918, "Spirit's Gift": 1480, "Spirit's Strength": 1736, 'Weapon of Renewal': 2149, "Wielder's Remedy": 1740, "Wielder's Zeal": 1737, 'Draw Spirit': 1224, '"Brace Yourself!"': 1572, '"Can\'t Touch This!"': 1780, '"Fall Back!"': 1595, '"Find Their Weakness!"': 1781, '"Go for the Eyes!"': 1558, '"Help Me!"': 1594, '"Incoming!"': 1596, '"Make Haste!"': 1591, '"Never Give Up!"': 1593, '"Never Surrender!"': 1598, '"Stand Your Ground!"': 1589, '"We Shall Return!"': 1592, 'Anthem of Disruption': 2018, 'Anthem of Envy': 1559, 'Anthem of Guidance': 1568, 'Anthem of Weariness': 2017, 'Bladeturn Refrain': 1580, 'Crippling Anthem': 1554, 'Godspeed': 1556, '"Lead the Way!"': 1590, '"Make Your Time!"': 1779, '"They\'re on Fire!"': 1597, 'Aggressive Refrain': 1774, 'Angelic Bond': 1587, 'Angelic Protection': 1586, 'Anthem of Flame': 1557, 'Anthem of Fury': 1553, 'Awe': 1573, 'Blazing Finale': 1575, 'Burning Refrain': 1576, 'Burning Shield': 2208, 'Defensive Anthem': 1555, 'Enduring Harmony': 1574, 'Focused Anger': 1769, 'Glowing Signet': 1581, 'Hasty Refrain': 2075, "Leader's Comfort": 1584, 'Natural Temper': 1770, 'Signet of Return': 1778, "Soldier's Fury": 1773, 'Spear Swipe': 2210, '"It\'s Just a Flesh Wound."': 1599, '"The Power Is Yours!"': 1782, 'Aria of Restoration': 1566, 'Aria of Zeal': 1562, 'Ballad of Restoration': 1564, 'Chorus of Restoration': 1565, 'Energizing Chorus': 1569, 'Energizing Finale': 1775, 'Finale of Restoration': 1577, 'Inspirational Speech': 2207, "Leader's Zeal": 1583, 'Lyric of Purification': 1772, 'Lyric of Zeal': 1563, 'Mending Refrain': 1578, 'Purifying Finale': 1579, 'Signet of Synergy': 1585, 'Song of Power': 1560, 'Song of Purification': 1570, 'Song of Restoration': 1771, 'Zealous Anthem': 1561, 'Cruel Spear': 1548, 'Barbed Spear': 1600, 'Blazing Spear': 1546, 'Chest Thumper': 2074, 'Disrupting Throw': 1604, "Harrier's Toss": 1549, 'Holy Spear': 2209, 'Maiming Spear': 2150, 'Merciless Spear': 1603, 'Mighty Throw': 1547, "Slayer's Spear": 1783, 'Spear of Lightning': 1551, 'Spear of Redemption': 2238, 'Stunning Strike': 1602, 'Swift Javelin': 1784, 'Unblockable Throw': 1550, 'Vicious Attack': 1601, 'Wearying Spear': 1552, 'Wild Throw': 1605, 'Cautery Signet': 1588, 'Hexbreaker Aria': 1571, 'Remedy Signet': 1777, 'Signet of Aggression': 1776, 'Song of Concentration': 1567, 'Armor of Sanctity': 1515, 'Aura of Thorns': 1495, 'Conviction': 1540, 'Dust Cloak': 1497, 'Ebon Dust Aura': 1760, 'Fleeting Stability': 1514, 'Mirage Cloak': 1500, 'Mystic Regeneration': 1516, 'Mystic Sandstorm': 1532, 'Pious Concentration': 1542, 'Sand Shards': 1510, 'Shield of Force': 2201, 'Signet of Pious Light': 1530, 'Staggering Force': 1498, 'Veil of Thorns': 1757, 'Vital Boon': 1506, 'Vow of Strength': 1759, 'Arcane Zeal': 1502, 'Aura Slicer': 2070, 'Avatar of Balthazar': 1518, 'Avatar of Dwayna': 1519, 'Avatar of Grenth': 1520, 'Avatar of Lyssa': 1521, 'Avatar of Melandru': 1522, "Balthazar's Rage": 1496, 'Banishing Strike': 1483, "Eremite's Zeal": 1524, 'Extend Enchantments': 1508, 'Faithful Intervention': 1509, 'Heart of Fury': 1762, 'Heart of Holy Flame': 1507, 'Imbue Health': 1526, 'Intimidating Aura': 1531, 'Meditation': 1523, 'Mystic Corruption': 1755, 'Mystic Sweep': 1484, 'Mystic Vigor': 1503, 'Pious Fury': 2146, 'Pious Haste': 1543, 'Pious Renewal': 1499, 'Rending Touch': 1534, 'Vow of Silence': 1517, 'Watchful Intervention': 1504, 'Zealous Renewal': 1763, "Lyssa's Assault": 1538, 'Chilling Victory': 1539, 'Crippling Sweep': 1535, 'Crippling Victory': 2147, "Eremite's Attack": 1485, "Farmer's Scythe": 2015, 'Irresistible Sweep': 1489, 'Pious Assault': 1490, 'Radiant Scythe': 2012, 'Reap Impurities': 1486, "Reaper's Sweep": 1767, 'Rending Sweep': 1753, 'Twin Moon Sweep': 1487, 'Victorious Sweep': 1488, 'Wearying Strike': 1537, 'Wounding Strike': 1536, 'Zealous Sweep': 2071, "Attacker's Insight": 1764, "Dwayna's Touch": 1528, 'Featherfoot Grace': 1766, "Grenth's Aura": 2013, "Grenth's Fingers": 1493, "Grenth's Grasp": 1756, 'Guiding Hands': 1513, "Harrier's Grasp": 1758, "Harrier's Haste": 1768, "Lyssa's Haste": 1512, 'Mystic Healing': 1527, 'Mystic Twister': 1491, 'Natural Healing': 1525, 'Onslaught': 1754, 'Pious Restoration': 1529, 'Rending Aura': 1765, 'Signet of Mystic Speed': 2200, 'Signet of Pious Restraint': 2014, 'Test of Faith': 1545, 'Vow of Piety': 1505, 'Whirling Charge': 1544, 'Winds of Disenchantment': 1533, 'Zealous Vow': 1761, 'Enchanted Haste': 1541, 'Whirlwind Attack': 2107, 'Never Rampage Alone': 2108, 'Seed of Life': 2105, 'Necrosis': 2103, 'Cry of Pain': 2102, 'Intensity': 2104, 'Critical Agility': 2101, 'Vampirism': 2110, '"There\'s Nothing to Fear!"': 2112, 'Eternal Aura': 2109, 'Sunspear Rebirth Signet': 1816, 'Lightbringer Signet': 1815, "Lightbringer's Gaze": 1814, 'Radiation Field': 2414, 'Air of Superiority': 2416, 'Asuran Scan': 2415, 'Mental Block': 2417, 'Mindbender': 2411, 'Pain Inverter': 2418, 'Smooth Criminal': 2412, 'Summon Ice Imp': 2226, 'Summon Mursaat': 2224, 'Summon Naga Shaman': 2227, 'Summon Ruby Djinn': 2225, 'Technobabble': 2413, '"By Ural\'s Hammer!"': 2217, '"Don\'t Trip!"': 2216, "Alkar's Alchemical Acid": 2211, 'Black Powder Mine': 2223, 'Brawling Headbutt': 2215, 'Breath of the Great Dwarf': 2221, 'Drunken Master': 2218, 'Dwarven Stability': 2423, 'Ear Bite': 2213, 'Great Dwarf Armor': 2220, 'Great Dwarf Weapon': 2219, 'Light of Deldrimor': 2212, 'Low Blow': 2214, 'Snow Storm': 2222, 'Deft Strike': 2228, 'Ebon Battle Standard of Courage': 2231, 'Ebon Battle Standard of Honor': 2233, 'Ebon Battle Standard of Wisdom': 2232, 'Ebon Escape': 2420, 'Ebon Vanguard Assassin Support': 2235, 'Ebon Vanguard Sniper Support': 2234, 'Signet of Infection': 2229, 'Sneak Attack': 2116, 'Tryptophan Signet': 2230, 'Weakness Trap': 2421, 'Winds': 2422, '"Dodge This!"': 2354, '"Finish Him!"': 2353, '"I Am the Strongest!"': 2355, '"I Am Unstoppable!"': 2356, '"You Are All Weaklings!"': 2359, '"You Move Like a Dwarf!"': 2358, 'A Touch of Guile': 2357, 'Club of a Thousand Bears': 2361, 'Feel No Pain': 2360, 'Raven Blessing': 2384, 'Ursan Blessing': 2374, 'Volfen Blessing': 2379, 'Enraged Smash (PvP)': 2808, 'Renewing Smash (PvP)': 3143, 'Defy Pain (PvP)': 3204, "Warrior's Endurance (PvP)": 3002, '"Watch Yourself!" (PvP)': 2858, "Soldier's Stance (PvP)": 3156, '"For Great Justice!" (PvP)': 2883, 'Call of Haste (PvP)': 2657, 'Charm Animal (Codex)': 3068, 'Comfort Animal (PvP)': 3045, 'Enraged Lunge (PvP)': 3051, 'Heal as One (PvP)': 3144, "Melandru's Assault (PvP)": 3047, 'Predatory Bond (PvP)': 3050, "Expert's Dexterity (PvP)": 2959, 'Escape (PvP)': 3060, 'Glass Arrows (PvP)': 3145, 'Lightning Reflexes (PvP)': 3141, 'Penetrating Attack (PvP)': 2861, 'Read the Wind (PvP)': 2969, "Sloth Hunter's Shot (PvP)": 2925, 'Sundering Attack (PvP)': 2864, 'Keen Arrow (PvP)': 3147, "Smiter's Boon (PvP)": 2895, 'Unyielding Aura (PvP)': 2891, 'Light of Deliverance (PvP)': 2871, 'Heal Party (PvP)': 3232, 'Aegis (PvP)': 2857, 'Spirit Bond (PvP)': 2892, 'Signet of Judgment (PvP)': 2887, 'Strength of Honor (PvP)': 2999, 'Signet of Agony (PvP)': 3059, 'Spoil Victor (PvP)': 3233, 'Unholy Feast (PvP)': 3058, 'Enfeeble (PvP)': 2859, 'Enfeebling Blood (PvP)': 2885, 'Discord (PvP)': 2863, 'Masochism (PvP)': 3054, 'Empathy (PvP)': 3151, "Enchanter's Conundrum (PvP)": 3192, 'Mind Wrack (PvP)': 2734, 'Mistrust (PvP)': 3191, 'Shatter Delusions (PvP)': 3180, 'Spiritual Pain (PvP)': 3189, 'Unnatural Signet (PvP)': 3188, 'Visions of Regret (PvP)': 3234, 'Psychic Instability (PvP)': 3185, 'Stolen Speed (PvP)': 3187, 'Accumulated Pain (PvP)': 3184, 'Calculated Risk (PvP)': 3196, 'Crippling Anguish (PvP)': 3152, 'Fevered Dreams (PvP)': 3289, 'Fragility (PvP)': 2998, 'Frustration (PvP)': 3190, 'Illusion of Haste (PvP)': 3373, 'Illusion of Pain (PvP)': 3374, 'Illusionary Weaponry (PvP)': 3181, 'Migraine (PvP)': 3183, 'Shared Burden (PvP)': 3186, 'Signet of Clumsiness (PvP)': 3193, 'Wandering Eye (PvP)': 3195, 'Mantra of Resolve (PvP)': 3063, 'Mantra of Signets (PvP)': 3179, 'Mirror of Disenchantment (PvP)': 3194, 'Web of Disruption (PvP)': 3386, 'Lightning Hammer (PvP)': 3396, 'Mind Shock (PvP)': 2804, 'Ride the Lightning (PvP)': 2807, 'Obsidian Flame (PvP)': 2809, 'Ether Renewal (PvP)': 2860, 'Aura of Restoration (PvP)': 3375, 'Elemental Flame (PvP)': 3397, 'Savannah Heat (PvP)': 3021, 'Mind Freeze (PvP)': 2803, 'Mist Form (PvP)': 2805, 'Slippery Ground (PvP)': 3398, 'Ward Against Harm (PvP)': 2806, "Assassin's Remedy (PvP)": 2869, 'Death Blossom (PvP)': 3061, 'Fox Fangs (PvP)': 3251, 'Wild Strike (PvP)': 3252, 'Signet of Deadly Corruption (PvP)': 3053, 'Shadow Form (PvP)': 2862, 'Shroud of Distress (PvP)': 3048, 'Unseen Fury (PvP)': 3049, "Ancestors' Rage (PvP)": 2867, 'Signet of Spirits (PvP)': 2965, 'Splinter Weapon (PvP)': 2868, 'Agony (PvP)': 3038, 'Bloodsong (PvP)': 3019, 'Destruction (PvP)': 3008, 'Gaze of Fury (PvP)': 3022, 'Signet of Ghostly Might (PvP)': 2966, 'Anguish (PvP)': 3023, 'Armor of Unfeeling (PvP)': 3003, 'Disenchantment (PvP)': 3017, 'Displacement (PvP)': 3010, 'Dissonance (PvP)': 3014, 'Earthbind (PvP)': 3015, 'Pain (PvP)': 3007, 'Restoration (PvP)': 3018, 'Shadowsong (PvP)': 3006, 'Shelter (PvP)': 3016, 'Soothing (PvP)': 3009, 'Union (PvP)': 3005, 'Wanderlust (PvP)': 3020, 'Death Pact Signet (PvP)': 2872, 'Flesh of My Flesh (PvP)': 2866, 'Weapon of Warding (PvP)': 2893, 'Life (PvP)': 3012, 'Preservation (PvP)': 3011, 'Recovery (PvP)': 3025, 'Recuperation (PvP)': 3013, 'Rejuvenation (PvP)': 3039, 'Empowerment (PvP)': 3024, '"Incoming!" (PvP)': 2879, '"Never Surrender!" (PvP)': 2880, '"Brace Yourself!" (PvP)': 3027, '"Can\'t Touch This!" (PvP)': 3031, '"Fall Back!" (PvP)': 3037, '"Find Their Weakness!" (PvP)': 3034, '"Go for the Eyes!" (PvP)': 3026, '"Help Me!" (PvP)': 3036, '"Never Give Up!" (PvP)': 3035, '"Stand Your Ground!" (PvP)': 3032, '"We Shall Return!" (PvP)': 3033, 'Anthem of Disruption (PvP)': 3040, 'Anthem of Envy (PvP)': 3148, 'Bladeturn Refrain (PvP)': 3029, 'Defensive Anthem (PvP)': 2876, 'Blazing Finale (PvP)': 3028, 'Signet of Return (PvP)': 3030, 'Ballad of Restoration (PvP)': 2877, 'Song of Restoration (PvP)': 2878, 'Finale of Restoration (PvP)': 3062, 'Mending Refrain (PvP)': 3149, "Harrier's Toss (PvP)": 2875, 'Mystic Regeneration (PvP)': 2884, 'Aura of Thorns (PvP)': 3346, 'Dust Cloak (PvP)': 3347, 'Avatar of Dwayna (PvP)': 3270, 'Avatar of Melandru (PvP)': 3271, 'Banishing Strike (PvP)': 3263, 'Heart of Fury (PvP)': 3366, 'Pious Fury (PvP)': 3368, 'Irresistible Sweep (PvP)': 3265, 'Pious Assault (PvP)': 3266, 'Twin Moon Sweep (PvP)': 3264, 'Wounding Strike (PvP)': 3367, 'Guiding Hands (PvP)': 3269, "Lyssa's Haste (PvP)": 3348, 'Mystic Healing (PvP)': 3272, 'Onslaught (PvP)': 3365, 'Signet of Pious Restraint (PvP)': 3273, 'Time Ward': 3422, 'Soul Taker': 3423, 'Over the Limit': 3424, 'Judgment Strike': 3425, 'Seven Weapons Stance': 3426, '"Together as One!"': 3427, 'Shadow Theft': 3428, 'Weapons of Three Forges': 3429, 'Vow of Revolution': 3430, 'Heroic Refrain': 3431})

def WriteBuild():
    Data = {PRIMARY: 0,
            SECONDARY: 0,
            ATTRIBUTES: dict(),
            SKILLS: []}
    
    print("Enter Primary Profession:")
    Input = input()
    while Input not in ProfessionDict.keys():
        print("Invalid Profession. Try Again:")
        Input = input()
    Data[PRIMARY] = ProfessionDict[Input]
    
    print("Enter Secondary Profession (Enter Nothing Or 'None' For No Secondary Profession):")
    Input = input()
    if Input=="":
        Input = "None"
    while Input not in ProfessionDict.keys() or Input==ProfessionDict.inv[Data[PRIMARY]]:
        print("Invalid Profession. Try Again:")
        Input = input()
        if Input=="":
            Input = "None"
    Data[SECONDARY] = ProfessionDict[Input]

    Input="Not Done"
    while not Input == "":
        print("Enter Attribute (Enter Nothing To Finish Entering Attributes):")
        Input = input()
        if Input=="":
            break
        else:
            while Input not in AttributeDict.keys():
                print("Invalid Attribute. Try Again:")
                Input = input()
                if Input == "":
                    break
            else:
                print("Enter Value (0-12):")
                Data[ATTRIBUTES][AttributeDict[Input]] = int(input())

    for SkillNum in range(8):
        print("Enter Skill "+str(SkillNum+1)+" (Enter Nothing Or 'No Skill' For No Skill):")
        Input = input()
        if Input=="":
            Input = "No Skill"
        while Input not in SkillDict.keys():
            print("Invalid Skill. Try Again:")
            Input = input()
            if Input == "":
                Input = "No Skill"
        Data[SKILLS].append(SkillDict[Input])

    return BitsToBase64(DataToBits(Data))
        
def FastLog2(Num):
    Result=0
    while Num>1:
        Num = Num//2
        Result+=1
    return Result+1

def DataToBits(Data):
    Bits=""
    #Header
    Bits+=IntToBin(14, Length=4)
    Bits+=IntToBin(0, Length=4)
    #Professions
    BitsPerProfession = max(FastLog2(max(Data[PRIMARY], Data[SECONDARY])) + FastLog2(max(Data[PRIMARY], Data[SECONDARY]))%2, 4)
    Bits+=IntToBin((BitsPerProfession-4)//2, Length=2)
    Bits+=IntToBin(Data[PRIMARY], Length=BitsPerProfession)
    Bits+=IntToBin(Data[SECONDARY], Length=BitsPerProfession)
    #Attributes
    Bits+=IntToBin(len(Data[ATTRIBUTES]), Length=4)
    BitsPerAttribute = max(FastLog2(max(Data[ATTRIBUTES].keys())), 4)
    Bits+=IntToBin(BitsPerAttribute-4, Length=4)
    for Attribute in Data[ATTRIBUTES].keys():
        Bits+=IntToBin(Attribute, Length=BitsPerAttribute)
        Bits+=IntToBin(Data[ATTRIBUTES][Attribute], Length = 4)
    #Skills
    BitsPerSkill = max(FastLog2(max(Data[SKILLS])), 8)
    Bits+=IntToBin(BitsPerSkill-8, Length=4)
    for Skill in Data[SKILLS]:
        Bits+=IntToBin(Skill, Length=BitsPerSkill)
    return Bits

def BitsToBase64(Bits):
    Bits = Bits.ljust((len(Bits)//6 + (len(Bits)%6 != 0))*6, "0")
    Base64=""
    Pointer = 0
    while Pointer<len(Bits):
        Number, Pointer = ReadBitNum(Bits, Pointer, 6)
        Base64+=Base64Dict.inv[Number]
    return Base64

def IntToBin(Int, Length=8):
    # Anet uses reversed binary numbers, god knows why
    return (('{0:0'+str(Length)+"b}").format(Int))[::-1]

def ReadBuild(String):
    Bits = "".join(list([IntToBin(Base64Dict[Char], Length=6) for Char in String]))
    Data = {PRIMARY: 0,
            SECONDARY: 0,
            ATTRIBUTES: dict(),
            SKILLS: []}
    Pointer = 0
    Pointer = CheckHeader(Bits, Pointer)
    Pointer, Data[PRIMARY], Data[SECONDARY] = GetProfessions(Bits, Pointer)
    Pointer, Data[ATTRIBUTES] = GetAttributes(Bits, Pointer)
    Pointer, Data[SKILLS] = GetSkills(Bits, Pointer)
    return DisplayData(Data)

def CheckHeader(Bits, Pointer):
    TemplateType, Pointer = ReadBitNum(Bits, Pointer, 4)
    if TemplateType == 0:
        return Pointer
    elif TemplateType == 14:
        VersionNum, Pointer = ReadBitNum(Bits, Pointer, 4)
        if VersionNum==0:
            return Pointer
        else:
            raise Exception("Invalid Version Number")
    else:
        raise Exception("Invalid Template Type")

def GetProfessions(Bits, Pointer):
    BitsPerProfession, Pointer = ReadBitNum(Bits, Pointer, 2)
    BitsPerProfession *= 2
    BitsPerProfession += 4
    PrimaryProfession, Pointer = ReadBitNum(Bits, Pointer, BitsPerProfession)
    SecondaryProfession, Pointer = ReadBitNum(Bits, Pointer, BitsPerProfession)
    return Pointer, PrimaryProfession, SecondaryProfession

def GetAttributes(Bits, Pointer):
    AttributeCount, Pointer = ReadBitNum(Bits, Pointer, 4)
    BitsPerAttribute, Pointer = ReadBitNum(Bits, Pointer, 4)
    BitsPerAttribute+=4
    Attributes = dict()
    for _ in range(AttributeCount):
        Attribute, Pointer = ReadBitNum(Bits, Pointer, BitsPerAttribute)
        Points, Pointer = ReadBitNum(Bits, Pointer, 4)
        Attributes[Attribute] = Points
    return Pointer, Attributes

def GetSkills(Bits, Pointer):
    BitsPerSkill, Pointer = ReadBitNum(Bits, Pointer, 4)
    BitsPerSkill+=8
    Skills=[]
    for _ in range(8):
        Skill, Pointer = ReadBitNum(Bits, Pointer, BitsPerSkill)
        Skills.append(Skill)
    return Pointer, Skills
    

def ReadBitNum(Bits, Pointer, Length):
    Num = 0
    for Offset in range(Length):
        Num+=int(Bits[Pointer+Offset])*2**(Offset)
    Pointer+=Length
    return Num, Pointer

def DisplayData(Data):
    return ("Primary Profession: "+Try(lambda: ProfessionDict.inv[Data[PRIMARY]], Error=KeyError)+
    "\nSecondary Profession: "+Try(lambda: ProfessionDict.inv[Data[SECONDARY]], Error=KeyError)+
    "\nAttributes:\n\t"+"\n\t".join(list([Try(lambda: AttributeDict.inv[Each], Error=KeyError)+": "+str(Data[ATTRIBUTES][Each]) for Each in Data[ATTRIBUTES]]))+
    "\nSkills:\n\t"+"\n\t".join(list([Try(lambda: SkillDict.inv[Each], Error=KeyError) for Each in Data[SKILLS]])))

def Try(Function, Default="Unknown", Error=Exception):
    try:
        return Function()
    except Error:
        return Default

while True:
    print("Read Skill Template ('Read'/'R'), Create New ('New'/'N') Or Exits ('Exit'/'E')?")
    Type = input()
    if Type == "Read" or Type == "R":
        print("Enter Build Template String:")
        print(ReadBuild(input()))
    elif Type == "New" or Type == "N":
        print(WriteBuild())
    elif Type == "Exit" or Type == "E":
        break
