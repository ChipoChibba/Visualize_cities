# Author:Chipo
# Date:11/1/2022
# Purpose:Lab 3

from Visualize_cities.city import City
from Visualize_cities.quicksort import *


# Comparing functions
def compare_cities(a, b):
    if type(a.name and b.name) == str:
        if a.name.lower() <= b.name.lower():
            return True
        return False


def compare_latitude(a, b):
    if type(a.latitude and b.latitude) == float:
        if a.latitude <= b.latitude:
            return True
        return False


def compare_populations(a, b):
    if type(a.popul and b.popul) == int:
        if a.popul <= b.popul:
            return False  # swapped returns for population
        return True


fp = open("../ShortAssignments/world_cities", "r")
rlist = []

# splitting each line into lists by "," delimiter
for line in fp:
    word = line.split(",")
    c = City(word[0], word[1], word[2], int(word[3]), float(word[4]), float(word[5]))
    rlist.append(c)

# for the iteration
i = 0
glist = ["cities_alpha", "cities_latitude", "cities_population"]
func_list = [compare_cities, compare_latitude, compare_populations]

while i < len(glist):
    fp_w = open(glist[i], "w")

    sort(rlist, func_list[i])

    # writing city objects onto files
    for c in rlist:
        fp_w.write(str(c))
        fp_w.write("\n")

    fp_w.close()
    i = i + 1

fp.close()
