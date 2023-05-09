# Creating a repository and connecting to it:
	
	git init

  	cd /path/to/local/repository

  	git add . 

  	git commit -m "Commit message here"

  	git remote add origin https://github.com/your-username/your-repository.git


# Push the changes to the remote repository on GitHub using the git push command:

	git push origin main

	OBS: Replace main with the name of the branch you want to push to, if it's not the default main branch.


# Virtual Environment:
	
	python -m venv env_name

	source env_name/Scripts/activate


# Committing changes to existing repos:

	git remote add origin <repository-url>

	git push -u origin main

	OR:

	git remote add origin <repository-url>

  	git add . 

  	git commit -m "Commit message here"

	git push -u origin main


# Git verification:
	
	git branch

	git status

	git log


#  Empty file creation:

	touch newfile.txt


# Printing text to the terminal:

	echo "Hello, world!"


# Displaying the contents of a file:

	cat file.txt


# Copying a file or directory:
	
	cp myfile.txt mycopy.txt.


# Moving a file or directory:

	mv myfile.txt mynewfile.txt


# Deleting a file or directory:

	rm dir_example

	rm -r dir_example -> deleting all content in it too


# Displaying the manual page for a given command:
	
	man ls / man <command>


# Displaying your command history:

	history


# Searching for text within files:

	grep "example" myfile.txt


# Searching for files and directories within a given directory hierarchy:

	find <starting_dir> -name somefile.txt

	OBS: You can specify any dir as the starting point by replacing . with the path to the desired dir.


# Counting lines, words and characters in a file or input stream:

	wc -l myfile.txt.  -> Only lines

	wc myfile.txt  -> Lines, words and characters 



