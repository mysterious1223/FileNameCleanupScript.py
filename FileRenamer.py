import os
import sys

if(len(sys.argv) < 2):
    print("invalid param")
    sys.exit()
   
#path
directoryName = sys.argv [1]


#character set
invalid_characters = "#$%&\'()*+ ,-=/:;<=>?@[\\]^_`{|}~"

def clean_filename (filename, sourceDirectory):

    new_filename = filename
    #remove unwanted character s
    for ch in invalid_characters:
        new_filename = new_filename.replace(ch, '')
        

    #rename
    os.rename (sourceDirectory + '/' + filename, sourceDirectory + '/'+ new_filename)
    print ("[+] cleaning done : " +new_filename)

def ProcessClean (SourceDirectory):

    for filename in os.listdir (SourceDirectory):

        if (os.path.isfile (SourceDirectory + '/' + filename)):
            #do something
            print ("[-] cleaning : "+filename)
            #process the clean
            clean_filename (filename, SourceDirectory)
        else:
            print ("[-] Entering a sub directory -> " + SourceDirectory + '/' + filename)
            ProcessClean (SourceDirectory + '/' + filename)


ProcessClean (directoryName)

    
