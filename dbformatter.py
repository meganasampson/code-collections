#NO DATA INCLUDED IN DIRECTORY = WONT WORK FOR NOW

#Header stuff including packages we need, etc...

#packages we need
import pandas as pd
from pathlib import Path

#The os module provides a portable way of using operating system dependent functionality.
import os
import click

#Imports all the files into a dictionary

@click.command()
@click.option('--path', default=os.getcwd(), help='Directory in which the files you want to change are')
@click.option('--old', prompt='What variable do you want to change?',
              help='The old variable which you want to change')
@click.option('--new', prompt='What is the new variable name?',
              help='The new name of the variable you are changing')
def variablerename(path, old, new):
    #This renames the column headings for Reference

    #Assigns the variables and correction factor
    #Old_Variable = 'meta.refstr'
    #New_Variable = 'Reference'

    print(old)
    print(new)
    print(path)

    # Makes the substitution
    data = [x for x in os.listdir(path) if x.endswith('.xlsx')]

    # then it makes a list of the filenames minus the .xlsx ending
    fns = [os.path.splitext(os.path.basename(x))[0] for x in data]

    # this creates a dictionary of all the excel files, read to individual dataframes while skipping the 0th row
    # The key for each individual dataframe is the original filename minus .xlsx
    d = dict()
    for i in range(len(fns)):
        d[fns[i]] = pd.read_excel(data[i]) 

    for i in fns:
        if old in d[i].columns:
            d[i].rename(columns={old:new}, inplace=True)

    for i in fns:
        d[i] = d[i][d[i].columns.drop(list(d[i].filter(regex='Unnamed')))]

    #Exports the files to excel, having modified the column names
    for i in fns:
        d[i].to_excel(i+ '.xlsx') #export to excel

if __name__ == '__main__':
    variablerename()