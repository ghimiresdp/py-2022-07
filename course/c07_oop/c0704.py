class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return (f'Point({self.x}, {self.y})')

class Shape:
    """
    This is a sample shape class which is capable of adding multiple points

    For an instance if the shape has more than 3 points, the shape might not
    be a planar so we assume the shape with more than 3 vertices will not be
    planar
    """

    def __init__(self):
        self.__points = []
        self.is_plane = True

    def add_point(self, p: Point):
        """
        #####################
        step 1: points = []
        step 2: points = [Point(1, 2)]

        points = [(1, 2), (3,4), (5, 6), (7, 8)]
        points.append((9, 10))
        points = [(1, 2), (3,4), (5, 6), (7, 8), (9, 10)]
        """
        self.__points.append(p)
        if len(self.__points) > 3:
            self.is_plane = False
        else:
            self.is_plane = True

    def type(self):
        """
        points = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
        len(points) = 5
        print(types.get(len(points), "Unknown"))
        """
        types = {
            1: 'Point',
            2: 'Line',
            3: 'Triangle',
            4: 'Quadrilateral',
            5: 'Pentagon',
            # 6: 'Hexagon'
        }

        return types.get(len(self.__points), 'Unknown')


    def __str__(self):
        return f'Shape({self.type()})'

p1 = Point(2, 1)
p2 = Point(4, 3)



shape1 = Shape()
print(shape1, ', is_plane:', shape1.is_plane)

shape1.add_point(p1)
print(shape1, ', is_plane:', shape1.is_plane)

shape1.add_point(Point(4, 3))
print(shape1, ', is_plane:', shape1.is_plane)


shape1.add_point(Point(6, 1))
print(shape1, 'is_plane:', shape1.is_plane)

shape1.add_point(Point(5, -2))
print(shape1, 'is_plane:', shape1.is_plane)



# print(shape1)
