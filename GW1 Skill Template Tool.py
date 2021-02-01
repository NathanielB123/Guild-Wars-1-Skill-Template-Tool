from random import choice
from Data import ProfessionDict, ProfessionDict, DualProfessions, Base64Dict, AttributeDict, SkillDict, StoredNPCs

PRIMARY="Pr"
SECONDARY="Se"
ATTRIBUTES="At"
SKILLS = "Sk"

PROPHECIES = "P"
FACTIONS = "F"
NIGHTFALL = "N"
ALL = "A"

NPCs = {'Sunspear Recruit': ('Allies', 'Humans', 'Ranger', 2, 20), 'Kormir': ('Allies', 'Humans', 'Paragon', 20, 20), 'Corsair Buccaneer': ('Foes', 'Humans (Corsairs)', 'Warrior', 1, 22), 'Corsair': ('Foes', 'Humans (Corsairs)', 'Ranger', 0, 22), 'Corsair Spotter': ('Foes', 'Humans (Corsairs)', 'Ranger', 0, 22), 'Corsair Healer': ('Foes', 'Humans (Corsairs)', 'Monk', 1, 22), 'Corsair Mage': ('Foes', 'Humans (Corsairs)', 'Elementalist', 0, 22), 'Midshipman Bennis': ('Bosses', 'Humans (Corsairs)', 'Paragon', 4, 26), 'Ghostly Sunspear Commander': ('Allies', 'Ghosts (Order of the Sunspears)', 'Warrior', 12, 20), 'Kahdash': ('Allies', 'Ghosts (Order of the Sunspears)', 'Warrior', 12, 20), 'Grub Lance': ('Foes', 'Insects', 'Monk', 8, 23), 'Preying Lance': ('Foes', 'Insects', 'Paragon', 8, 23), 'Fanged Iboga': ('Foes', 'Plants', 'Mesmer', 10, 24), 'Stormseed Jacaranda': ('Foes', 'Plants', 'Elementalist', 10, 24), 'Darehk the Quick': ('Foes', 'Ghosts', 'Warrior', 12, 20), 'Relentless Corpse': ('Foes', 'Skeletons (Undead)', 'Warrior', 10, 24), 'Restless Dead': ('Foes', 'Skeletons (Undead)', 'Necromancer', 10, 24), 'Apocrypha': ('Foes', 'Monoliths', 'MesmerParagonDervish', 13, 24), 'Corsair Raider': ('Allies', 'Humans (Corsairs)', 'Ranger', 15, 20), 'Ironhook Hube': ('Allies', 'Humans (Corsairs)', 'Ranger', 15, 20), 'Corsair Wizard': ('Allies', 'Humans (Corsairs)', 'Mesmer', 14, 20), 'Captain Besuz': ('Allies', 'Humans (Corsairs)', 'Elementalist', 15, 20), 'Corsair Commandant': ('Allies', 'Humans (Corsairs)', 'Paragon', 16, 20), 'Corsair Berserker': ('Allies', 'Humans (Corsairs)', 'Dervish', 15, 20), 'Rinkhal Monitor': ('Foes', 'Beasts', 'Monk', 13, 24), 'Grasp of Chaos': ('Foes', 'Demons (Torment creatures)', 'Warrior', 12, 20), 'Corsair Bosun': ('Foes', 'Humans (Corsairs)', 'Monk', 15, 25), 'Corsair Blackhand': ('Foes', 'Humans (Corsairs)', 'Necromancer', 15, 25), 'Corsair Cook': ('Foes', 'Humans (Corsairs)', 'Elementalist', 16, 25), "Ironfist's Envoy": ('Foes', 'Humans (Corsairs)', 'Paragon', 16, 25), 'Ridgeback Skale': ('Foes', 'Skales', 'Warrior', 13, 24), 'Skale Blighter': ('Foes', 'Skales', 'Necromancer', 13, 24), 'Frigid Skale': ('Foes', 'Skales', 'Elementalist', 14, 24), 'Skale Lasher': ('Foes', 'Skales', 'Dervish', 15, 24), 'Skree Talon': ('Foes', 'Skree harpies', 'Warrior', 12, 24), 'Skree Hunter': ('Foes', 'Skree harpies', 'Ranger', 11, 24), 'Skree Griffon': ('Foes', 'Skree harpies', 'Monk', 14, 24), 'Skree Warbler': ('Foes', 'Skree harpies', 'Paragon', 13, 24), 'General Kahyet': ('Bosses', 'Humans (Corsairs)', 'Dervish', 18, 24), 'Boklon Blackwater': ('Bosses', 'Skales', 'Necromancer', 17, 28), 'Glug Klugg': ('Bosses', 'Skales', 'Necromancer', 17, 28), 'Ahtok': ('Allies', 'Human (Order of the Sunspear)', 'Ranger', 20, 20), 'Nerashi': ('Allies', 'Human (Order of the Sunspear)', 'Ranger', 20, 20), 'Lonai': ('Allies', 'Human (Order of the Sunspear)', 'Necromancer', 20, 20), 'Rojis': ('Allies', 'Human (Order of the Sunspear)', 'Elementalist', 20, 20), 'Sunspear Warrior': ('Allies', 'Human (Order of the Sunspear)', 'Warrior', 20, 20), 'Sunspear Ranger': ('Allies', 'Human (Order of the Sunspear)', 'Ranger', 20, 20), 'Sunspear Paragon': ('Allies', 'Human (Order of the Sunspear)', 'Paragon', 20, 20), 'Kournan Guard': ('Foes', 'Humans (Kournan military)', 'Warrior', 20, 26), 'Kournan Elite Guard': ('Foes', 'Humans (Kournan military)', 'Warrior', 22, 26), 'Kournan Spotter': ('Foes', 'Humans (Kournan military)', 'Ranger', 20, 26), 'Kournan Bowman': ('Foes', 'Humans (Kournan military)', 'Ranger', 20, 26), 'Kournan Priest': ('Foes', 'Humans (Kournan military)', 'Monk', 16, 25), 'Kournan Oppressor': ('Foes', 'Humans (Kournan military)', 'Necromancer', 20, 26), 'Kournan Seer': ('Foes', 'Humans (Kournan military)', 'Mesmer', 20, 26), 'Kournan Siege Engineer': ('Foes', 'Humans (Kournan military)', 'Mesmer', 20, 26), 'Kournan Scribe': ('Foes', 'Humans (Kournan military)', 'Elementalist', 20, 26), 'Kournan Zealot': ('Foes', 'Humans (Kournan military)', 'Dervish', 20, 26), 'Kournan Elite Zealot': ('Foes', 'Humans (Kournan military)', 'Dervish', 22, 26), 'Kournan Phalanx': ('Foes', 'Humans (Kournan military)', 'Paragon', 20, 26), 'Kournan Elite Spear': ('Foes', 'Humans (Kournan military)', 'Paragon', 22, 26), 'Kournan Field Commander': ('Foes', 'Humans (Kournan military)', 'Paragon', 24, 26), 'Captain Kavaka': ('Bosses', 'Humans (Kournan military)', 'Warrior', 24, 30), 'Captain Mwende': ('Bosses', 'Humans (Kournan military)', 'Elementalist', 24, 30), 'Captain Lumanda': ('Bosses', 'Humans (Kournan military)', 'Paragon', 24, 30), 'Captain Denduru': ('Bosses', 'Humans (Kournan military)', 'Dervish', 24, 30), 'Margrid the Sly': ('Allies', 'Humans', 'Ranger', 18, 20), 'Sunspear Evacuee': ('Allies', 'Humans', 'Monk', 20, 20), 'Guard Post Commander': ('Foes', 'Humans (Kournan military)', 'Paragon', 20, 26), 'Haroj Firemane': ('Allies', 'Centaurs', 'Ranger', 20, 20), 'Veldrunner Centaur': ('Allies', 'Centaurs', 'Ranger', 20, 20), 'Mirza Veldrunner': ('Allies', 'Centaurs', 'Paragon', 20, 20), 'Kournan Taskmaster': ('Foes', 'Humans (Kournan military)', 'Warrior', 24, 30), 'Kournan Elite Scribe': ('Foes', 'Humans (Kournan military)', 'Elementalist', 22, 26), 'Taskmaster Sadi-Belai': ('Bosses', 'Humans (Kournan military)', 'Monk', 24, 30), 'Overseer Haubeh': ('Bosses', 'Humans (Kournan military)', 'Necromancer', 24, 30), 'Taskmaster Vanahk': ('Bosses', 'Humans (Kournan military)', 'Necromancer', 24, 30), 'Overseer Boktek': ('Bosses', 'Humans (Kournan military)', 'Paragon', 24, 30), 'Taskmaster Suli': ('Bosses', 'Humans (Kournan military)', 'Dervish', 24, 30), 'Captain Nahnkos': ('Allies', 'Humans', 'Warrior', 20, 20), 'Guard Captain Kahturin': ('Allies', 'Humans', 'Warrior', 20, 20), 'Kournan Captain': ('Allies', 'Humans', 'Warrior', 20, 20), 'Vault Master Eijah': ('Allies', 'Humans', 'Warrior', 20, 20), 'Guard Linko': ('Allies', 'Humans', 'Warrior', 20, 20), 'Jailer Gahanni': ('Allies', 'Humans', 'Warrior', 20, 20), 'Prison Keeper Shelkesh': ('Allies', 'Humans', 'Warrior', 20, 20), 'Vabbi Guard': ('Allies', 'Humans', 'Warrior', 20, 20), 'Shahai the Cunning': ('Allies', 'Humans', 'Monk', 20, 20), 'Sunspear Prisoner': ('Allies', 'Humans', 'Warrior', 20, 20), 'Demon Spawn': ('Foes', 'Demon (Torment creature)', 'Mesmer', 20, 29), 'Lieutenant Nali': ('Bosses', 'Humans (Kournan military)', 'Mesmer', 24, 30), 'Captain Nebo': ('Bosses', 'Humans (Kournan military)', 'Elementalist', 24, 30), 'Colonel Kajo': ('Bosses', 'Humans (Kournan military)', 'Paragon', 24, 30), 'Dehjah': ('Allies', 'Elementals', 'Dervish', 20, 20), 'Agent of Whispers': ('Allies', 'Humans', 'Warrior', 20, 20), 'Kournan Engineer': ('Allies', 'Humans', 'Elementalist', 20, 20), 'Steelfang Drake': ('Foes', 'Dragons', 'Warrior', 20, 26), 'Droughtling': ('Foes', 'Elementals', 'Elementalist', 24, 26), 'Bladed Veldt Termite': ('Foes', 'Insects', 'Warrior', 20, 26), 'Veldt Beetle Queen': ('Foes', 'Insects', 'Monk', 20, 26), 'Veldt Beetle Lance': ('Foes', 'Insects', 'Paragon', 20, 26), 'The Drought': ('Bosses', 'Elementals', 'Elementalist', 28, 30), 'Veldt Nephila': ('Foes', 'Arachnids', 'Ranger', 20, 26), 'Corsair Cutthroat': ('Foes', 'Humans (Corsairs)', 'Warrior', 17, 20), 'Corsair Weapons Master': ('Foes', 'Humans (Corsairs)', 'Warrior', 21, 26), 'Corsair Lieutenant': ('Foes', 'Humans (Corsairs)', 'Ranger', 22, 26), 'Corsair Runner': ('Foes', 'Humans (Corsairs)', 'Ranger', 22, 26), 'Corsair Doctor': ('Foes', 'Humans (Corsairs)', 'Monk', 22, 26), 'Corsair Wind Master': ('Foes', 'Humans (Corsairs)', 'Elementalist', 21, 26), 'Captain Bohseda': ('Foes', 'Humans (Corsairs)', 'Paragon', 16, 20), 'Corsair Admiral': ('Foes', 'Humans (Corsairs)', 'Paragon', 23, 26), 'Mandragor Slither': ('Foes', 'Mandragors', 'Warrior', 22, 26), 'Mandragor Imp': ('Foes', 'Mandragors', 'Necromancer', 22, 26), 'Stoneflesh Mandragor': ('Foes', 'Mandragors', 'Elementalist', 22, 24), 'Ranshek, Carrion Eater': ('Bosses', 'Insects', 'Warrior', 24, 30), 'Kehmak the Tranquil': ('Bosses', 'Insects', 'Monk', 24, 30), 'Yakun Trueshot': ('Bosses', 'Insects', 'Paragon', 24, 30), 'General Bayel': ('Bosses', 'Humans (Kournan military)', 'Monk', 28, 30), 'Istani Peasant': ('Allies', 'Humans', 'Ranger', 20, 20), 'Elder Jonah': ('Allies', 'Humans', 'Monk', 20, 20), 'Margonite Executioner': ('Foes', 'Demons (Margonites)', 'Warrior', 24, 26), 'Margonite Bowmaster': ('Foes', 'Demons (Margonites)', 'Ranger', 24, 26), 'Margonite Cleric': ('Foes', 'Demons (Margonites)', 'Monk', 24, 26), 'Margonite Warlock': ('Foes', 'Demons (Margonites)', 'Necromancer', 24, 26), 'Margonite Seer': ('Foes', 'Demons (Margonites)', 'Mesmer', 24, 26), 'Margonite Sorcerer': ('Foes', 'Demons (Margonites)', 'Elementalist', 24, 26), 'Margonite Ascendant': ('Foes', 'Demons (Margonites)', 'Paragon', 24, 26), 'Margonite Reaper': ('Foes', 'Demons (Margonites)', 'Dervish', 24, 26), 'Harbinger of Twilight': ('Foes', 'Demons (Torment creatures)', 'Warrior', 28, 30), 'Harbinger of Nightfall': ('Foes', 'Demons (Torment creatures)', 'Warrior', 28, 30), 'Priest Zein Zuu': ('Bosses', 'Demons (Margonites)', 'Monk', 28, 30), 'Scribe Wensal': ('Bosses', 'Demons (Margonites)', 'Elementalist', 28, 30), 'Commander Chutal': ('Bosses', 'Demons (Margonites)', 'Paragon', 28, 30), 'Zealot Sheoli': ('Bosses', 'Demons (Margonites)', 'Dervish', 28, 30), 'Palace Guard': ('Allies', 'Humans', 'Warrior', 20, 20), 'Vabbi Guard Captain': ('Allies', 'Humans', 'Warrior', 20, 20), 'Duel Master Lumbo': ('Allies', 'Humans', 'Warrior', 10, 20), 'Goren': ('Allies', 'Humans', 'Warrior', 18, 20), 'Kurideh the Mad': ('Allies', 'Humans', 'Warrior', 10, 20), 'Lieutenant Murunda': ('Allies', 'Humans', 'Warrior', 20, 20), 'Zilo the Drunkard': ('Allies', 'Humans', 'Warrior', 10, 20), 'The Great Zehtuka': ('Allies', 'Humans', 'Ranger', 20, 20), 'Royal Servant': ('Allies', 'Humans', 'Warrior', 20, 20), 'Vabbi Noble': ('Allies', 'Humans', 'Warrior', 10, 20), 'Vaughn the Venerable': ('Allies', 'Humans', 'Ranger', 10, 20), 'Tahlkora': ('Allies', 'Humans', 'Monk', 12, 20), 'Kehanni': ('Allies', 'Humans', 'Mesmer', 20, 20), 'Norgu': ('Allies', 'Humans', 'Mesmer', 18, 20), 'Prince Bokka the Magnificent': ('Allies', 'Humans', 'Mesmer', 20, 20), 'General Morgahn': ('Allies', 'Humans', 'Paragon', 20, 20), 'Skree Raider': ('Foes', 'Harpies', 'Warrior', 24, 26), 'Skree Tracker': ('Foes', 'Harpies', 'Ranger', 24, 26), 'Skree Singer': ('Foes', 'Harpies', 'Paragon', 24, 26), 'Royal Guard Captain': ('Foes', 'Humans', 'Warrior', 20, 20), '"Palawa Joko"': ('Foes', 'Humans', 'Necromancer', 20, 20), 'Divine Guardian': ('Allies', 'Elemental (Djinn)', 'Paragon', 24, 24), 'Roaring Ether': ('Foes', 'Elementals', 'Mesmer', 24, 26), 'Ruby Djinn': ('Foes', 'Elementals (Djinn)', 'Elementalist', 24, 26), 'Ruby of Ahdashim': ('Foes', 'Elementals (Djinn)', 'Elementalist', 24, 26), 'Diamond of Ahdashim': ('Foes', 'Elementals (Djinn)', 'Paragon', 24, 26), 'Eternal Guardian of Languor': ('Foes', 'Elementals (Djinn)', 'Paragon', 24, 26), 'Eternal Guardian of Lethargy': ('Foes', 'Elementals (Djinn)', 'Paragon', 24, 26), 'Eternal Guardian of Suffering': ('Foes', 'Elementals (Djinn)', 'Paragon', 24, 26), 'Thunder of Ahdashim': ('Foes', 'Elementals (Djinn)', 'Paragon', 28, 30), 'Sapphire Djinn': ('Foes', 'Elementals (Djinn)', 'Dervish', 24, 26), 'Sapphire of Ahdashim': ('Foes', 'Elementals (Djinn)', 'Dervish', 24, 26), 'Kormab, Burning Heart': ('Bosses', 'Elemental (Djinn)', 'Elementalist', 28, 30), 'Shakor Firespear': ('Bosses', 'Elemental (Djinn)', 'Paragon', 28, 30), 'Hajok Earthguardian': ('Bosses', 'Elemental (Djinn)', 'Dervish', 28, 30), 'Vabbian Guard': ('Allies', 'Humans', 'Warrior', 20, 20), 'Disciple of Secrets': ('Allies', 'Humans', 'Mesmer', 20, 20), 'Mirage Iboga': ('Foes', 'Plants', 'Mesmer', 22, 26), 'Storm Jacaranda': ('Foes', 'Plants', 'Elementalist', 22, 26), 'Whistling Thornbrush': ('Foes', 'Plants', 'Paragon', 22, 26), 'Enchanted Brambles': ('Foes', 'Plants', 'Dervish', 22, 26), 'General Doriah': ('Bosses', 'Demons (Margonites)', 'Warrior', 28, 30), 'General Nimtak': ('Bosses', 'Demons (Margonites)', 'Monk', 28, 30), 'General Tirraj': ('Bosses', 'Demons (Margonites)', 'Elementalist', 28, 30), 'General Kumtash': ('Bosses', 'Demons (Margonites)', 'Paragon', 28, 30), 'Torment Claw': ('Foes', 'Demons (Torment creatures)', 'Warrior', 24, 26), 'Horticulturist Hinon': ('Allies', 'Human', 'Ranger', 20, 20), 'Harbinger': ('Foes', 'Demons (Torment creatures)', 'Warrior', 26, 30), 'Palawa Joko': ('Allies', 'Mummy (Undead)', 'Necromancer', 24, 24), 'Aijundu': ('Allies', 'Wurm', 'Ranger', 28, 28), 'Shambling Mesa': ('Foes', 'Elementals', 'Warrior', 24, 26), 'Sandstorm Crag': ('Foes', 'Elementals', 'Elementalist', 24, 26), 'Carven Effigy': ('Foes', 'Elementals (Undead)', 'Elementalist', 24, 26), 'Awakened Blademaster': ('Foes', 'Mummies (Undead)', 'Warrior', 24, 26), 'Awakened Gray Giant': ('Foes', 'Mummies (Undead)', 'Ranger', 24, 26), 'Awakened Acolyte': ('Foes', 'Mummies (Undead)', 'Monk', 24, 26), 'Awakened Defiler': ('Foes', 'Mummies (Undead)', 'Necromancer', 24, 26), 'Awakened Head': ('Foes', 'Mummies (Undead)', 'Mesmer', 24, 26), 'Awakened Thought Leech': ('Foes', 'Mummies (Undead)', 'Mesmer', 24, 26), 'Awakened Cavalier': ('Foes', 'Mummies (Undead)', 'Paragon', 24, 26), 'Awakened Dune Carver': ('Foes', 'Mummies (Undead)', 'Dervish', 24, 26), 'Avah the Crafty': ('Bosses', 'Mummies (Undead)', 'Warrior', 28, 30), 'Nehmak the Unpleasant': ('Bosses', 'Mummies (Undead)', 'Necromancer', 28, 30), 'Amind the Bitter': ('Bosses', 'Mummies (Undead)', 'Mesmer', 28, 30), 'Chakeh the Lonely': ('Bosses', 'Mummies (Undead)', 'Paragon', 28, 30), 'Chundu the Meek': ('Bosses', 'Mummies (Undead)', 'Dervish', 28, 30), 'Commander Varesh': ('Foes', 'Demons (Margonites)', 'Paragon', 30, 32), 'Prophet Varesh': ('Foes', 'Demons (Margonites)', 'Dervish', 29, 32), 'Arm of Insanity': ('Foes', 'Demons (Torment creatures)', 'Ranger', 28, 30), 'Shadow of Fear': ('Foes', 'Demons (Torment creatures)', 'Necromancer', 28, 30), 'Herald of Nightmares': ('Foes', 'Demons (Torment creatures)', 'Mesmer', 28, 30), 'Spear of Torment': ('Foes', 'Demons (Torment creatures)', 'Paragon', 28, 30), 'Rain of Terror': ('Foes', 'Demons (Torment creatures)', 'Elementalist', 28, 30), 'Lost Soul': ('Allies', 'Ghosts', 'Monk', 20, 20), 'Terrorweb Dryder': ('Foes', 'Dryders', 'Elementalist', 28, 30), 'Blade of Corruption': ('Foes', 'Demons (Torment creatures)', 'Warrior', 28, 30), 'Emissary of Dhuum': ('Foes', 'Demons (Torment creatures)', 'Warrior', 28, 28), 'Word of Madness': ('Foes', 'Demons (Torment creatures)', 'Monk', 28, 30), 'Scythe of Chaos': ('Foes', 'Demons (Torment creatures)', 'Dervish', 28, 30), 'Tortureweb Dryder': ('Bosses', 'Dryders', 'Elementalist', 28, 30), 'Margonite High Priest': ('Foes', 'Demons (Margonites)', 'Monk', 28, 30), 'Margonite Patriarch': ('Foes', 'Demons (Margonites)', 'Paragon', 28, 30), 'Portal Wraith': ('Foes', 'Phantoms (Undead)', 'Elementalist', 24, 26), "Shiro'ken Warrior": ('Foes', "Shiro'ken", 'Warrior', 28, 30), "Shiro'ken Ranger": ('Foes', "Shiro'ken", 'Ranger', 28, 30), "Shiro'ken Monk": ('Foes', "Shiro'ken", 'Monk', 28, 30), "Shiro'ken Mesmer": ('Foes', "Shiro'ken", 'Mesmer', 28, 30), "Shiro'ken Necromancer": ('Foes', "Shiro'ken", 'Necromancer', 28, 30), "Shiro'ken Elementalist": ('Foes', "Shiro'ken", 'Elementalist', 28, 30), "Shiro'ken Ritualist": ('Foes', "Shiro'ken", 'Ritualist', 28, 30), "Shiro'ken Assassin": ('Foes', "Shiro'ken", 'Assassin', 28, 30), 'Armageddon Lord': ('Foes', 'Titans (arranged in spawning pattern order)', 'Elementalist', 28, 30), 'Risen Ashen Hulk1, ': ('Foes', 'Titans (arranged in spawning pattern order)', 'Necromancer', 28, 30), 'Hand of the Titans1, ': ('Foes', 'Titans (arranged in spawning pattern order)', 'Warrior', 28, 30), 'Fist of the Titans1, ': ('Foes', 'Titans (arranged in spawning pattern order)', 'Warrior', 28, 30), 'Titan Abomination': ('Foes', 'Titans (arranged in spawning pattern order)', 'Warrior', 28, 30), 'Pain Titan': ('Foes', 'Titans (arranged in spawning pattern order)', 'Elementalist', 28, 30), 'Madness Titan': ('Foes', 'Titans (arranged in spawning pattern order)', 'Dervish', 28, 30), 'Champion Puran': ('Bosses', 'Demons (Margonites)', 'Warrior', 28, 30), 'Curator Kali': ('Bosses', 'Demons (Margonites)', 'Elementalist', 28, 30), 'Shiro Tagachi': ('Bosses', 'Envoy', 'Assassin', 31, 33), 'Undead Lich': ('Bosses', 'Lich (Undead)', 'Necromancer', 30, 32), 'Abaddon': ('Foes', 'God (Torment creature)', 'Elementalist', 30, 32), 'Graven Monolith': ('Foes', 'Monoliths', 'MesmerParagonDervish', 22, 26)}

