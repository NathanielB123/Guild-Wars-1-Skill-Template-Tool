from random import choice
from Data import ProfessionDict, ProfessionDict, DualProfessions, Base64Dict, AttributeDict, SkillDict, StoredNPCs
import webbrowser

PRIMARY="Pr"
SECONDARY="Se"
ATTRIBUTES="At"
SKILLS = "Sk"

PROPHECIES = "P"
FACTIONS = "F"
NIGHTFALL = "N"
EOTN = "E"
ALL = "Al"

NPCs = {'Jora': ('Allies', 'Norn', 'Warrior', 20, 20), 'Sif Shadowhunter': ('Allies', 'Norn', 'Ranger', 20, 20), 'Arctic Wolf': ('Foes', 'Beasts', 'Warrior', 20, 26), 'Stonewolf': ('Foes', 'Beasts', 'Warrior', 20, 26), 'Jotun Skullsmasher': ('Foes', 'Giants', 'Warrior', 28, 30), 'Jotun Bloodcurdler': ('Foes', 'Giants', 'Necromancer', 28, 30), 'Jotun Bladeturner': ('Foes', 'Giants', 'Mesmer', 28, 30), 'Jotun Mindbreaker': ('Foes', 'Giants', 'Mesmer', 28, 30), 'Mandragor Scavenger': ('Foes', 'Mandragors', 'Ranger', 20, 26), 'Ulcerous Mandragor': ('Foes', 'Mandragors', 'Necromancer', 20, 26), 'Dreamroot Mandragor': ('Foes', 'Mandragors', 'Mesmer', 20, 26), 'Mystic Mandragor': ('Foes', 'Mandragors', 'Dervish', 20, 26), 'Olaf Olafson': ('Allies', 'Norn', 'Warrior', 20, 20), 'Bear Spirit': ('Allies', '', 'Mesmer', 20, 26), 'Egil Fireteller': ('Allies', '', 'Paragon', 20, 20), 'Charr Axemaster': ('Foes', 'Charr', 'WarriorElementalist', 20, 26), 'Charr Blademaster': ('Foes', 'Charr', 'WarriorElementalist', 20, 26), 'Charr Bladestorm': ('Foes', 'Charr', 'WarriorElementalist', 20, 26), 'Charr Seeker': ('Foes', 'Charr', 'RangerElementalist', 20, 26), 'Charr Prophet': ('Foes', 'Charr', 'MonkMesmer', 20, 26), 'Charr Mender': ('Foes', 'Charr', 'MonkParagon', 20, 26), 'Charr Hexreaper': ('Foes', 'Charr', 'NecromancerRitualist', 20, 26), 'Charr Dominator': ('Foes', 'Charr', 'MesmerMonk', 20, 26), 'Charr Wardkeeper': ('Foes', 'Charr', 'Elementalist', 20, 26), 'Charr Flameshielder': ('Foes', 'Charr', 'ElementalistMonk', 20, 26), 'Charr Avenger': ('Foes', 'Charr', 'Ritualist', 20, 26), 'Frozen Elemental': ('Foes', 'Elementals', 'Elementalist', 24, 26), 'Avalanche': ('Foes', 'Elementals', 'Elementalist', 28, 30), 'Tenagg Flametroller': ('Bosses', 'Charr', 'Warrior', 24, 30), 'Docu Kindleshot': ('Bosses', 'Charr', 'Ranger', 24, 30), 'Elmohr Snowmender': ('Bosses', 'Charr', 'Monk', 24, 30), 'Kakei Stormcaller': ('Bosses', 'Charr', 'Elementalist', 24, 30), 'Charr Firereigner': ('Foes', 'Charr', 'ElementalistMonk', 20, 26), 'Mandragor Dust Devil': ('Foes', 'Mandragor', 'Ranger', 24, 26), 'Mandragor Smoke Devil': ('Foes', 'Mandragor', 'Ranger', 24, 26), 'Vile Mandragor': ('Foes', 'Mandragor', 'Necromancer', 24, 26), 'Mandragor Shadowfang': ('Foes', 'Mandragor', 'Assassin', 24, 26), 'Mantid Queen': ('Foes', 'Mantis', 'Monk', 20, 26), 'Mantid Nymph': ('Foes', 'Mantis', 'Mesmer', 20, 26), 'Mantid Digger': ('Foes', 'Mantis', 'Dervish', 20, 26), 'Swampwater Skale': ('Foes', 'Skale', 'Elementalist', 24, 26), 'Deadly Skale': ('Foes', 'Skale', 'Assassin', 24, 26), 'Skale Lasher': ('Foes', 'Skale', 'Dervish', 24, 26), 'Gordam Griefgiver': ('Bosses', 'Charr', 'Warrior', 24, 30), 'Groknar Weazlewortz': ('Bosses', 'Charr', 'Ranger', 24, 30), 'Harvest Soulreign': ('Bosses', 'Charr', 'Necromancer', 24, 30), 'Anmat the Trickster': ('Bosses', 'Charr', 'Mesmer', 24, 30), 'Frazar Frostfur': ('Bosses', 'Charr', 'Elementalist', 24, 30), 'Needling Lavastrider': ('Foes', 'Arachnids (level 2)', 'Ranger', 20, 24), 'Spider': ('Foes', 'Arachnids (level 2)', 'Ranger', 14, 24), 'Venomweaver': ('Foes', 'Arachnids (level 2)', 'Ranger', 24, 26), 'Bloodweaver': ('Foes', 'Arachnids (level 2)', 'Paragon', 24, 26), 'Jadam Spearspinner': ('Bosses', 'Arachnids', 'Paragon', 28, 30), 'Charr Prison Guard': ('Bosses', 'Charr', 'Warrior', 24, 30), 'Flamemaster Maultooth': ('Bosses', 'Charr', 'Elementalist', 28, 30), 'Bonwor Fierceblade': ('Allies', 'Charr', 'Warrior', 20, 20), 'Roan Fierceheart': ('Allies', 'Charr', 'MonkMesmer', 20, 20), 'Cowl Fiercetongue': ('Allies', 'Charr', 'ElementalistMonk', 20, 20), 'Gron Fierceclaw': ('Allies', 'Charr', 'Assassin', 20, 20), 'Seer Fiercereign': ('Allies', 'Charr', 'Ritualist', 20, 20), 'Armored Saurus': ('Allies', 'Dinosaurs', 'Elementalist', 28, 28), 'Elite Charr Guard': ('Foes', 'Charr', 'WarriorElementalist', 20, 26), 'Destroyer of Bones': ('Foes', 'Destroyers', 'Warrior', 28, 30), 'Destroyer of Sinew': ('Foes', 'Destroyers', 'Warrior', 24, 26), 'Destroyer of Deeds': ('Foes', 'Destroyers', 'Ranger', 24, 26), 'Destroyer of Hordes': ('Foes', 'Destroyers', 'Ranger', 28, 30), 'Destroyer of Hope': ('Foes', 'Destroyers', 'Necromancer', 28, 30), 'Destroyer of Thoughts': ('Foes', 'Destroyers', 'Mesmer', 28, 30), 'Hierophant Burntsoul': ('Bosses', 'Charr', 'ElementalistMonk', 24, 30)}
CAMPAIGN = "C"
TYPE = "T"
SECONDARY_TYPE="S"
LEVEL = "L"
HARD_MODE_LEVEL="H"

