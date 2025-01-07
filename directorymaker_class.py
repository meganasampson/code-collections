import os
from pathlib import Path
import argparse
from dataclasses import dataclass


filelist = []
finalstructure = []


parser = argparse.ArgumentParser()
parser.add_argument("--filename", default = 'examples/structureexample.txt', type = str)
parser.add_argument("--location", default = str(os.getcwd()), type = str)

args = parser.parse_args()

class Maker():
    def __init__(self, filename, location) -> None:
        self.filelist = []
        self.filename: float = filename
        self.location = location

    def get_dictionary_word_list(self):
        """
        open file with the file structure and put in a list
        """
        f = open(self.filename)
        for word in f.read().replace("   ", "").replace("│","├──").split():
            self.filelist.append(word)
        print(self.filelist)
        self.folder_maker()

    def folder_maker(self):
        """
        loops through file structure list and makes folders based on ├── symbol
        """
        os.chdir(self.location)

        level = 1

        for i in range(len(self.filelist)):

            if "├──" not in self.filelist[i]:
                #checks where the next folder should be based on current level
                level2 = self.filelist[i-1].count("├──")

                if level2 == level:
                    #make folder in same directory
                    os.makedirs(self.filelist[i])

                elif level2 > level:
                    #moves DOWN next directory and makes folder in there
                    cwd = Path(os.getcwd())
                    foldername = Path(self.filelist[i-2])
                    newpath = cwd/foldername
                    os.chdir(newpath)
                    os.makedirs(self.filelist[i])
                    #make new level the current level
                    level = level + 1

                elif level2 < level:
                    for j in range(level - level2):
                        #moves UP to the correct directory and makes folder there
                        cwd = Path(os.getcwd())
                        foldername = Path("..")
                        newpath = cwd/foldername
                        os.chdir(newpath)
                    os.makedirs(self.filelist[i])
                    #make new level the current level
                    level = level2






if __name__ == '__main__':
    write_files = Maker(args.filename, args.location)
    write_files.get_dictionary_word_list()


        