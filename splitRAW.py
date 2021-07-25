import os
import shutil


dataDir = "data/"
rawDir = "raw/"
jpgDir = "jpg/"

for entry in os.listdir(dataDir):
    if os.path.isfile(os.path.join(dataDir, entry)):
        #print(entry)
        if entry.endswith("JPG"):
            print(entry)
            shutil.copy(dataDir + entry, jpgDir)
        if entry.endswith("ARW"):
            print(entry)
            shutil.copy(dataDir + entry, rawDir)