ALLY = "A"
ENEMY = "E"
BOSS = "B"

def DrawMonster():
    print("Here you can draw random GW1 NPCs.")
    print("""I have not personally entered all of their builds into this app, but you will be given their name, the wiki page and some basic info,
so it should be quite simple to look them up and then create the skill template using this tool.""")
    Input = ""
    while Input not in ("Ally", "A", "Foe", "F", "Boss", "B", "All"):
        print("What Type? ('Ally'/'A', 'Foe'/'F', 'Boss'/'B', Or 'All')")
        Input = input()
    if Input in ("Ally", "A"):
        Type = ALLY
    elif Input in ("Foe", "F"):
        Type = ENEMY
    elif Input in ("Boss", "B"):
        Type = BOSS
    elif Input in ("All"):
        Type = ALL
    else:
        raise Exception("!!!")
    
    Input = ""
    while Input not in ("Prophecies", "P", "Factions", "F", "Nightfall", "N", "EOTN", "E", "All", "A"):
        print("Which Campaign? ('Prophecies'/'P', 'Factions'/'F', 'Nightfall'/'N', 'EOTN'/'N' Or 'All/'A'')")
        Input = input()
    if Input in ("Prophecies", "P"):
        Campaign = PROPHECIES
    elif Input in ("Factions", "F"):
        Campaign = FACTIONS
    elif Input in ("Nightfall", "N"):
        Campaign = NIGHTFALL
    elif Input in ("EOTN", "E"):
        Campaign = EOTN
    elif Input in ("All", "A"):
        Campaign = ALL
    else:
        raise Exception("!!!")
    
    while True:
        print("Enter 'Draw'/'D' to Draw, Enter 'Back'/'B' to go back:")
        Input = input()
        if Input in ("Draw", "D"):
            if Campaign==ALL:
                TempCampaign = choice((PROPHECIES, FACTIONS, NIGHTFALL, EOTN))
            else:
                TempCampaign = Campaign
            Choice = None
            while Choice is None or (TempCampaign not in StoredNPCs[Choice][CAMPAIGN]) or not (Type==ALL or StoredNPCs[Choice][TYPE]==Type):
                Choice = choice(list(StoredNPCs.keys()))
            print(Choice)
            print("Primary Profession: "+ProfessionDict.inv[StoredNPCs[Choice][PRIMARY]]+
            "\nSecondary Profession: "+ProfessionDict.inv[StoredNPCs[Choice][SECONDARY]])
            print("Level: "+str(StoredNPCs[Choice][LEVEL])+" ("+str(StoredNPCs[Choice][HARD_MODE_LEVEL])+")")
            print("Type: "+("Foe" if  StoredNPCs[Choice][TYPE]==ENEMY else "Boss" if  StoredNPCs[Choice][TYPE]==BOSS else "Ally")) #+ " - "+StoredNPCs[Choice][SECONDARY_TYPE]) Secondary types are not always useful (often relate to mechanics rather than affliction) so I have commented it out for now
            print("Campaign(s): "+("Prophecies " if PROPHECIES in StoredNPCs[Choice][CAMPAIGN] else "") +
                  ("Factions " if FACTIONS in StoredNPCs[Choice][CAMPAIGN] else "") +
                  ("Nightfall " if NIGHTFALL in StoredNPCs[Choice][CAMPAIGN] else "") +
                  ("EOTN " if EOTN in StoredNPCs[Choice][CAMPAIGN] else ""))
            print("Wiki Page: https://wiki.guildwars.com/wiki/"+Choice.replace(" ", "_"))
            print("")
            webbrowser.open("https://wiki.guildwars.com/wiki/"+Choice.replace(" ", "_"))
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
        if NewData[0] in (PROPHECIES, FACTIONS, NIGHTFALL, EOTN):
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
