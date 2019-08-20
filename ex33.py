j = 0
numbers = []
numbers_while = []

while j < 6:
    print(f"At the top i is {j}")
    numbers_while.append(j)

    j = j + 1
    print("Numbers now: ", numbers_while)
    print("At the bottom i is {}".format(j))

for num in numbers_while:
    print(num)


for i in range (0, 6):
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print(">>>> i", i)
    print("Numbers now: ", numbers)
    print("At the bottom i is {}".format(i))

for num in numbers:
    print(num)
