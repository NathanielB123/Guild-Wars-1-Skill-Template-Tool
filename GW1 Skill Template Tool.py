from random import choice
from Data import ProfessionDict, ProfessionDict, Base64Dict, AttributeDict, SkillDict, StoredNPCs, Campaigns, Affiliations, Types, Explorables, Outposts, Missions, Regions, Dungeons, Arenas
import webbrowser
import json
from urllib.request import urlopen
from bs4 import BeautifulSoup

PRIMARY="Primary"
SECONDARY="Secondary"
ATTRIBUTES="Attributes"
SKILLS = "Skills"

NPCs = {}
PROFESSIONS="Professions"
CAMPAIGNS = "Campaigns"
CATEGORY = "Category"
STANDARD, HENCHMAN, BOSS = "Standard", "Henchman", "Boss"
TYPE = "Type"
AFFILIATIONS = "Affiliations"
REGIONS = "Regions"
AREAS = "Areas"

ALL = "All"

def DrawMonster():
    print("Here you can draw random GW1 NPCs.")
    print("Please note that a lot of features here are very much WIP")
    
    Input = ""
    FirstLetters = list(map(lambda each: each[0], Campaigns))
    while Input not in Campaigns + FirstLetters + ["All", "A"]:
        print("Which Campaign? ("+", ".join(list(["'"+Campaigns[Num]+"'/'"+FirstLetters[Num]+"'" for Num in range(0,len(Campaigns))]))+" or 'All/'A'')")
        Input = input()
    if Input in Campaigns:
        Campaign = Input
    elif Input in FirstLetters:
        Campaign = Campaigns[FirstLetters.index(Input)]
    elif Input in ("All", "A"):
        Campaign = ALL
    else:
        raise Exception("!!!")
    while True:
        print("Enter 'Draw'/'D' to Draw, Enter 'Back'/'B' to go back:")
        Input = input()
        if Input in ("Draw", "D"):
            if Campaign==ALL:
                ChosenCampaign = choice(Campaigns)
            else:
                ChosenCampaign = Campaign
            Choice = None
            while Choice is None or (ChosenCampaign not in StoredNPCs[Choice][CAMPAIGNS]):
                Choice = choice(list(StoredNPCs.keys()))
            print(Choice)
            print("Primary Profession: "+ProfessionDict.inv[StoredNPCs[Choice][PROFESSIONS][0]])
            if len(StoredNPCs[Choice][PROFESSIONS]) > 1:
                print("Secondary Profession: "+ProfessionDict.inv[StoredNPCs[Choice][PROFESSIONS][1]])
            print("Skills: "+", ".join(list(map(lambda each: SkillDict.inv[each], StoredNPCs[Choice][SKILLS]))))
            print("Campaign(s): "+", ".join(StoredNPCs[Choice][CAMPAIGNS]))
            print("Category: "+StoredNPCs[Choice][CATEGORY])
            print("Type: "+StoredNPCs[Choice][TYPE])
            print("Affiliation(s): "+", ".join(StoredNPCs[Choice][AFFILIATIONS]))
            print("Regions: "+", ".join(StoredNPCs[Choice][REGIONS]))
            print("Areas: "+", ".join(StoredNPCs[Choice][AREAS]))
            print("Wiki Page: https://wiki.guildwars.com/wiki/"+Choice.replace(" ", "_"))
            print("Build Code: "+BitsToBase64(DataToBits({PRIMARY: StoredNPCs[Choice][PROFESSIONS][0],
            SECONDARY: (StoredNPCs[Choice][PROFESSIONS][1] if len(StoredNPCs[Choice][PROFESSIONS])>1 else 0),
            ATTRIBUTES: dict(),
            SKILLS: StoredNPCs[Choice][SKILLS]+list([0 for _ in range(0,8-len(StoredNPCs[Choice][SKILLS]))])})))
            print("")
            #open wiki
            #webbrowser.open("https://wiki.guildwars.com/wiki/"+Choice.replace(" ", "_"))
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

