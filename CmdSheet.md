# creates a virtual environment

    python -m venv <env_name>

# activates the virtual environment

    <env_name>\Scripts\activate.bat 

# creates a new file "myfile.txt" with the text "This is some content" -

    echo This is some content > myfile.txt

    OBS: the > symbol is used as a redirector to send the output of a command to a file

# returns to parent directory.

    cd/  

# displays the content of file

    type <some_file> 

# finds folders and returns paths according to the name <my_folder>

    dir <folder_name> \s \a

# finds files and returns paths according to the name <filename>
    where /R C:\ filename.ext

    /s searches for the folder recursively in all subdirectories
    /a displays only the path, without any additional information

#  Graphically displays the folder structure of a drive or path.

    tree [drive:][path] [/f] [/a]

    /f -> Display the names of the files in each folder.
    /a -> Use ASCII instead of extended characters.

# is used to display the contents of a text file one screen at a time

    more <file_name>

# deletes a folder that is not empty on cmd

    rd /s /q <folder_name>
    /s (including all subdirectories) 
    /q (quiet mode) 
