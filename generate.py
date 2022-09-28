# -*- coding: utf-8 -*-
import re
import unicodedata

# works like .strip() but takes regex instead of string
def re_strip(string, char="\s"):
    result = re.sub(f"^{char}+", "", string)
    result = re.sub(f"{char}+$", "", result)
    return result

settings = open("Settings.txt", encoding="utf-8-sig") 
# skip first two lines
[settings.readline() for i in range(2)] 


regexParam = re.compile("[,\s]").pattern
regexParam2 = re.compile("[,\s]")

# open output file from line 3
output = open(re_strip(settings.readline(), regexParam),"w", encoding="utf-8-sig")

# write ahk header
output.write("""#NoEnv
SendMode Input
SetWorkingDir %A_ScriptDir%\n\n"""
)
# skip line 4 of setting
settings.readline() 
# write hotkey into file
output.write( re_strip(settings.readline(), regexParam) + "::\n")

#get font and box size and number of colums
settings.readline()
fSize = int(re_strip(settings.readline(),regexParam))
settings.readline()
bSize = re_strip(settings.readline(),regexParam)
bSize = fSize*2 if bSize == "" else int(bSize)
settings.readline()
nCols = int(re_strip(settings.readline(),regexParam))

# creates list of characters
settings.readline()
chars = []
for line in settings:
    chars += regexParam2.split(line)
temp = []
for char in chars:
    if char != "":
        temp.append(char)
chars = temp

#create the gui
output.write("\tGui, Font, s"+str(fSize)+
             "\tGui, Add, Text, , select symbol\n")
i = 0
for char in chars:
    if i%nCols == 0:
        #newline
        output.write("\tGui, Add, Button,xm  W"+str(bSize)+" H"+str(bSize)+", "+char+"\n")
    else:
        output.write("\tGui, Add, Button,x+0 W"+str(bSize)+" H"+str(bSize)+", "+char+"\n")
    i = i+1

output.write("\n\tGui, Show, , SymbolGUI\n\tReturn\n")

#create button presses
temp = []
for char in chars:
    if(char not in temp):
        output.write("\tButton"+char+":\n"+
                     "\t\tWinClose\n"+
                     "\t\tSend, "+char+"\n"+
                     "\t\tReturn\n")    
    temp.append(char)

#create bottom section for better naviagation with arrows
output.write("\n\n"+
             "#IfWinActive, SymbolGUI\n\n"+
             "Down::\n"+
             "\tSend, {Right "+str(nCols)+"}\n"+
             "\treturn\n"+
             "Up::\n"+
             "\tSend, {Left "+str(nCols)+"}\n"+
             "\treturn")