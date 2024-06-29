#!/usr/bin/python3

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

newlist = []
for i in list1:
    for j in list2:
        newlist.append([i, j])


print(newlist)