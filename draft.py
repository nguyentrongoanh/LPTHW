from sys import argv

script, from_file, to_file = argv

(open(to_file)).write(open(from_file).read())
