import os
from os import walk
import re

path = input("Bitte Verzeichnispfad angeben:")
if os.name == 'nt':
    path = path.replace("/","\\")
else:
    path = path.replace("\\","/")

os.chdir(path)
print("Verzeichnis :"+os.getcwd()+" wurde ausgewählt")

files = []
for (dirpath, dirnames, filenames) in walk(path):
    files.extend(filenames)
    break

remflag = False
rencount = 0

for f in files:
    if(f == "archive_filelist.csv"):
        os.remove(f)
        remflag = True
    newf = re.sub('^\[\d+\]_','', f)
    if f != newf:
        os.rename(f, newf)
        print("Datei: "+f+" wurde in: "+newf+" umbenannt")
        rencount += 1

s = "Es wurden: "+str(rencount)+" Dateien umbenannt"
if(remflag):
    s += ", und die archive_filelist wurde gelöscht"
print("\n"+s)