# Audio_frame_classification

**Data Extraction:-**

https://www.openslr.org/16/

Download headset.tar.gz and ami_manual_1.6.1.tar.gz 

**Data Preparation:-**

This part is in Matlab, So download GNU OCTAVE.

Use folder.py to create folder for a unique meeting from the words folder present in AMI manual.

Use nite_xml_to_rttm.py to generate RTTM files from XML files given in the AMI manual.

Use path.py to create a .txt file containing all the paths of wav files per line.(refer example Sample.txt)

Create audio files and reference labels for single-task SCD, OSD or VAD:
Data Preparation/prepare_data_for_wav2vec.m

Example input  - prepare_data_for_wav2vec('wav_file_paths.txt', 'split_file' , 'references' , 'SCD' , 'SCD')

**Training and Testing**

Use Setup.py to install all the dependencies.

Run the script run.sh to Train and Test the model.
