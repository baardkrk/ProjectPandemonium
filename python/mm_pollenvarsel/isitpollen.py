from bs4 import BeautifulSoup
import requests


SCRIPT_INDEX = 9
ID_LENGTH = 32
ID_OFFSET_STRING = "': '"

INVALID_OPTION = -1
TYPE = ["Or", "Hassel", "Bjork", "Salix", "Gress", "Burot"]

AREA_IDS = ["fjellsor", "rogaland", "soerlandet", "hordaland", "sognfjorande", \
            "troendelag", "finnmark", "troms", "nordland", "indreostland", \
            "oestlandoslo", "moereromsdal"]
CURRENT_AREA = 10


def getPollenHTML():
    url = "https://www.naaf.no/pollenvarsel/"
    
    htmlCode = requests.get(url)
    soup = BeautifulSoup(htmlCode.text, "html.parser")

    return soup


def getScriptContent(htmlSoup):
    scriptContent = htmlSoup.find_all('script')[SCRIPT_INDEX].string
    return scriptContent


def getIdentifier(typeIdx, scriptContent):
    identifierIdx = scriptContent.find(TYPE[typeIdx]) - (len(ID_OFFSET_STRING) + ID_LENGTH)
    identifier = scriptContent[identifierIdx:identifierIdx+ID_LENGTH]

    if (identifierIdx <= 0):
        identifier = INVALID_OPTION

    return identifier


def getPollenValue(area, day, pollenIdentifier,  scriptContent):
    areaIdx = scriptContent.find(AREA_IDS[area])
    dayIdx = scriptContent.find(day, areaIdx)
    pollenValueIdx = scriptContent.find(pollenIdentifier, dayIdx)

    startIdx = pollenValueIdx + ID_LENGTH + len(ID_OFFSET_STRING)
    endIdx = scriptContent.find("\",",startIdx)
    
    pollenValue = scriptContent[startIdx:endIdx];

    return pollenValue


##### tests

## make variables in a class possibly? (to avoid unneccessary querys)
## and also to avoid passing around the scriptContent all the time
msoup = getPollenHTML()
scCont = getScriptContent(msoup)
identifier = getIdentifier(0, scCont)

print(getPollenValue(CURRENT_AREA, "today", identifier, scCont))