CAMPAIGN = "C"
TYPE = "T"
SECONDARY_TYPE="S"
LEVEL = "L"
HARD_MODE_LEVEL="H"

ALLY = "A"
ENEMY = "E"
BOSS = "B"

def DrawMonster():
    print("Here you can draw random GW1 NPCs")
    print("""I have not personally entered all of their builds into this app, but you will be given their name and the wiki page,
so it should be quite simple to look them up and then create the skill template using this tool.""")
    Input = ""
    while Input not in ("Y", "N"):
        print("Enable Bosses ('Yes'/'Y' Or 'No'/'N')?")
        Input = input()
    if Input in ("Yes", "Y"):
        Bosses = True
    elif Input in ("No", "N"):
        Bosses = False
    else:
        raise Exception("!!!")

    Input = ""
    while Input not in ("Y", "N"):
        print("Enable Allies ('Yes'/'Y' Or 'No'/'N')?")
        Input = input()
    if Input in ("Yes", "Y"):
        Allies = True
    elif Input in ("No", "N"):
        Allies = False
    else:
        raise Exception("!!!")
    
    Input = ""
    while Input not in ("Prophecies", "P", "Factions", "F", "Nightfall", "N", "All", "A"):
        print("Which Campaign? ('Prophecies'/'P', 'Factions'/'F', 'Nightfall'/'N' Or 'All'/'A')")
        Input = input()
    if Input in ("Prophecies", "P"):
        Campaign = PROPHECIES
    elif Input in ("Factions", "F"):
        Campaign = FACTIONS
    elif Input in ("Nightfall", "N"):
        Campaign = NIGHTFALL
    elif Input in ("All", "A"):
        Campaign = ALL
    else:
        raise Exception("!!!")
    while True:
        print("Enter 'Draw'/'D' to Draw, Enter 'Back'/'B' to go back:")
        Input = input()
        if Input in ("Draw", "D"):
            if Campaign==ALL:
                TempCampaign = choice((PROPHECIES, FACTIONS, NIGHTFALL))
            else:
                TempCampaign = Campaign
            Choice = None
            while Choice is None or (TempCampaign not in StoredNPCs[Choice][CAMPAIGN]) or (
                not Bosses and StoredNPCs[Choice][TYPE]==BOSS) or (not Allies and StoredNPCs[Choice][TYPE]==ALLY):
                Choice = choice(list(StoredNPCs.keys()))
            print(Choice)
            print("Wiki Page: https://wiki.guildwars.com/wiki/"+Choice+"    (May rarely be incorrect)")
        elif Input in ("Back", "B"):
            return

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
    if len(Data[ATTRIBUTES]) == 0:
        BitsPerAttribute = 4
    else:
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

