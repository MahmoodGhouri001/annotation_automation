import sys
import os
import os.path
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import math
from pathlib import Path
directory = r'C:\Users\96655\Downloads\CAU Sample\CAU Sample'
objList = ['orign','cicNo','branch', 'idNo', 'date','name',  'dateOfIssue', 'nationality','phoneNo',
                   'empAddress','salary', 'pOBox', 'city', 'passport', 'acNo','idType','placeOfIssue','dateOfExpiry','mobileNo','empName',
           'jobTitle','postalCode','sourceOfIncome','additionalSourceOfIncome','purposeOfAccount']


def processObject(filename):
    print(f'arun--------check {filename}')
    tree = ET.parse(filename)
    lst = tree.findall('object')

    for item in lst:
        print("....................old.................")
        print('Name', item.find('name').text)
        print('xmin', item.find('bndbox/xmin').text)
        print('ymin', item.find('bndbox/ymin').text)
        print('xmax', item.find('bndbox/xmax').text)
        print('ymax', item.find('bndbox/ymax').text)

        object = item.find('name').text
        if object == "orign":
            print('--------orign object---------')
            # input
            org_xmin = float(item.find('bndbox/xmin').text)
            org_ymin = float(item.find('bndbox/ymin').text)
            org_xmax = float(item.find('bndbox/xmax').text)
            org_ymax = float(item.find('bndbox/ymax').text)



            # find
            org_xdif =  org_xmax - org_xmin
            org_ydif = org_ymax - org_ymin
            # cal

            print("....................not updated.................")
        elif object == "cicNo":
            print('------processing cicNo--------')
            dist = math.sqrt((org_xmax - org_xmin) ** 2 + (org_ymax - org_ymin) ** 2)
            CIC_xmin = org_xmin
            CIC_ymin = org_ymin- 0.5 * (org_ymax - org_ymin)
            CIC_xmax = org_xmax
            CIC_ymax = org_ymax

            item.find('bndbox/xmin').text = str(CIC_xmin)
            item.find('bndbox/ymin').text = str(CIC_ymin)
            item.find('bndbox/xmax').text = str(CIC_xmax)
            item.find('bndbox/ymax').text = str(CIC_ymax)
            print("....................updated.................")
        elif object == "date":
            print('------processing cicNo--------')
            dist = math.sqrt((org_xmax - org_xmin) ** 2 + (org_ymax - org_ymin) ** 2)


            CIC_xmin = org_xmax+(0.17*dist)
            CIC_ymin = org_ymin
            CIC_xmax = org_xmax+(0.17*dist) +dist
            CIC_ymax = org_ymax

            item.find('bndbox/xmin').text = str(CIC_xmin)
            item.find('bndbox/ymin').text = str(CIC_ymin)
            item.find('bndbox/xmax').text = str(CIC_xmax)
            item.find('bndbox/ymax').text = str(CIC_ymax)

            print("....................updated.................")
        elif object == "branch":
            print('------processing branch--------')
            dist = math.sqrt((org_xmax - org_xmin) ** 2 + (org_ymax - org_ymin) ** 2)

            CIC_xmin = org_xmax + (0.17 * dist)
            CIC_ymin = org_ymin -org_ydif
            CIC_xmax = org_xmax + (0.17 * dist) + dist
            CIC_ymax = org_ymax-org_ydif

            item.find('bndbox/xmin').text = str(CIC_xmin)
            item.find('bndbox/ymin').text = str(CIC_ymin)
            item.find('bndbox/xmax').text = str(CIC_xmax)
            item.find('bndbox/ymax').text = str(CIC_ymax)
            print("....................updated.................")
        #elif object == "":
            #cic('')
        # print(a)
        elif object == "name":
            print('------processing name--------')
            dist = math.sqrt((org_xmax - org_xmin) ** 2 + (org_ymax - org_ymin) ** 2)

            CIC_xmin = org_xmax + (0.17 * dist)
            CIC_ymin = org_ymin + org_ydif*2
            CIC_xmax = org_xmax + (0.17 * dist) + dist
            CIC_ymax = org_ymax + org_ydif*2

            item.find('bndbox/xmin').text = str(CIC_xmin)
            item.find('bndbox/ymin').text = str(CIC_ymin)
            item.find('bndbox/xmax').text = str(CIC_xmax)
            item.find('bndbox/ymax').text = str(CIC_ymax)

            print("....................updated.................")
        elif object == "nationality":
            print('------processing nationality--------')

            dist = math.sqrt((org_xmax - org_xmin) ** 2 + (org_ymax - org_ymin) ** 2)

            CIC_xmin = org_xmax + (0.17 * dist)
            CIC_ymin = org_ymin + org_ydif * 3
            CIC_xmax = org_xmax + (0.17 * dist) + dist
            CIC_ymax = org_ymax + org_ydif * 3

            item.find('bndbox/xmin').text = str(CIC_xmin)
            item.find('bndbox/ymin').text = str(CIC_ymin)
            item.find('bndbox/xmax').text = str(CIC_xmax)
            item.find('bndbox/ymax').text = str(CIC_ymax)
            print("....................updated.................")
        elif object == "idNo":
            print('------processing idNo--------')
            dist = math.sqrt((org_xmax - org_xmin) ** 2 + (org_ymax - org_ymin) ** 2)

            CIC_xmin = org_xmax + (0.17 * dist)
            CIC_ymin = org_ymin + org_ydif * 4
            CIC_xmax = org_xmax + (0.17 * dist) + dist
            CIC_ymax = org_ymax + org_ydif * 4

            item.find('bndbox/xmin').text = str(CIC_xmin)
            item.find('bndbox/ymin').text = str(CIC_ymin)
            item.find('bndbox/xmax').text = str(CIC_xmax)
            item.find('bndbox/ymax').text = str(CIC_ymax)

            print("....................updated.................")

        elif object == "dateOfIssue":
            print('------processing dateOfIssue--------')
            dist = math.sqrt((org_xmax - org_xmin) ** 2 + (org_ymax - org_ymin) ** 2)

            CIC_xmin = org_xmax + (0.17 * dist)
            CIC_ymin = org_ymin + org_ydif * 5
            CIC_xmax = org_xmax + (0.17 * dist) + dist
            CIC_ymax = org_ymax + org_ydif * 5

            item.find('bndbox/xmin').text = str(CIC_xmin)
            item.find('bndbox/ymin').text = str(CIC_ymin)
            item.find('bndbox/xmax').text = str(CIC_xmax)
            item.find('bndbox/ymax').text = str(CIC_ymax)
            print("....................updated.................")

        elif object == "phoneNo":
            print('------processing cicNo--------')
            dist = math.sqrt((org_xmax - org_xmin) ** 2 + (org_ymax - org_ymin) ** 2)

            CIC_xmin = org_xmax + (0.17 * dist)
            CIC_ymin = org_ymin + org_ydif * 6
            CIC_xmax = org_xmax + (0.17 * dist) + dist
            CIC_ymax = org_ymax + org_ydif * 6

            item.find('bndbox/xmin').text = str(CIC_xmin)
            item.find('bndbox/ymin').text = str(CIC_ymin)
            item.find('bndbox/xmax').text = str(CIC_xmax)
            item.find('bndbox/ymax').text = str(CIC_ymax)
            print("....................updated.................")
        elif object == "empAddress":
            print('------processing cicNo--------')
            print('------processing idNo--------')
            dist = math.sqrt((org_xmax - org_xmin) ** 2 + (org_ymax - org_ymin) ** 2)

            CIC_xmin = org_xmax + (0.17 * dist)
            CIC_ymin = org_ymin + org_ydif * 7
            CIC_xmax = org_xmax + (0.17 * dist) + dist
            CIC_ymax = org_ymax + org_ydif * 7

            item.find('bndbox/xmin').text = str(CIC_xmin)
            item.find('bndbox/ymin').text = str(CIC_ymin)
            item.find('bndbox/xmax').text = str(CIC_xmax)
            item.find('bndbox/ymax').text = str(CIC_ymax)

            print("....................updated.................")
        elif object == "salary":
            print('------processing cicNo--------')

            dist = math.sqrt((org_xmax - org_xmin) ** 2 + (org_ymax - org_ymin) ** 2)

            CIC_xmin = org_xmax + (0.17 * dist)
            CIC_ymin = org_ymin + org_ydif * 8
            CIC_xmax = org_xmax + (0.17 * dist) + dist
            CIC_ymax = org_ymax + org_ydif * 8

            item.find('bndbox/xmin').text = str(CIC_xmin)
            item.find('bndbox/ymin').text = str(CIC_ymin)
            item.find('bndbox/xmax').text = str(CIC_xmax)
            item.find('bndbox/ymax').text = str(CIC_ymax)
            print("....................updated.................")
        elif object == "pOBox":
            print('------processing idNo--------')
            dist = math.sqrt((org_xmax - org_xmin) ** 2 + (org_ymax - org_ymin) ** 2)

            CIC_xmin = org_xmax + (0.17 * dist)
            CIC_ymin = org_ymin + org_ydif * 9
            CIC_xmax = org_xmax + (0.17 * dist) + dist
            CIC_ymax = org_ymax + org_ydif * 9

            item.find('bndbox/xmin').text = str(CIC_xmin)
            item.find('bndbox/ymin').text = str(CIC_ymin)
            item.find('bndbox/xmax').text = str(CIC_xmax)
            item.find('bndbox/ymax').text = str(CIC_ymax)

            print("....................updated.................")
        elif object == "city":
            print('------processing idNo--------')
            dist = math.sqrt((org_xmax - org_xmin) ** 2 + (org_ymax - org_ymin) ** 2)

            CIC_xmin = org_xmax + (0.17 * dist)
            CIC_ymin = org_ymin + org_ydif * 10
            CIC_xmax = org_xmax + (0.17 * dist) + dist
            CIC_ymax = org_ymax + org_ydif * 10

            item.find('bndbox/xmin').text = str(CIC_xmin)
            item.find('bndbox/ymin').text = str(CIC_ymin)
            item.find('bndbox/xmax').text = str(CIC_xmax)
            item.find('bndbox/ymax').text = str(CIC_ymax)

            print("....................updated.................")
        elif object == "passport":
            print('------processing passport--------')
            dist = math.sqrt((org_xmax - org_xmin) ** 2 + (org_ymax - org_ymin) ** 2)

            CIC_xmin = org_xmax + (0.17 * dist)
            CIC_ymin = org_ymin + org_ydif * 12
            CIC_xmax = org_xmax + (0.17 * dist) + dist
            CIC_ymax = org_ymax + org_ydif * 12

            item.find('bndbox/xmin').text = str(CIC_xmin)
            item.find('bndbox/ymin').text = str(CIC_ymin)
            item.find('bndbox/xmax').text = str(CIC_xmax)
            item.find('bndbox/ymax').text = str(CIC_ymax)
            print("....................updated.................")
        elif object == "acNo":
            print('------processing acNo--------')
            dist = math.sqrt((org_xmax - org_xmin) ** 2 + (org_ymax - org_ymin) ** 2)
            CIC_xmin = org_xmin
            CIC_ymin = org_ymin + 2.2 * (org_ymax - org_ymin)
            CIC_xmax = org_xmax
            CIC_ymax = org_ymax + 3.2 * (org_ymax - org_ymin)

            item.find('bndbox/xmin').text = str(CIC_xmin)
            item.find('bndbox/ymin').text = str(CIC_ymin)
            item.find('bndbox/xmax').text = str(CIC_xmax)
            item.find('bndbox/ymax').text = str(CIC_ymax)
            print("....................updated.................")
        elif object == "idType":
            print('------processing idType--------')
            dist = math.sqrt((org_xmax - org_xmin) ** 2 + (org_ymax - org_ymin) ** 2)
            CIC_xmin = org_xmin
            CIC_ymin = org_ymin + 4.2 * (org_ymax - org_ymin)
            CIC_xmax = org_xmax
            CIC_ymax = org_ymax + 4.2 * (org_ymax - org_ymin)

            item.find('bndbox/xmin').text = str(CIC_xmin)
            item.find('bndbox/ymin').text = str(CIC_ymin)
            item.find('bndbox/xmax').text = str(CIC_xmax)
            item.find('bndbox/ymax').text = str(CIC_ymax)

            print("....................updated.................")
        elif object == "placeOfIssue":
            print('------processing cicNo--------')
            dist = math.sqrt((org_xmax - org_xmin) ** 2 + (org_ymax - org_ymin) ** 2)
            CIC_xmin = org_xmin
            CIC_ymin = org_ymin + 5.2 * (org_ymax - org_ymin)
            CIC_xmax = org_xmax
            CIC_ymax = org_ymax + 5.2 * (org_ymax - org_ymin)

            item.find('bndbox/xmin').text = str(CIC_xmin)
            item.find('bndbox/ymin').text = str(CIC_ymin)
            item.find('bndbox/xmax').text = str(CIC_xmax)
            item.find('bndbox/ymax').text = str(CIC_ymax)

            print("....................updated.................")
        elif object == "dateOfExpiry":
            print('------processing cicNo--------')
            dist = math.sqrt((org_xmax - org_xmin) ** 2 + (org_ymax - org_ymin) ** 2)
            CIC_xmin = org_xmin
            CIC_ymin = org_ymin + 6.2 * (org_ymax - org_ymin)
            CIC_xmax = org_xmax
            CIC_ymax = org_ymax + 6.2 * (org_ymax - org_ymin)

            item.find('bndbox/xmin').text = str(CIC_xmin)
            item.find('bndbox/ymin').text = str(CIC_ymin)
            item.find('bndbox/xmax').text = str(CIC_xmax)
            item.find('bndbox/ymax').text = str(CIC_ymax)

            print("....................updated.................")
        elif object == "mobileNo":
            print('------processing cicNo--------')
            dist = math.sqrt((org_xmax - org_xmin) ** 2 + (org_ymax - org_ymin) ** 2)
            CIC_xmin = org_xmin
            CIC_ymin = org_ymin + 7.2 * (org_ymax - org_ymin)
            CIC_xmax = org_xmax
            CIC_ymax = org_ymax + 7.2 * (org_ymax - org_ymin)

            item.find('bndbox/xmin').text = str(CIC_xmin)
            item.find('bndbox/ymin').text = str(CIC_ymin)
            item.find('bndbox/xmax').text = str(CIC_xmax)
            item.find('bndbox/ymax').text = str(CIC_ymax)
            print("....................updated.................")
        elif object == "empName":
            print('------processing cicNo--------')
            dist = math.sqrt((org_xmax - org_xmin) ** 2 + (org_ymax - org_ymin) ** 2)
            CIC_xmin = org_xmin
            CIC_ymin = org_ymin + 8.2 * (org_ymax - org_ymin)
            CIC_xmax = org_xmax
            CIC_ymax = org_ymax + 8.2 * (org_ymax - org_ymin)

            item.find('bndbox/xmin').text = str(CIC_xmin)
            item.find('bndbox/ymin').text = str(CIC_ymin)
            item.find('bndbox/xmax').text = str(CIC_xmax)
            item.find('bndbox/ymax').text = str(CIC_ymax)
            print("....................updated.................")
        elif object == "jobTitle":
            print('------processing cicNo--------')
            dist = math.sqrt((org_xmax - org_xmin) ** 2 + (org_ymax - org_ymin) ** 2)
            CIC_xmin = org_xmin
            CIC_ymin = org_ymin + 9.2 * (org_ymax - org_ymin)
            CIC_xmax = org_xmax
            CIC_ymax = org_ymax + 9.2 * (org_ymax - org_ymin)

            item.find('bndbox/xmin').text = str(CIC_xmin)
            item.find('bndbox/ymin').text = str(CIC_ymin)
            item.find('bndbox/xmax').text = str(CIC_xmax)
            item.find('bndbox/ymax').text = str(CIC_ymax)
            print("....................updated.................")
        elif object == "sourceOfIncome":
            print('------processing cicNo--------')
            dist = math.sqrt((org_xmax - org_xmin) ** 2 + (org_ymax - org_ymin) ** 2)
            CIC_xmin = org_xmin
            CIC_ymin = org_ymin + 14.2 * (org_ymax - org_ymin)
            CIC_xmax = org_xmax * 1.99
            CIC_ymax = org_ymax + 16.5 * (org_ymax - org_ymin)

            item.find('bndbox/xmin').text = str(CIC_xmin)
            item.find('bndbox/ymin').text = str(CIC_ymin)
            item.find('bndbox/xmax').text = str(CIC_xmax)
            item.find('bndbox/ymax').text = str(CIC_ymax)

            print("....................updated.................")
        elif object == "postalCode":
            print('------processing cicNo--------')
            dist = math.sqrt((org_xmax - org_xmin) ** 2 + (org_ymax - org_ymin) ** 2)
            CIC_xmin = org_xmin
            CIC_ymin = org_ymin + 10.2 * (org_ymax - org_ymin)
            CIC_xmax = org_xmax
            CIC_ymax = org_ymax + 10.2 * (org_ymax - org_ymin)

            item.find('bndbox/xmin').text = str(CIC_xmin)
            item.find('bndbox/ymin').text = str(CIC_ymin)
            item.find('bndbox/xmax').text = str(CIC_xmax)
            item.find('bndbox/ymax').text = str(CIC_ymax)

            print("....................updated.................")
        elif object == "additionalSourceOfIncome":
            print('------processing cicNo--------')
            CIC_xmin = org_xmin
            CIC_ymin = org_ymin + 20.2 * (org_ymax - org_ymin)
            CIC_xmax = org_xmax * 1.99
            CIC_ymax = org_ymax + 21 * (org_ymax - org_ymin)

            item.find('bndbox/xmin').text = str(CIC_xmin)
            item.find('bndbox/ymin').text = str(CIC_ymin)
            item.find('bndbox/xmax').text = str(CIC_xmax)
            item.find('bndbox/ymax').text = str(CIC_ymax)
            print("....................updated.................")
        elif object == "purposeOfAccount":
            print('------processing purposeOfAccount--------')
            CIC_xmin = org_xmin
            CIC_ymin = org_ymin + 26.8 * (org_ymax - org_ymin)
            CIC_xmax = org_xmax * 1.99
            CIC_ymax = org_ymax + 27.6 * (org_ymax - org_ymin)

            item.find('bndbox/xmin').text = str(CIC_xmin)
            item.find('bndbox/ymin').text = str(CIC_ymin)
            item.find('bndbox/xmax').text = str(CIC_xmax)
            item.find('bndbox/ymax').text = str(CIC_ymax)

            print("....................updated.................")

        print("....end..")

        tree.write(filename)



