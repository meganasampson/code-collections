import os
from pathlib import Path
import click


filelist = []
finalstructure = []

@click.command()
@click.option('--filename', default='structureexample.md', help='file containing desired option, default = structureexample.md')
@click.option('--opsys', prompt='os?', help='os file structure, 1 for linux, 2 for windows')

def get_dictionary_word_list(filename, opsys):
    """
    open file with the file structure and put in a list
    """
    f = open(filename)
    for word in f.read().split():
        filelist.append(word)

    splitter(opsys)


def splitter(opsys):
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
    removesymbol(result, opsys)

def removesymbol(splitlist, opsys):
    """
    get rid of ugly ├── symbols
    """
    for i in splitlist:
        removedstuff = [x for x in i if "├──" not in x]
        finalstructure.append(removedstuff)
    del finalstructure[0]
    structuremaker(opsys)

def structuremaker(opsys):
    """
    actually make paths and create folders with them. Gives error to warn about naming issues.
    """
    try:
        if opsys == "1"
            for i in finalstructure:
                x = "/".join(i)
                print(x)
                os.makedirs(x)
        elif opsys == "2":
            print("No windows functionality yet")#doesnt work bc windows doesnt like ├── symbol :(
                for i in finalstructure:
                x = "\\".join(i)
                print(x)
                os.makedirs(x)
    except FileExistsError:
        print(f"The name -{x}- is already in use in this directory. Choose a different name or rename the existing folder.")


if __name__ == '__main__':
    get_dictionary_word_list()


        