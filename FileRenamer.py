import os
import sys

if(len(sys.argv) < 2):
    print("invalid param")
    sys.exit()
   
#path
directoryName = sys.argv [1]


#character set
invalid_characters = "#$%&\'()*+ ,-=/:;<=>?@[\\]^_`{|}~"

def clean_filename (filename):

    new_filename = filename
    #remove unwanted character s
    for ch in invalid_characters:
        new_filename = new_filename.replace(ch, '')
        

    #rename
    os.rename (directoryName + '/' + filename,directoryName + '/' + new_filename)
    print ("cleaning done : " +new_filename)


for filename in os.listdir (directoryName):

    #do something
    print ("cleaning : "+filename)
    #process the clean
    clean_filename (filename)

    