def cic(object,item):

    return True

def prettify(filename):
    # ------------pretty print-------
    tree_pretty = ET.parse(filename)
    root_pretty = tree_pretty.getroot()
    xmlstr = minidom.parseString(ET.tostring(root_pretty)).toprettyxml(indent="   ")
    with open(filename, "w") as f:
        f.write(xmlstr)

def processXmlFile(filename):
    tree = ET.parse(filename)
    lst = tree.findall('object')
    root = tree.getroot()

    print(f'processing xml for file {filename}')
    for i in range(len(objList)):
        if objList[i] not in lst:
            print('ghouri'+str(objList[i]))
            print(lst)

            new = ET.Element("object")
            newsub1 = ET.SubElement(new, "name")
            newsub1.text = str(objList[i])
            newsub2 = ET.SubElement(new, "pose")
            newsub2.text = str('Unspecified')
            newsub3 = ET.SubElement(new, "truncated")
            newsub3.text = str('Unspecified')
            # newsub3 = ET.SubElement(new, "truncated")
            # n
            newsub4 = ET.SubElement(new, "difficult")
            newsub4.text = '0'
            newsub5 = ET.SubElement(new, "bndbox")
            newsub6 = ET.SubElement(newsub5, "xmin")
            newsub6.text = '216'
            newsub7 = ET.SubElement(newsub5, "ymin")
            newsub7.text = '418'
            newsub8 = ET.SubElement(newsub5, "xmax")
            newsub8.text = '1115'
            newsub9 = ET.SubElement(newsub5, "ymax")
            newsub9.text = '507'
            root.append(new)
            tree.write(filename)

