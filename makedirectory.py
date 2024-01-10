import os
from pathlib import Path
import click


filelist = []
finalstructure = []

@click.command()
@click.option('--filename', default='structureexample.md', help='file containing desired option, default = structureexample.md')

def get_dictionary_word_list(filename):
    """
    open file with the file structure and put in a list
    """
    f = open(filename)
    for word in f.read().split():
        filelist.append(word)

    splitter()


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
    removesymbol(result)

def removesymbol(splitlist):
    """
    get rid of ugly ├── symbols
    """
    for i in splitlist:
        removedstuff = [x for x in i if "├──" not in x]
        finalstructure.append(removedstuff)
    del finalstructure[0]
    structuremaker()

def structuremaker():
    """
    actually make paths and create folders with them
    """
    for i in finalstructure:
        x = "/".join(i)
        print(x)
        os.makedirs(x)

if __name__ == '__main__':
    get_dictionary_word_list()


        