def ScrapeEVERYNPC():
    # Depreciated
    url = ("https://wiki.guildwars.com/api.php?action=query&format=json&prop=&list=&meta=&continue=gcmcontinue%7C%7C&generator=categorymembers&gcmtitle=Category%3A"+
           "Warrior"+"s&gcmlimit=max")
    #Remember + bosses and +henchmen
    page = urlopen(url)
    html = page.read().decode("utf-8")
    JSON = json.loads(html)
    for key in JSON["query"]["pages"]:
        print(JSON["query"]["pages"][key]["title"])
        #then check if has skills
    while "continue" in JSON.keys():
        print("Cont...")
        url = ("https://wiki.guildwars.com/api.php?action=query&format=json&prop=&list=&meta=&continue=gcmcontinue%7C%7C&generator=categorymembers&gcmtitle=Category%3A"+
               "Warrior"+"s&gcmcontinue="+JSON["continue"]["gcmcontinue"]+"&gcmlimit=max")
        page = urlopen(url)
        html = page.read().decode("utf-8")
        JSON = json.loads(html)
        for key in JSON["query"]["pages"]:
            print(JSON["query"]["pages"][key]["title"])



    #Works so - here is plan:
    # Could add skill descriptions and pictures - not sure where to get descriptions from, pictures can be attempted to be gotten by going to the actual page and searching html string for png or jpg
    # https://wiki.guildwars.com/wiki/Zilo_the_Drunkard - decode to string like usual and then search for .jpg and go right until '[stuff]src="[image path and name here]"[more stuff]'
    # Skill icons can be found with same method
    # Skill tooltips are unnecessary IMO
    # In order to prevent >1 elite - maybe go to skill page and get if elite link is present
    # Also remember Category:NPCs_with_multiple_professions -> bosses with multiple professions

def GetIfSkillIsElite(SkillName):
    url = ("https://wiki.guildwars.com/api.php?action=parse&format=json&page="+SkillName+"&prop=categories").replace(" ", "_")
    page = urlopen(url)
    html = page.read().decode("utf-8")
    JSON = json.loads(html)
    for Category in JSON["parse"]["categories"]:
        if Category["*"] == "Elite_skills":
            return True
    return False

def GetNPCImage(Name):
    pass

def GetSkillImage(SkillName):
    pass

