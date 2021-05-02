# TODO 1 - list files and attributes (is directory, is cloud?)
#
# TODO 2 - Create UI
#   how to display??
#   inital: show on command line
#   *** current ***
#  lets start with PySimpleGUI
#  see: https://realpython.com/pysimplegui-python/
#       install via python -m pip install pysimplegui
#  see: https://towardsdatascience.com/learn-how-to-quickly-create-uis-in-python-a97ae1394d5
#
#   *** laaater: 3rd browser -> web server, python in webserver or simple python web server ... all in container
#   *** probably never? pygame? <- for other samples

# TODO 3 - make folders to links / make links navigatable

from file_functions.file_list import file_list
#import file_functions.file_list

# TODO move path to config -> later to db
my_file_list = file_list( "L:\\" ) 

files = my_file_list.get_file_objects()

for f in files:
	print( f.name )


# TODO create database
