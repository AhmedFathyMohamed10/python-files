import time

def gen(list_item: list) -> int:
    size = len(list_item)
    total = 0
    iterator = 0
    start = time.perf_counter()
    print('Reached to while loop...')
    while iterator < size:
        total += list_item[iterator]
        iterator += 1
        print(f'Iterator ID: {iterator}, and Total is: {total}')
    end = time.perf_counter()

    return f'The total : {total}, and it takes : {round(end-start, 2)}'



lst = [1,2,3,4,5,6,7]
print(gen(lst))