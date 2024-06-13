import os
from pathlib import Path
import click


filelist = []
finalstructure = []

@click.command()
@click.option('--filename', default='structureexample.txt', help='file containing desired option, default = structureexample.md')
@click.option('--opsys', prompt='os?', help='os file structure, 1 for linux, 2 for windows')

def get_dictionary_word_list(filename, opsys):
    """
    open file with the file structure and put in a list
    """
    f = open(filename)
    for word in f.read().split():
        filelist.append(word)
    print(filelist)
    splitter(filelist)

def splitter(filelist):
    level = int(1)
    for i in range(len(filelist)):
        if "├──" not in filelist[i]:
            level2 = int(filelist[i-1].count("├──"))
            if level2 == level:
                os.makedirs(filelist[i])
            elif level2 > level:
                cwd = Path(os.getcwd())
                foldername = Path(filelist[i-2])
                newpath = cwd/foldername
                os.chdir(newpath)
                os.makedirs(filelist[i])
                level = level + 1
            elif level2 < level:
                #for j in range(level - level2):
                cwd = Path(os.getcwd())
                foldername = Path("..")
                newpath = cwd/foldername
                #newpath = os.path.abspath(os.path.join(cwd, os.pardir))
                os.chdir(newpath)
                print(os.getcwd())
                os.makedirs(filelist[i])
                print(filelist[i])
                level = level2
            print(level)
            print(filelist[i])
                



if __name__ == '__main__':
    get_dictionary_word_list()


        