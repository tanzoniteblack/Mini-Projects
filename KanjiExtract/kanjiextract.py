from xml.etree import ElementTree as ET
import sys

xml_file = open(sys.argv[1])

tree = ET.parse(xml_file)

for element in tree.getiterator():
    print(element)
    sys.exit()
