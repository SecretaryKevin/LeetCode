def mergeTwoLists(list1, list2):
    """Merge two sorted lists into one sorted list>"""
    list3 = []
    while len(list1) > 0 and len(list2) > 0:
        if list1[0] <= list2[0]:
            list3.append(list1.pop(0))
        else:
            list3.append(list2.pop(0))
    if len(list1) > 0:
        list3.extend(list1)
    if len(list2) > 0:
        list3.extend(list2)
    return list3

list1 = [1, 2, 4]
list2 = [1, 3, 4]
test = mergeTwoLists(list1, list2)
print(test)

list1 = []
list2 = []
test = mergeTwoLists(list1, list2)
print(test)

list1 = []
list2 = [0]
test = mergeTwoLists(list1, list2)
print(test)