def addXmlFile(filename_1,filename):
    blankroot = ET.Element("annotation")
    #print(filename_1)
    subelement_folder = ET.SubElement(blankroot, "folder")
    subelement_folder.text = '100'
    subelement_filename = ET.SubElement(blankroot, "filename")
    subelement_filename.text = filename
    subelement_path = ET.SubElement(blankroot, "path")
    subelement_path.text = filename_1
    subelement_source = ET.SubElement(blankroot, "source")
    subelement_databaseheight = ET.SubElement(subelement_source, "database")
    subelement_size = ET.SubElement(blankroot, "size")

    subelement_width = ET.SubElement(subelement_size, "width")
    subelement_width.text = '2466'
    subelement_height = ET.SubElement(subelement_size, "height")
    subelement_height.text = '3504'
    subelement_depth = ET.SubElement(subelement_size, "depth")
    subelement_depth.text = '1'
    subelement_segmented = ET.SubElement(blankroot, "segmented")
    subelement_segmented.text = '0'
    tree_new = ET.ElementTree(blankroot)
    # dd=prettify(tree_new)

    tree_new.write(filename_1 + '.xml')

firstFile =''
#start program look for files in directory and create or update xml files with mentioned objects in objList
for filename in os.listdir(directory):
    firstFile =filename
    if filename.lower().endswith(".jpg") or filename.lower().endswith(".png") or filename.lower().endswith(".tif"):
        filename_1, file_extension = os.path.splitext(directory+'\\'+filename)
        if os.path.isfile(filename_1+'.xml'):
            print('filename exits')
            #processXmlFile(filename_1+'.xml')#add blank mentioned objects
            processObject(filename_1+'.xml')
            # prettify(filename_1+'.xml')
        else:
            print(f'xml file present for {filename_1}')
            addXmlFile(filename_1,filename)
            processXmlFile(filename_1+'.xml')
            processObject(filename_1+'.xml')
            prettify(filename_1+'.xml')
        continue




    # stuff.write("test.xml")

    # print('Attribute', item.get("x"))