def GetNPCs():
    #NPC structure is - Name: {Professions, Skills, Campaigns, (Standard-0, Henchman-1 or Boss-2), Type, Affiliations, Regions, Areas (explorables, dungeons, missions)}
    StandardNames = set(GetPages(["Assassins"], ExpandSubCategories = False)[1::] + GetPages(["Dervishes"], ExpandSubCategories = False)[1::] + 
                GetPages(["Elementalists"], ExpandSubCategories = False)[1::] + GetPages(["Mesmers"], ExpandSubCategories = False)[1::] + 
                GetPages(["Monks"], ExpandSubCategories = False)[1::] + GetPages(["Necromancers"], ExpandSubCategories = False)[1::] +
                GetPages(["Paragons"], ExpandSubCategories = False)[1::] + GetPages(["Rangers"], ExpandSubCategories = False)[1::] +
                GetPages(["Ritualists"], ExpandSubCategories = False)[1::] + GetPages(["Warriors"], ExpandSubCategories = False)[1::])
    
    HenchmanNames = set(GetPages(["Assassin_henchmen"], ExpandSubCategories = False) + GetPages(["Dervish_henchmen"], ExpandSubCategories = False) + 
                GetPages(["Elementalist_henchmen"], ExpandSubCategories = False) + GetPages(["Mesmer_henchmen"], ExpandSubCategories = False) + 
                GetPages(["Monk_henchmen"], ExpandSubCategories = False) + GetPages(["Necromancer_henchmen"], ExpandSubCategories = False) +
                GetPages(["Paragon_henchmen"], ExpandSubCategories = False) + GetPages(["Ranger_henchmen"], ExpandSubCategories = False) +
                GetPages(["Ritualist_henchmen"], ExpandSubCategories = False) + GetPages(["Warrior_henchmen"], ExpandSubCategories = False))
    
    BossNames = set(GetPages(["Assassin_bosses"], ExpandSubCategories = False)[1::] + GetPages(["Dervish_bosses"], ExpandSubCategories = False)[1::] + 
                GetPages(["Elementalist_bosses"], ExpandSubCategories = False)[1::] + GetPages(["Mesmer_bosses"], ExpandSubCategories = False)[1::] + 
                GetPages(["Monk_bosses"], ExpandSubCategories = False)[1::] + GetPages(["Necromancer_bosses"], ExpandSubCategories = False)[1::] +
                GetPages(["Paragon_bosses"], ExpandSubCategories = False)[1::] + GetPages(["Ranger_bosses"], ExpandSubCategories = False)[1::] +
                GetPages(["Ritualist_bosses"], ExpandSubCategories = False)[1::] + GetPages(["Warrior_bosses"], ExpandSubCategories = False)[1::])
    NewHenchmanNames = set()
    for each in HenchmanNames:
        if not each[-8::]=="Henchman":
            NewHenchmanNames.add(each)
    HenchmanNames = NewHenchmanNames

    NewBossNames = set()
    for each in BossNames:
        if not each in HenchmanNames:
            NewBossNames.add(each)
    BossNames = NewBossNames

        
    NewStandardNames = set()
    for Name in StandardNames:
        if not (Name in HenchmanNames or Name in BossNames):
            NewStandardNames.add(Name)
    StandardNames = NewStandardNames
    print(len(StandardNames) + len(HenchmanNames) + len(BossNames))
    Heroes = 0
    for Category in STANDARD, BOSS, HENCHMAN:
        if Category == STANDARD:
            NPCNames = StandardNames
        elif Category == BOSS:
            NPCNames = BossNames
        elif Category == HENCHMAN:
            NPCNames = HenchmanNames
        for Name in NPCNames:
            print(Name)
            NPCs[Name] = {PROFESSIONS : [], SKILLS : [], CAMPAIGNS : [], CATEGORY : Category, TYPE : None, AFFILIATIONS : [], REGIONS : [], AREAS : []}
            Data, Skills, Locations = FetchNPCData(Name)
            for Each in Data:
                if Each in ProfessionDict.keys() and ProfessionDict[Each] not in NPCs[Name][PROFESSIONS] and len(NPCs[Name][PROFESSIONS])<2:
                    NPCs[Name][PROFESSIONS].append(ProfessionDict[Each])
                elif Each in Campaigns and Each not in NPCs[Name][CAMPAIGNS]:
                    NPCs[Name][CAMPAIGNS].append(Each)
                elif Each in Types and NPCs[Name][TYPE] is None:
                    NPCs[Name][TYPE] = Each
                elif Each in Affiliations and Each not in NPCs[Name][AFFILIATIONS]:
                    NPCs[Name][AFFILIATIONS].append(Each)
                elif Each == "Hero":
                    print("HERO!!")
                    Heroes+=1
                    NPCs.pop(Name)
                    break
            else:
                for Skill in Skills:
                    if not Skill[-5::] == "(PvP)" and SkillDict[Skill] not in NPCs[Name][SKILLS]:
                        NPCs[Name][SKILLS].append(SkillDict[Skill])
                for Location in Locations:
                    if Location in Regions and Location not in NPCs[Name][REGIONS]:
                        NPCs[Name][REGIONS].append(Location)
                    elif Location in Explorables+Outposts+Missions+Dungeons+Arenas and Location not in NPCs[Name][AREAS]:
                        NPCs[Name][AREAS].append(Location)
                print(NPCs[Name])
                print(str(len(NPCs))+"/"+str(len(StandardNames) + len(HenchmanNames) + len(BossNames)) + "-"+str(Heroes))
    return NPCs

def GetLinks(Page):
    url = ("https://wiki.guildwars.com/api.php?action=parse&format=json&page="+Page+"&prop=links").replace(" ", "_")
    page = urlopen(url)
    html = page.read().decode("utf-8")
    JSON = json.loads(html)
    Links = []
    for Link in JSON["parse"]["links"]:
        Links.append(Link["*"])
    return Links

