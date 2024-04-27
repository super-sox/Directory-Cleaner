#!/usr/bin/env python3
import os


def get_file_types(files):
    #get list of unique file types in directory
    file_types = []
    for file in files:
        name_type = file.lower().split(".")[1]
        if not name_type in file_types:
            file_types += [name_type]
        else:
            pass
    return file_types

def create_file_dir(file_types, target_path):
    #create a directory for each file type
    new_dir_paths = {}
    for file_type in types:
        new_dir_path = str(path + file_type + "_files/")
        new_dir_paths[file_type] = new_dir_path
        #only create directory if it does not already exist
        try:
            os.mkdir(new_dir_path)
            print(f"{file_type + '_files'} created!")
        except OSError:
            print(f"Skipping {file_type + ' files'}! {new_dir_path} already exists!")
    return new_dir_paths

def move_files(file_type_dirs, file_list, undo=False):
    for file_type in file_type_dirs:
        for file in file_list:
            if file_type in file.lower():
                if undo:
                    os.replace(str(file_type_dirs[file_type]) + file, path + file)
                    continue
                os.replace(path + file, str(file_type_dirs[file_type]) + file)


while True:
    path = input("Enter a directory path to clean: ")
    if path == "cwd":
        path = os.getcwd() + "/"
        print(path)
        dir_contents = os.listdir(path)
        break
    else:
        try:
            dir_contents = os.listdir(path)
            break
        except OSError:
            print("Error! Directory does not exist or is not accessible!")

#pull list of files from directory contents
files = []
for item in dir_contents: 
    #currently excludes files with more than one . in their name, such as hidden files and temporary files (i.e swap files)
    if os.path.isfile(path + item) and len(item.split(".")) <= 2 and item != "main.py":
        files += [item]

print("Getting file types...")
types = get_file_types(files)

print("Creating new directories...")
created_dir_paths = create_file_dir(types, path)

print("Moving files...")
move_files(created_dir_paths, files)

print("Target directory contents: ")
print(os.listdir(path))

while True:
    undo_y_n = input("Undo? y/n : ")
    if undo_y_n  == "y":
        move_files(created_dir_paths, files, True)
        for file_type in created_dir_paths:
            os.rmdir(created_dir_paths[file_type])
        print("Undo operation complete! Target directory contents: ")
        print(os.listdir(path))
        break
    elif undo_y_n == "n":
        break
    else:
        print("Error! Response not recognized!")
    
