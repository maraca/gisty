Gisty
=====

Gisty allows you to paste code to gist.gisthub.com

Options
-------

The following options are available:

* --login : Your Git username
* --passowrd : Your Git password
* --filename : The file to be added to gist
* --description : The description of your new gist
* --private : Add this option to make your gist private
* --ext : The extension of your file for syntax highlight. eg: .py, .c, .cs, .pl, .diff etc. 

Warning : Private gist are not secured. Anyone with the URL can access them.

Install
-------
Run the following commands:

	git clone git@github.com:maraca/gisty.git
	cd gisty
	python bootstrap.py
	bin/buildout

You can now access gisty by doing the following;
	bin/gisty

Usage
-----
After installing gisty, you can start using it.
	cat 'yourfile.txt' | bin/gisty --login=yourusername

Gisty will return the url of your gist in the terminal.
If you have pbcopy installed, the url will be copied to your clipboard.

File Extension
-------
By default, gist will consider your file as a text file.
To add an extension to your file, and add a better syntax, use the --ext command
For example :
	git diff | gisty --ext=.diff
Will show a colored diff syntax with green / red background.
	cat file.py | gisty --ext=.py
Will add syntax for python etc.



Recommended
-----------
I've added gist to my ~/bin/ folder

	vim ~/bin/gisty

Then add :
	
	#!/bin/bash
	
	~/bin/gist/bin/gisty --login=yourusername $*


That way I can use gisty anytime and anywhere :)

	echo 'Hi gisty ! ' | gisty 

Will return

	echo 'Hi gisty!' | gisty
	Password for yourusername@github: 
	https://gist.github.com/870387


Credits
----------
This project is a fork of a [gist](https://gist.github.com/763188) by [Marc Abramowitz](http://marc-abramowitz.com/).

