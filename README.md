# UOCIS322 - Project 2 #

* Author: Freddy Lopez
* Email: flopez2@uoregon.edu

* Description: This project consisted of creating a file checking system for a server that vetted user requeseted files based off if the requested fil existed in the specified path, if the file name contained illegal characters "~" or ".." or if the file did in fact exist and the then would be transmitted to the user and displayed in browser. I used parse_config() from project0 in order to have app.py read the PORT and DEBUG values from credentials.ini and if credentials.ini is unreachable for whatever reason, then default.ini will be read to find the default PORT and DEBUG values. I also created .html files to display Error and error mesages for ERROR 403 and ERROR 404.
