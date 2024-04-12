# class MyIterator:
#     def __init__(self, data):
#         self.data = data
#         self.index = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.index >= len(self.data):
#             raise StopIteration
#         value = self.data[self.index]
#         self.index += 1
#         return value

# # Using the iterator
# my_iter = MyIterator([1, 2, 3, 4, 5])
# for item in my_iter:
#     print(item)
# print(my_iter.__iter__())
# """
# Generators:
# A generator is a special type of iterator that generates values on-the-fly
#  instead of storing them in memory.
# Generators are particularly useful for generating large sequences of values
#  without storing them all in memory at once.
# """

# def my_generator(data):
#     for item in data:
#         yield item

# # Using the generator
# gen = my_generator([x for x in range(100)])
# for item in gen:
#     print(item)



# lst = [2,1, 4, 5, 1, 1]
# lst.remove(1)
# del lst[:]
# print(lst.pop(0)) # 2
# print(lst) # [1, 4, 5]
# print(lst.index(5)) # return index of specific value
# x = 1
# print(lst.count(x))
# lst.reverse() # Reverse elemnts in-place
# print(lst)

# Using the lists as queues
# from collections import deque
# Attendence = []

# queue = deque(['Eric', 'Anna', 'Mikka'])
# queue.append('Ahmed') # Appended at last of the queue
# queue.append('Mona') # Appended at last of the queue
# queue.append('Uri') # Appended at last of the queue
# print(list(queue))
# queue.popleft() # Now Eric is gone
# queue.popleft() # Now also Anna is gone
# print(list(queue))




# import pprint

# printer = pprint.PrettyPrinter()

# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]
# transposed = [[row[i] for row in matrix] for i in range(4)]
# print(*transposed)

# transposed1 = []
# for i in range(4):
#     transposed1.append([row[i] for row in matrix])

# print(*transposed1)



# tricky = list(zip(*matrix))
# printer.pprint(tricky)


# lst1 = [1, 2, 3]
# lst2 = [4, 5, 6]
# zipped = []
# for i, j in zip(lst1, lst2):
#     zipped.append(i)
#     zipped.append(j)

# print(zipped)

# singelton = 'ahmed', # Tricky Tuple
# print(singelton)
# print(len(singelton))

# seq_names = ['Ahmed', 'Mohammed', 'Ibrahime']
# for index, value in enumerate(seq_names):
#     print(index+1,' --> ', value)


# questions = ['name', 'quest', 'favorite color']
# answers = ['lancelot', 'the holy grail', 'blue']
# for q, a in zip(questions, answers):
#     print(f'What is your {q}? Its {a}')