from tempfile import mkstemp
from shutil import move, copymode
from os import fdopen, remove
import glob
import os

def replace(file_path, pattern, subst):
    #Create temp file
    fh, abs_path = mkstemp()
    with fdopen(fh,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, subst))
    #Copy the file permissions from the old file to the new file
    copymode(file_path, abs_path)
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)


myFiles = glob.glob('*.txt')
print(myFiles)
print(type(myFiles))
for f in myFiles:
    print("Replaceing",f)
    replace(f,"Car","0")
    replace(f,"Truck","1")
    replace(f,"Motorcycle","2")

