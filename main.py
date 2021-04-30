# todo 1 - list files and attributes (is directory, is cloud?)
#
# todo 2 - make folders to links
#    how to display??
#    inital: show on command line
#    2nd? pygame?`
#    3rd browser -> web server, python im WS installieren, deployen`
# todo 3 - make links navigatable
from file_functions.file_list import file_list

# todo move path to config -> later to db
my_file_list = file_list( "L:\\" ) 

files = my_file_list.get_file_objects()

for f in files:
	print( f.name )


# todo create database