import xml.etree.ElementTree as ET
import os

# Directory containing the XML files
xml_directory = 'XML' 
#Add all the word files for a single meeting in a directory naming as the meeting ex. EN2001

# Output RTTM file
output_rttm_file = f'{xml_directory}.rttm'

# Create the root element for the combined XML
combined_root = ET.Element('combined')

# Iterate over the XML files in the directory
for file_name in os.listdir(xml_directory):
    if file_name.endswith('.xml'):
        file_path = os.path.join(xml_directory, file_name)
        tree = ET.parse(file_path)
        root = tree.getroot()

        # Append the root of each XML file to the combined XML
        combined_root.extend(root)

# Create a new XML document with the combined elements
combined_tree = ET.ElementTree(combined_root)

# Sort the elements based on the start time attribute
elements = combined_root.findall('.//w')
sorted_elements = sorted(elements, key=lambda e: float(e.get('starttime')))

# Create a new root element for the sorted elements
sorted_root = ET.Element(combined_root.tag)

# Add the sorted elements to the new root
for element in sorted_elements:
    sorted_root.append(element)

# Create a new XML document with the sorted elements
sorted_tree = ET.ElementTree(sorted_root)

# Generate RTTM from the sorted XML
words = []
for w in sorted_root.findall('.//w'):
    word = w.text
    word_id = None
    for attr_name, attr_value in w.attrib.items():
        if 'id' in attr_name:
            word_id = attr_value[8:9]
            break
    starttime = float(w.attrib['starttime'])
    endtime = float(w.attrib['endtime'])
    words.append((word, word_id, starttime, endtime))

rttm_lines = []
prev_word_id = None
sentence = ''
start_time = None
end_time = None
for i, (word, word_id, starttime, endtime) in enumerate(words):
    if i == 0 or word_id != prev_word_id:
        if sentence:
            duration = end_time - start_time
            rttm_line = f"SPEAKER {prev_word_id} "
            rttm_line += ' ' + 'Start_time' + '-' + f"{start_time:.2f} "
            rttm_line += ' ' + 'End_time' + '-' + f"{end_time:.2f} "
            rttm_line += ' ' + 'Duration' + '-' + f"{duration:.2f} "
            rttm_line += f"{sentence}"
            rttm_lines.append(rttm_line)
            sentence = ''
        if word_id:
            start_time = starttime
    sentence += word + ' '
    prev_word_id = word_id
    end_time = endtime

if sentence:
    duration = end_time - start_time
    rttm_line = f"SPEAKER {prev_word_id} "
    rttm_line += f"{start_time:.2f} "
    rttm_line += f"{end_time:.2f} "
    rttm_line += f"{duration:.2f} "
    rttm_line += f"{sentence}"
    rttm_lines.append(rttm_line)

# Write the RTTM lines to the output file
with open(output_rttm_file, 'w') as f:
    f.write('\n'.join(rttm_lines))

print(f"RTTM file '{output_rttm_file}' generated successfully.")
