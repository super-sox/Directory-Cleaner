#!/usr/bin/env python3
import os, shutil


def get_file_types(files):
    #get list of unique file types in directory
    file_types = []
    for file in files:
        name_type = file.split(".")
        if len(name_type) <= 2 and not name_type[1] in file_types:
            file_types += [name_type[1]]
        else:
            pass
    return file_types

def create_file_dir(file_types, target_path):
    #create a directory for each file type
    new_dir_names = []
    for file_type in types:
        new_dir_path = str(path + file_type + "_files/")
        new_dir_names += [new_dir_path]
        #only create directory if it does not already exist
        try:
            os.mkdir(new_dir_path)
        except OSError:
            print(f"Skipping {file_type + ' files'}! {new_dir_path} already exists!")
    return new_dir_names

path = "/home/micah/Code/FileSorter/"
dir_contents = os.listdir(path)
#pull list of files from directory contents
file_list = []
for item in dir_contents: 
    if os.path.isfile(path + item):
        file_list += [item]
print(file_list)
types = get_file_types(file_list)
print(types)
created_dir_paths = create_file_dir(types, path)
print(created_dir_paths)
command = input("Please enter a command: ")
if command == "rm dirs":
    for dir_path in created_dir_paths:
        os.rmdir(dir_path)
elif command == "ls":
    print(os.listdir(path))

