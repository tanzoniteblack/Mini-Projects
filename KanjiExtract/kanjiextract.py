from xml.etree import ElementTree as etree
import sys

with open("kanjidic2.xml") as xml_file:
    tree = etree.parse(xml_file)

most_freq = {}
root = tree.getroot()

for element in root:
    if element.tag == "character":
        misc = element.find("misc")
        freq = misc.find("freq")
        if freq is not None:
            most_freq[int(freq.text)] = element

most_freq_nums = sorted(most_freq)
most_freq = [most_freq[x] for x in most_freq_nums]

for item in most_freq:
    print(item.find("literal").text, item.find("misc").find("freq").text)
