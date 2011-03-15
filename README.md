Gisty
=====

Gisty allows you to paste code to gist.gisthub.com

Options
-------

The following options are available:
- --login : Your Git username
- --passowrd : Your Git password
- --filename : The file to be added to gist
- --description : The description of your new gist
- --private : Add this option to make your gist private

Warning : Private gist are not secured. Anyone with the URL can access them.

Install
-------
Run the following commands:

	git clone git@github.com:maraca/gisty.git
	cd gisty
	python bootstap.py
	bin/buildout

You can now access gisty by doing the following;
	bin/gisty

Usage
-----
After installing gisty, you can start using it.
	cat 'yourfile.txt' | bin/gisty --login=yourusername

Gisty will return the url of your gist in the terminal.
If you have pbcopy installed, the url will be copied to your clipboard.


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