def AddNPCs(Data):
    #Method call Add() and push changes to temporary NPCs to format of StoredNPCs and print
    #Quite ugly code - case by case
    print("CTRL+D to confirm")
    while True:
        NewData=[]
        while True:
            try:
                NewData.append(input())
            except EOFError:
                break
        if NewData[0] in (PROPHECIES, FACTIONS, NIGHTFALL):
            Campaign = NewData[0]
            print("Pushing NPCs data to StoredNPCs...")
            for Name in NPCs:
                if Name in StoredNPCs.keys():
                    if StoredNPCs[Name][CAMPAIGN] != Campaign:
                        StoredNPCs[Name][CAMPAIGN]+=Campaign
                else:
                    Type, SecondaryType, Profession, Level, HardModeLevel = NPCs[Name]
                    PrimaryProfession = 0
                    SecondaryProfession = 0
                    if Profession in ProfessionDict.keys():
                        PrimaryProfession = ProfessionDict[Profession]
                    else:
                        for Each in ProfessionDict.keys():
                            if Profession.startswith(Each):
                                PrimaryProfession = ProfessionDict[Each]
                            elif Profession.endswith(Each):
                                SecondaryProfession = ProfessionDict[Each]
                    if Type=="Allies":
                        Type = ALLY
                    elif Type=="Foes":
                        Type = ENEMY
                    elif Type=="Bosses":
                        Type = BOSS
                    else:
                        raise Exception("Unknown Type" + Type)
                    StoredNPCs[Name] = {CAMPAIGN: Campaign, TYPE: Type, SECONDARY_TYPE: SecondaryType, PRIMARY: PrimaryProfession, SECONDARY: SecondaryProfession, LEVEL: Level,
                                        HARD_MODE_LEVEL: HardModeLevel}
            print(StoredNPCs)
            return
        Data = Add(NewData, Data)
        print(Data)

