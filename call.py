def binary_search(item, lst):
    found = False
    first = 0
    last = len(lst) - 1

    while first <= last and found == False:
        midpoint = (first + last) // 2
        if lst[midpoint] == item:
            found = True
        else:
            if lst[midpoint] < item:
                first = midpoint + 1
            else:
                last = midpoint - 1


    return found

print(binary_search(2, [1,2,4,6,8,9,14,17]))


