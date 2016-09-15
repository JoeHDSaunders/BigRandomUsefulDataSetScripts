import random
import xml.etree.ElementTree as ET
from xml.dom import minidom
#import time

def outputFileLook(element):
    rough = ET.tostring(element, "utf-8")
    look = minidom.parseString(rough)
    return look.toprettyxml(indent="    ")


xmlNameData = ET.parse("E:\TheBigRandomUsefullDataSet\Scripts/names.xml")
xmlNameTree = xmlNameData.getroot()

OUTPUT_FILE_LOCATION = "E:\TheBigRandomUsefullDataSet\Data\XML/names/"
OUTPUT_FILE_NAME = input("OUTPUT_NAME : ")

namesRequired = int(input("Names Required : "))
#namesRequired = 1000000

boysOrGirls = input("(M)ale, (F)emales or (B)oth Names : ")
#boysOrGirls = "M"

surnameLength = len(xmlNameTree[1])-1


newRoot = ET.Element("names")
comment = ET.Comment(str(namesRequired) + " Names In File With Gender " + boysOrGirls)
newRoot.append(comment)


#startTime = time.time()
if(boysOrGirls == "M"):
    lengthOfPos = len(xmlNameTree[0][0])-1
    for n in range(0, namesRequired):
        x = xmlNameTree[0][0][random.randint(0, lengthOfPos)].text + " " + xmlNameTree[1][random.randint(0, surnameLength)].text
        newName = ET.SubElement(newRoot, "name")
        newName.text = x
elif(boysOrGirls == "F"):
    lengthOfPos = len(xmlNameTree[0][1]) - 1
    for n in range(0, namesRequired):
        x = xmlNameTree[0][1][random.randint(0, lengthOfPos)].text + " " + xmlNameTree[1][random.randint(0, surnameLength)].text
        newName = ET.SubElement(newRoot, "name")
        newName.text = x
elif(boysOrGirls == "B"):
    lengthOfPos = [(len(xmlNameTree[0][0])-1), (len(xmlNameTree[0][1]) - 1)]
    for n in range(0, namesRequired):
        boyGirl = random.randint(0,1)
        x = xmlNameTree[0][boyGirl][random.randint(0, lengthOfPos[boyGirl])].text + " " + xmlNameTree[1][random.randint(0, surnameLength)].text
        newName = ET.SubElement(newRoot, "name")
        newName.text = x
else:
    print("You Entered A False Value")
    exit()

output = open(OUTPUT_FILE_LOCATION + OUTPUT_FILE_NAME + ".xml", "w")
output.write(outputFileLook(newRoot))
output.close()


print("Done File @ : ", OUTPUT_FILE_LOCATION + OUTPUT_FILE_NAME + ".xml")