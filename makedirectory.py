import os
from pathlib import Path

filename = str(input("filename?:"))#get file that has wanted structure in it (see filestructure.md)
filelist = []

def get_dictionary_word_list():
    """
    open file with the file structure and put in a list
    """
    f = open(filename)
    for word in f.read().split():
        filelist.append(word)

get_dictionary_word_list()

def splitter():
    """
    split the list of directories and ├── symbols imto lists that will make paths
    """
    particular_value = "├──"
    result = []
    temp_list = []
    for i in filelist:
        if i == particular_value:
            temp_list.append(i)
            result.append(temp_list)
            temp_list = []
        else:
            temp_list.append(i)
    result.append(temp_list)
    return result

splitlist = splitter()
print(splitlist)

finalstructure = []

def removesymbol():
    """
    get rid of ugly ├── symbols
    """
    for i in splitlist:
        removedstuff = [x for x in i if "├──" not in x]
        finalstructure.append(removedstuff)
    del finalstructure[0]

removesymbol()

def structuremaker():
    """
    actually make paths and create folders with them
    """
    for i in finalstructure:
        x = "/".join(i)
        print(x)
        os.makedirs(x)

structuremaker()


        