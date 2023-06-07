import math
import xml.etree.ElementTree as ET
import os

input_directory = 'XML'  # Specify the input directory here
output_directory = 'rttm'  # Specify the output directory here
os.makedirs(output_directory, exist_ok=True)
xml_trees = []

def print_rttm_line(output_file, id_value, start_time, end_time, speaker_id):
    output_file.write("SPEAKER {} 0 \t{:.2f} \t{:.2f}\t<NA>\t<NA>\t {}\t<NA>\n".format(id_value, start_time,
                                                                                      end_time - start_time,
                                                                                      speaker_id))


def convert_xml_to_rttm(xml_files, output_file):
    speaker_id_counter = 0
    for xml_file in xml_files:
        speaker_id = chr(ord('A') + speaker_id_counter)
        speaker_id_counter += 1
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
                    id_value = nite_id[:7].replace('.', '')  # Extract first 4 letters and remove '.'
                    print_rttm_line(output_file, id_value, start_time, end_time, speaker_id)
                    start_time = float(element.attrib['starttime'])
                    end_time = float(element.attrib['endtime'])
        if not ((start_time is None) or (end_time is None)):
            nite_id = root.attrib.get('{{{}}}id'.format(namespace["nite"]), '')
            id_value = nite_id[:7].replace('.', '')  # Extract first 4 letters and remove '.'
            print_rttm_line(output_file, id_value, start_time, end_time, speaker_id)


for root, dirs, files in os.walk(input_directory):
    for dir in dirs:
        folder_path = os.path.join(root, dir)
        xml_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.xml')]
        if not xml_files:
            continue
        output_file_path = os.path.join(output_directory, dir + '.rttm')
        with open(output_file_path, 'w') as output_file:
            convert_xml_to_rttm(xml_files, output_file)
