import json
from difflib import get_close_matches

def getDict(sw):
    data = json.load(open("Dictionary\data.json"))
    datak = {}

    for dk in data.keys():
        if str(dk[0]).isupper() == False:
            datak.update({dk : str(dk).title()})
        else:
             datak.update({str(dk).lower() : dk})

    print(datak[sw])
    return True

while True:

    srchWord = input("Search word: ")

    if srchWord == '\end':
        break

    getDict(srchWord)

print("Out of Dictionary.")
