# from distutils.filelist import findall
# import re

# pattern = re.compile("[0-9BbRr]+")

# song = """1. Z mnoha zrn se stal jeden chléb,
# co naši duši z prachu povýší,
# naplní radostí, pokojem,
# k životu v nebi nás přiblíží.

# R: Láskou proměň nám,
# to, co zde přinášíme,
# Tvé se staň.
# Dej ať jsme jedno tělo, jeden chrám,
# my děti Tvé, Ty náš pán.

# 2. Z hroznů za pár chvil bude krev,
# která nás uzdraví a očistí,
# zahojí bolesti, pády, hněv
# a svou blízkostí nás utiší."""

# songTextInParts = re.split("[0-9][.]|[R][:]|[C][:]|[B][:]", song)
# songTextInParts.pop(0) # pop the first blank space in array
# songVersesSings = re.findall("[0-9][.]|[R][:]|[C][:]|[B][:]", song)

# format = "1234RR"
# for part in format:

#     try:
#         if part.isalpha() :
#             verseIndex = songVersesSings.index(part+':')
#         elif part.isdigit() :
#             verseIndex = songVersesSings.index(part+'.')

#         print(songTextInParts[verseIndex].strip())
#         print()
#     except Exception as e:
#         print(str(e))
    
# if pattern.fullmatch("5487R21rBB") : print("yeah")
# else : print("ney")

import json
# number = 40
# song = { 
#     "song data" : {
#         "font weight" : number,
#         "song name" : "Open The Eyes",
#     },
#     "song text" : [
#         "sloka jedna", 
#         "sloka dva",
#         "sloka tri"
#     ]
# }

# song["song text"] = ['ahoj', 'jak se mas', 'ja se mam dobre']
# with open("song-data.json", "w") as file:
#     file.write(json.dumps(song))

# buildedsong = [
#     [ "2", "verse text"],
#     ["1", "verse text"]
# ]
# buildedsong.append(["B.:", "bridge text"])

# print(buildedsong)

import threading
import time


def countSeconds():
    print("Second")
    threading.Timer(1, countSeconds).start()

def countTenSeconds():
    print("Ten seconds passed")
    threading.Timer(10, countTenSeconds).start()


print("Before I'll start threads")
threading.Timer(1, countSeconds).start()
threading.Timer(10, countTenSeconds).start()

print("Here I am after threads start...")
g = input("Write me som input")
print(f"You have entered: {g}")