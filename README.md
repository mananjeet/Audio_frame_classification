# Audio_frame_classification

**Data Extraction:-**

https://www.openslr.org/16/

Download headset.tar.gz and ami_manual_1.6.1.tar.gz 

**Data Preparation:-**

This part is in Matlab, So download GNU OCTAVE.

Use nite_xml_to_rttm.py to generate RTTM files from XML files given in the AMI manual.

Create audio files and reference labels for single-task SCD, OSD or VAD:
Data Preparation/prepare_data_for_wav2vec.m

**Training and Testing**

Use Setup.py to install all the dependencies.

Run the script run.sh to Train and Test the model.
