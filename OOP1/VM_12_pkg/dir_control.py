# Author: Melissa Melaugh
# Date Created: 08 August 2016
# Date Updated: 12 August 2016
# Description: This contains all of the directory controls
# File: dir_control
# Status: In progress

# Imports:
import os
import zipfile  # https://docs.python.org/3/library/zipfile.html


def check_size(dir_name, a_size):
    # checks the size of a directory and all of its subfolders
    total_size = a_size

    for file_name in os.listdir(dir_name):
        full = os.path.join(dir_name, file_name)

        # if the path is a directory use recursion and return the size of the sub folder and add it to the total_size
        if os.path.isdir(full):
            print("Folder: {}".format(file_name))
            total_size += check_size(full, 0)
        else:
            size = os.path.getsize(full)
            print("File: {0} - {1} bytes".format(file_name, size))
            total_size += size

    print("The size of {0} is: {1} bytes".format(dir_name, total_size))
    return total_size
# end check_size


def open_dir(dir_name):
    # this checks if a directory is accessable and returns the directory and true if it is, none and false if not
    try:
        a_dir_name = os.path.abspath(dir_name)
        if os.path.isdir(a_dir_name):
            return a_dir_name, True
    except NotADirectoryError:
        print("Directory unaccessable.")

    return None, False
# end open_dir


def back_up(save_path, direct):
    # This backs up a system
    print("When the process is finished a message will be displayed.")

    # create the zip file and the text file that is the archive.
    a_zip = zipfile.ZipFile(os.path.join(save_path, "back_up.zip"), 'a')
    text_file = open(os.path.join(save_path, "Archive.txt"), 'w')

    text_file.write("Backup for: {}\n".format(direct))
    os.chdir(direct)
    for root, dirs, files in os.walk(direct):
        for file_name in files:
            # create the full path name, write the file name to the archive file, and then add it to the zip
            full = os.path.join(root, file_name)
            text_file.write("\nFile: {}".format(file_name))
            a_zip.write(full)

    # close the text file so that it properly saves before adding it to the top of the zip file and print complete
    text_file.close()
    os.chdir(save_path)
    a_zip.write("Archive.txt")
    print("Backup complete")
# end back_up
