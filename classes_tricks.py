# from dataclasses import dataclass, field

# # @dataclass
# # class Point:
# #     x: int
# #     y: int

# # p1 = Point(1, 2)
# # p2 = Point(2, 1)
# # p3 = Point(1, 2)

# # print(Point.__eq__(p1, p2))
# # print(Point.__eq__(p1, p3))


# # @dataclass
# # class Inventory:
# #     name: str
# #     unit_price: float
# #     quantity : int = 0

# #     def total(self):
# #         return self.unit_price * self.quantity
    
# # o = Inventory('Item1', 19.10, 2)
# # print(o.total())  



# # Inheritance from dataclasses

# @dataclass
# class Rectangle:
#     __width: int
#     __height: int

#     def __repr__(self) -> str:
#         return str(f'The area is: {self.area()}')

#     def area(self):
#         return self.__width * self.__height

# @dataclass
# class ColoredRectangle(Rectangle):
#     __color: str

#     def __repr__(self) -> str:
#         return str(f'{super().__repr__()}, and the color is: {self.__color}')

#     def print_color(self):
#         return self.__color

# # Example usage
# rect = ColoredRectangle(5, 4, "blue")
# rect.__color = 'green'
# print(rect)


# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]

# transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
# # print(transposed_matrix)
# # # Tricky
# # print(list(zip(*matrix)))
# flattened = [row for one in matrix for row in one]
# print(*flattened) # Series of number


class Vector:
    def __init__(self, x, y) -> None:
        self.__x = x
        self.__y = y

    def __add__(self, other):
        return Vector(self.__x + other.x, self.__y + other.y)
    

v1 = Vector(10, 20)
v2 = Vector(30, 40)
v3 = v1 + v2

print(v3)
