#!/usr/bin/env python3

import os, sys
import xml.etree.ElementTree as et

def main():
    homepath = os.path.expanduser('~')
    if not os.path.isfile(homepath + '/.htpc-browser-launcher/htpc-browser-launcher.py'):
        print('Install HTPC Browser Launcher before running this script')
        print('Exiting')
        sys.exit(0)
    xmlfile = False
    if os.path.isfile("/usr/share/mythtv/themes/defaultmenu/mainmenu.xml"):
        xmlfile = "/usr/share/mythtv/themes/defaultmenu/mainmenu.xml"
    if os.path.isdir(homepath + '/.mythtv'):
        if os.path.isfile(homepath + '/.mythtv/mainmenu.xml'):
            xmlfile = homepath + '/.mythtv/mainmenu.xml'
    else:
        os.mkdir(homepath + '/.mythtv')
    if not xmlfile:
        print('Required menu file not found')
        print('Exiting')
        sys.exit(0)
    tree = et.parse(xmlfile)
    root = tree.getroot()
    newelement = et.Element("button")
    newelement.tail = "\n\n    "
    newelement.text = "\n        "
    newsubelement = et.SubElement(newelement, "type")
    newsubelement.tail = "\n        "
    newsubelement.text = "TV_WATCH_TV"
    newsubelement = et.SubElement(newelement, "text")
    newsubelement.tail = "\n        "
    newsubelement.text = "Chromium"
    newsubelement = et.SubElement(newelement, "description")
    newsubelement.tail = "\n        "
    newsubelement.text = "Launch Chromium"
    newsubelement = et.SubElement(newelement, "action")
    newsubelement.tail = "\n    "
    exe = 'EXEC ' + homepath + '/.htpc-browser-launcher/htpc-browser-launcher.py'
    newsubelement.text = exe + ' chromium-browser'
    lengthtree = len(list(root))
    if lengthtree > 4:
        position = lengthtree - 2
    else:
        position = 1
    root.insert(position, newelement)
    addchrome = input('Also add a menu button for Chrome? (y/n): ').lower().strip()[0]
    if addchrome == "y":
        newelement = et.Element("button")
        newelement.tail = "\n\n    "
        newelement.text = "\n        "
        newsubelement = et.SubElement(newelement, "type")
        newsubelement.tail = "\n        "
        newsubelement.text = "TV_WATCH_TV"
        newsubelement = et.SubElement(newelement, "text")
        newsubelement.tail = "\n        "
        newsubelement.text = "Chrome"
        newsubelement = et.SubElement(newelement, "description")
        newsubelement.tail = "\n        "
        newsubelement.text = "Launch Chrome"
        newsubelement = et.SubElement(newelement, "action")
        newsubelement.tail = "\n    "
        newsubelement.text = exe + ' google-chrome'
        root.insert(position, newelement)
    tree.write(homepath + '/.mythtv/mainmenu.xml', encoding="utf-8", xml_declaration=True)
    print('Done')
    print('Please restart MythTV Frontend')

if __name__ == '__main__':
    if os.geteuid() != 0:
        main()
    else:
        print('Run this script without using sudo')
        print('Exiting')
