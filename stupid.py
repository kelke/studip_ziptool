import os
from os import walk
import re

path = input("Please enter desired folder:")
if os.name == 'nt':
    path = path.replace("/","\\")
else:
    path = path.replace("\\","/")

os.chdir(path)
print("Folder :"+os.getcwd()+" was selected")

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
        print("File: "+f+" was renamed to: "+newf)
        rencount += 1

s = "A total of: "+str(rencount)+" files were renamed"
if(remflag):
    s += ", and 'archive_filelist.csv' was deleted"
print("\n"+s)