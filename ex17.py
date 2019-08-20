from sys import argv
from os.path import exists

# assign agurment to variables
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")


# we could do these two on one line, how?
# assign file to a variable
in_file = open(from_file)
# read from_file
indata = in_file.read()

# print the size of from_file
print(f"The input file is {len(indata)} bytes long")

# check if the target file is exist or not, return True if exist, False if non
print(f"Does the output file exists? {exists(to_file)}")
# ask user if he wants to continue or not
print("Ready, hit RETURN to continue, CTRL-C to abort.")
# hit ENTER to continue code
input()

# create target file for copying
out_file = open(to_file, 'w')
# write the data of from_file to to_file
out_file.write(indata)

print("All right, all done.")

out_file.close()
in_file.close()