def Add(NewData, Data):
    #Method used to add NPCs to the NPC list - following format of mission wiki pages
    #Quite ugly code - case by case
    Type=""
    SecondaryType=""
    for Line in NewData:
        if "→" in Line:
                    Line = Line[0:Line.find("→")-1]
        if Line=="Allies" or Line == "Foes" or Line=="Bosses":
            Type = Line
        elif not Line == "":
            Split = Line.split(" ")
            MultiProfession = False
            for Each in DualProfessions:
                if Each in Split[0]:
                    MultiProfession = True
            if Split[0] in ProfessionDict.keys() or MultiProfession:
                if "(" in Line:
                    Name = Line[Line.rfind(")")+2::]
                    #Names ending in brackets will be empty strings
                    if Name!="": 
                        if Name[-1].isdigit():
                            Name = Name[0:-1]
                        if Name not in Data.keys():
                            Class = Split[0]
                            i=1
                            while True:
                                Level = Split[i]
                                if "," not in Split[i] and "," not in Split[i+1]:
                                    break
                                elif "(" in Split[i+1]:
                                    i+=1
                                i+=1
                            i+=1
                            Level = int(Level)
                            HardModeLevel = int(Split[i][1:-1])
                            Data[Name] = (Type, SecondaryType, Class, Level, HardModeLevel)
                else:
                    Index = len(Split[0])+1
                    Class = Split[0]
                    i=1
                    while True:
                        Index+=len(Split[i])+1
                        Level = Split[i]
                        if "," not in Split[i] and "," not in Split[i+1]:
                            break
                        i+=1
                    Level = int(Level)
                    HardModeLevel = Level
                    Name = Line[Index::]
                    #Names ending in brackets will be empty strings
                    if Name!="": 
                        if Name[-1].isdigit():
                            Name = Name[0:-1]
                        if not Name in Data.keys():
                            Data[Name] = (Type, SecondaryType, Class, Level, HardModeLevel)
            elif Split[0] != "Unknown":
                SecondaryType=Line
    return Data

while True:
    print("Read Skill Template ('Read'/'R'), Create New ('New'/'N'), Draw Monster ('Draw'/'D') Or Exit ('Exit'/'E')?")
    Type = input()
    if Type == "Read" or Type == "R":
        print("Enter Build Template String:")
        print(ReadBuild(input()))
    elif Type == "New" or Type == "N":
        print(WriteBuild())
    elif Type == "Draw" or Type == "D":
        DrawMonster()
    elif Type == "Exit" or Type == "E":
        break
    elif Type == "H" or Type == "Hax":
        # For adding NPCs from GW1 missions
        AddNPCs(NPCs)