def FetchNPCData(Name):    
    url = ("https://wiki.guildwars.com/api.php?action=parse&format=json&page="+Name+"&prop=text").replace(" ", "_")
    page = urlopen(url)
    html = page.read().decode("utf-8")
    JSON = json.loads(html)
    soup = BeautifulSoup(JSON["parse"]["text"]["*"], "html.parser")
    UsefulData = []
    Locations = []
    #for table in soup.find_all("tbody"):
    table1 = soup.find_all("tbody")[0]
    for each in table1.find_all("a"):
        UsefulData.append(each.get_text())
    for each in ProfessionDict.keys():
        if each in UsefulData:
            break
    else:
        table2 = soup.find_all("tbody")[1]
        for each in table2.find_all("a"):
            UsefulData.append(each.get_text())
    if soup.find(id="Locations") is not None:
        for each in soup.find(id="Locations").parent.next_sibling.next_sibling.find_all("a"):
            Locations.append(each.get("title"))
    if soup.find(id="Location") is not None:
        for each in soup.find(id="Location").parent.next_sibling.next_sibling.find_all("a"):
            Locations.append(each.get("title"))
    if soup.find(id="Missions") is not None:
        for each in soup.find(id="Missions").parent.next_sibling.next_sibling.find_all("a"):
            Locations.append(each.get("title"))

    for each in Locations:
        if each in Regions + Explorables+Outposts+Missions+Dungeons+Arenas:
            break
    else:
        #Sometimes contents is in the way
        if soup.find(id="Locations") is not None:
            for each in soup.find(id="Locations").parent.next_sibling.next_sibling.next_sibling.next_sibling.find_all("a"):
                Locations.append(each.get("title"))
        if soup.find(id="Location") is not None:
            for each in soup.find(id="Location").parent.next_sibling.next_sibling.next_sibling.next_sibling.find_all("a"):
                Locations.append(each.get("title"))
        if soup.find(id="Missions") is not None:
            for each in soup.find(id="Missions").parent.next_sibling.next_sibling.next_sibling.next_sibling.find_all("a"):
                Locations.append(each.get("title"))
    
    Skills = []
    if soup.find(id="Skills") is not None:
        for each in soup.find(id="Skills").parent.next_sibling.next_sibling.find_all("a"):
            if each.get("title") in SkillDict.keys():
                Skills.append(each.get("title"))
        if len(Skills) == 0:
            try:
                #If enemy has multiple variations, use first variation
                for each in soup.find(id="Skills").parent.next_sibling.next_sibling.next_sibling.next_sibling.find_all("a"):
                    if each.get("title") in SkillDict.keys():
                        Skills.append(each.get("title"))
                if len(Skills) == 0:
                    #If that variation gives a stat
                    try:
                        for each in soup.find(id="Skills").parent.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.find_all("a"):
                            if each.get("title") in SkillDict.keys():
                                Skills.append(each.get("title"))
                    except:
                        for each in soup.find(id="Skills").parent.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.find_all("a"):
                            if each.get("title") in SkillDict.keys():
                                Skills.append(each.get("title"))
            except:
                pass
    return UsefulData, Skills, Locations

def GetExplorables():
    return GetPages(["Explorable_areas"])[1::]

def GetRegions():
    return GetPages(["Regions"])[1::]

def GetDungeons():
    return GetPages(["Dungeons"], ExpandSubCategories=False)[1::]

def GetMissions():
    #Note that core missions are missing - from what I understand, these are mostly pvp focussed but I have not checked fully
    return (GetPages(["Challenge_missions"])[1::] + GetPages(["Competitive_missions"])[1::] + GetPages(["Cooperative_missions"])[1::] +
            GetPages(["Dragon_Festival_missions"]) + GetPages(["Elite_missions"])[1::] + GetPages(["Halloween_missions"]) +
            GetPages(["Mini_missions"])[1::])

def GetOutposts():
    Temp = GetPages(["Outposts"])[2::]
    print(Temp)
    Temp.remove("Arena outpost")
    return Temp

