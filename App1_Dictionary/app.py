import json
from difflib import get_close_matches

def getDict(sw):
    data = json.load(open("Dictionary\data.json"))
    sw = sw.lower()

    if sw in data:
        defsw(data[sw])
        return print("\n{}\n{}\n\n".format(sw.title(), defsw(data[sw])))
    elif sw.capitalize() in data:
        return print("\n{}\n{}\n\n".format(sw.capitalize(), defsw(data[sw.capitalize()])))
    elif sw.upper() in data:
        return print("\n{}\n{}\n\n".format(sw.upper(), defsw(data[sw.upper()])))
    elif len(get_close_matches(sw, data.keys())) >= 1:
        return print("\nIs the word you are looking for one of these?\n{}\n\n".format(gcmst(get_close_matches(sw, data.keys()))))
    else:
        return print("\n{} was not found in the dictionary\n\n".format(sw.title()))

    print(data[sw])
    return True

def defsw(dsw):
    dss = ""
    dscnt = 1

    for ds in dsw:
        if len(dsw) != dscnt:
            dss += "{}. {}\n".format(dscnt, ds)
        else:
            dss += "{}. {}".format(dscnt, ds)

        dscnt += 1
    return dss

def gcmst(gcm):
    gc = ""
    gcct = 1

    for g in gcm:
        if len(gcm) != gcct:
            gc += "{},".format(g)
        else:
            gc += "{}".format(g)
        gcct += 1
        
    return gc

while True:

    srchWord = input("Search word: ")

    if srchWord == '\end':
        break

    getDict(srchWord)

print("Out of Dictionary.")
