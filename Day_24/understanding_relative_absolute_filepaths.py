# Understanding relative and absolute file paths

# Paths
#
# we say we can open and close, and read and write the files
# sometimes files also have a path.


# File paths
# at the very root, is the origin. the root folder
# in windows, the root folder is usually c drive, or you can say a drive
# with a letter

# Absolute Filepath
# always start relative to the root
# starts from the origin
with open("E:\\Python_bootcamp_100days\\Day_24\\Project\\new_file.txt") as new_file:
    for i in new_file:
        print(i)
# Is relative to the root


# Relative file path
# If we are inside the project folder, or the working directory,
# we can use relative file path to get the file to work.
# eg ./talk.ppt # single dot represents the current directory
# eg ../report.doc  # meaning go up into hierarchy by one folder and find the file report.doc
# relative to our current working directory.
with open(".\\Project\\new_file.txt") as new_file:
    for i in new_file:
        print(i)


# in windows, the paths is separated by backslash
# in Mac, the paths are separated in forward slash
# but in python, we can put it as both.
