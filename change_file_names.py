import os

#get list of files
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = os.path.abspath(os.path.join(CURRENT_DIR, 'raw_data'))
OUR_DIR = os.path.abspath(os.path.join(DATA_DIR, 'our_movies'))

file_contents = os.listdir(OUR_DIR)
os.chdir(OUR_DIR)
for filename in file_contents:
    new_filename = filename.replace(":","").replace(" \" ","").replace("?","")
    os.rename(filename,new_filename)
