# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just take one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
    print("I got nothin'.")

print_two("Oanh", "Nguyen")
print_two_again("Nguyen", "Trong")
print_one("Nguyen Trong Oanh")
print_none()
