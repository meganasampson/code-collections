# code-collections

## Directory maker
Creates directory structure of a text file formatted as examples/structureexample.txt
- Run the command below to create the folder structure of examples/structureexample.txt
```
python directorymaker.py
```
### Options
- --filename : path the file that contains the desired directory structure, default = examples/structureexample.txt
- --location : directory to start creation from, default = current directory

## Database formatter
Changes name of column headers in an .xlsx files

Example
```
python directorymaker.py --old oldheader --new newheader
```

### Options
- --path : path to look for .xlsx files, default = current directory
- --old : column header to be changed
- --new : column header to be changed to
