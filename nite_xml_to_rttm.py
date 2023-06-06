import math
import sys
import xml.etree.ElementTree as ET

xml_trees = []

def print_rttm_line(id_value,start_time, end_time, speaker_id):
    speaker_char = chr(ord('A') + speaker_id)  
    print("SPEAKER {} 0 \t{:.2f} \t{:.2f}\t<NA>\t<NA>\t {}\t<NA>".format(id_value,start_time, end_time - start_time,
                                                                            speaker_char))


def convert_xml_to_rttm():
    xml_file = xml_files[xml_file_index]
    tree = ET.parse(xml_file)
    root = tree.getroot()
    xml_trees.append(root)
    start_time = end_time = None

    # Define the namespace
    namespace = {"nite": "http://nite.sourceforge.net/"}

    for element in root.iter("w"):
        if 'starttime' in element.attrib and 'endtime' in element.attrib:
            if start_time is None:
                start_time = float(element.attrib['starttime'])
            if end_time is None:
                end_time = float(element.attrib['starttime'])  # yes, 'starttime'
            if math.isclose(end_time, float(element.attrib['starttime']), abs_tol=0.01):
                # collapse the two
                end_time = float(element.attrib['endtime'])
            else:
                nite_id = element.attrib.get('{{{}}}id'.format(namespace["nite"]), '')
                id_value = nite_id[:7]  # Extract first 4 letters
                print_rttm_line(id_value, start_time, end_time, speaker_id=xml_file_index)
                start_time = float(element.attrib['starttime'])
                end_time = float(element.attrib['endtime'])
    if not ((start_time is None) or (end_time is None)):
        nite_id = root.attrib.get('{{{}}}id'.format(namespace["nite"]), '')
        id_value = nite_id[:7]  # Extract first 4 letters
        print_rttm_line(id_value, start_time, end_time, speaker_id=xml_file_index)

xml_files = sys.argv[1:]
for xml_file_index in range(len(xml_files)):
    convert_xml_to_rttm()
