import os
import sys

dir1 = sys.argv[1]
dir2 = sys.argv[2]

def fn_matchingfile(inputfile,comparedir):

    for dirName, subdirList, fileList in os.walk(comparedir):
        # print('Found directory: %s' % dirName)
        for fname in fileList:
            if fname==inputfile:
                with open('matchingfile.txt','wa') as f:
                   f.write('Source File: {}\{} \t Matching File: {}\{}'.format(dir1,inputfile, dirName, fname))




for eachFile in os.listdir(dir1):
    fn_matchingfile(eachFile,dir2)