from codecollections import Maker
import os

file_writer = Maker('../data/structureexample.txt', str(os.getcwd()))
file_writer.start_creation()