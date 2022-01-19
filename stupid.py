import os
from os import walk
import re

path = input("Bitte Verzeichnispfad angeben:")
path = path.replace("/","\\")
os.chdir(path)
print("Verzeichnis :"+os.getcwd()+" wurde ausgewählt")

fn = "[17]_220113_b.pdf"
newfn = re.sub('^\[\d+\]_','', fn)
#os.rename(fn, newfn)
#print(fn+" wurde in: "+newfn+"geändert")

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