def GetArenas():
    return GetPages(["Arenas"],  ExpandSubCategories=False)[5::] + GetPages(["Arena_outposts"],  ExpandSubCategories=False)[1::]

def GetAffiliations():
    return GetPages(["NPCs_by_affiliation"],  ExpandSubCategories=False, IncludeCategories=True)[1::]

def GetPages(Categories, ExpandSubCategories=True, IncludeCategories=False):
    Data = []
    while len(Categories)>0:
        JSON = None
        while JSON is None or "continue" in JSON.keys():
            if JSON is None:
                url = ("https://wiki.guildwars.com/api.php?action=query&format=json&prop=&list=&meta=&continue=gcmcontinue%7C%7C&generator=categorymembers&gcmtitle=Category%3A"+
                       Categories[0]+"&gcmlimit=max").replace(" ", "_")
            else:
                url = ("https://wiki.guildwars.com/api.php?action=query&format=json&prop=&list=&meta=&continue=gcmcontinue%7C%7C&generator=categorymembers&gcmtitle=Category%3A"+
                       Categories[0]+"&gcmcontinue="+JSON["continue"]["gcmcontinue"]+"&gcmlimit=max").replace(" ", "_")
            page = urlopen(url)
            html = page.read().decode("utf-8")
            JSON = json.loads(html)
            for key in JSON["query"]["pages"]:
                if not ".jpg" == JSON["query"]["pages"][key]["title"][-4::]:
                    # Do not include media files
                    if not "Category:" == JSON["query"]["pages"][key]["title"][0:9]:
                        Data.append(JSON["query"]["pages"][key]["title"])
                    else:
                        if ExpandSubCategories:
                            # New category to check
                            Categories.append(JSON["query"]["pages"][key]["title"][9::])
                        if IncludeCategories:
                            Data.append(JSON["query"]["pages"][key]["title"][9::])
        Categories.pop(0)
    return Data

def GetSkillImg(Name):
	url = ("https://wiki.guildwars.com/api.php?action=parse&format=json&page="+Name+"&prop=text").replace(" ", "_")
	page = urlopen(url)
	html = page.read().decode("utf-8")
	JSON = json.loads(html)
	soup = BeautifulSoup(JSON["parse"]["text"]["*"], "html.parser")
	for each in soup.find_all("div"):
		if each.get("class") == ["skill-image"]:
			image = each
			break
	else:
		raise Exception("No skill image!")
	# I have not found a way to get the original, high quality image directly through the wiki API, so instead I am just directly parsing the html of the file page
	new_url = "https://wiki.guildwars.com"+image.find("a").get("href")
	page = urlopen(new_url)
	html = page.read().decode("utf-8")
	soup = BeautifulSoup(html, "html.parser")
	for each in soup.find_all("a"):
		if each.get("href") is not None and each.get("href")[0:8] == "/images/":
			return "https://wiki.guildwars.com"+each.get("href")

def GetNPCImg(Name):
	url = ("https://wiki.guildwars.com/api.php?action=parse&format=json&page="+Name+"&prop=text").replace(" ", "_")
	page = urlopen(url)
	html = page.read().decode("utf-8")
	JSON = json.loads(html)
	soup = BeautifulSoup(JSON["parse"]["text"]["*"], "html.parser")
	table = soup.find_all("tbody")[0]
	for each in table.find_all("a"):
		if each.get_text() in ProfessionDict.keys():
			break
	else:
		for table in soup.find_all("tbody"):
			for each in table.find_all("a"):
				if each.get_text() in ProfessionDict.keys():
					break
		else:
			raise Exception("NPC has no stats table")
	# I have not found a way to get the original, high quality image directly through the wiki API, so instead I am just directly parsing the html of the file page
	new_url = "https://wiki.guildwars.com"+table.find("a").get("href")
	page = urlopen(new_url)
	html = page.read().decode("utf-8")
	soup = BeautifulSoup(html, "html.parser")
	for each in soup.find_all("a"):
		if each.get("href") is not None and each.get("href")[0:8] == "/images/":
			return "https://wiki.guildwars.com"+each.get("href")

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
