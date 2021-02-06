import pandas as pd
import os
import shutil

filedf = pd.read_csv('trainLabels.csv',skipinitialspace=True, usecols=['filename','grade'], sep=';')
nodrcount = 0 
moddrcount = 0
highdrcount = 0

def nodr(filename):
    global nodrcount
    nodrcount = nodrcount + 1
    srcfile = "train\\" + filename + ".jpeg" 
    destfile = "dataset\\nodr"
    shutil.copy2(srcfile, destfile)
    
    
def moddr(filename):
    global moddrcount
    moddrcount = moddrcount + 1 
    srcfile = "train\\" + filename + ".jpeg" 
    destfile = "dataset\\moddr"
    shutil.copy2(srcfile, destfile)
    
def highdr(filename):
    global highdrcount
    highdrcount = highdrcount + 1 
    srcfile = "train\\" + filename + ".jpeg" 
    destfile = "dataset\\highdr"
    shutil.copy2(srcfile, destfile)
    
switcher = { 0:nodr, 1:moddr, 2:moddr, 3:highdr, 4:highdr }

for index, row in filedf.iterrows():
    func = switcher.get(row['grade'], "invalid")
    print(row['filename'])
    try:
        func(row['filename']) 
    except :
        print('file not found : {}',row['filename'])
    
print("nodrcount : {} , moddrcount: {} , highdrcount: {}".format(nodrcount, moddrcount, highdrcount))