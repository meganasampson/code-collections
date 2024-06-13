import os
from pathlib import Path
import click


filelist = []
finalstructure = []

@click.command()
@click.option('--filename', default='structureexample.txt', help='file containing desired option, default = structureexample.md')

def get_dictionary_word_list(filename):
    """
    open file with the file structure and put in a list
    """
    f = open(filename)
    for word in f.read().split():
        filelist.append(word)
    folder_maker(filelist)


def folder_maker(filelist):
    """
    loops through file structure list and makes folders based on ├── symbol
    """
    level = 1

    for i in range(len(filelist)):

        if "├──" not in filelist[i]:
            #checks where the next folder should be based on current level
            level2 = filelist[i-1].count("├──")

            if level2 == level:
                #make folder in same directory
                os.makedirs(filelist[i])

            elif level2 > level:
                #moves DOWN next directory and makes folder in there
                cwd = Path(os.getcwd())
                foldername = Path(filelist[i-2])
                newpath = cwd/foldername
                os.chdir(newpath)
                os.makedirs(filelist[i])
                #make new level the current level
                level = level + 1

            elif level2 < level:
                for j in range(level - level2):
                    #moves UP to the correct directory and makes folder there
                    cwd = Path(os.getcwd())
                    foldername = Path("..")
                    newpath = cwd/foldername
                    os.chdir(newpath)
                os.makedirs(filelist[i])
                #make new level the current level
                level = level2


if __name__ == '__main__':
    get_dictionary_word_list()


        