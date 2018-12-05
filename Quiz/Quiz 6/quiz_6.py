# Defines two classes, Point() and Triangle().
# An object for the second class is created by passing named arguments,
# point_1, point_2 and point_3, to its constructor.
# Such an object can be modified by changing one point, two or three points
# thanks to the function change_point_or_points().
# At any stage, the object maintains correct values
# for perimeter and area.
#
# Written by Kun Zhang and Eric Martin for COMP9021


from math import sqrt

class Point():
    def __init__(self, x = None, y = None):
        if x == None and y == None:
            self.x = 0
            self.y = 0
        elif x == None or y == None:
            print('Need two coordinates, point not created.')
        else:
            self.x = x
            self.y = y

    def collinear(self, p2, p3):
        if (p2.y - self.y)*(p3.x - self.x) == (p2.x - self.x) * (p3.y - self.y):
            return True
        else:
            return False


class Triangle:
    def __init__(self, *, point_1, point_2, point_3):
    # variable after * are keyword only arguments in the form of point_1=xx
        if point_1.collinear(point_2, point_3):
            self.error_message('Initialisation')
        else:
            self._initialise(point_1, point_2, point_3)

    def error_message(self, phase):
        if phase == 'Initialisation':
            print('Incorrect input, triangle not created.')
        else:
            print('Incorrect input, triangle not modified.')
            print('Could not perform this change')


    def change_point_or_points(self, *, point_1 = None,
                                        point_2 = None,
                                        point_3 = None):
        temp_1 = self.get_point(point_1, self.p1)
        temp_2 = self.get_point(point_2, self.p2)
        temp_3 = self.get_point(point_3, self.p3)
        if temp_1.collinear(temp_2, temp_3):
            self.error_message('Modify')
        else:
            self._initialise(temp_1, temp_2, temp_3)

    @staticmethod
    def get_point(p, sp):
        if p is None:
            return sp
        return p

    def _initialise(self, p1, p2, p3):
        pass
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.area = self.get_area()
        self.perimeter = self.get_peri()

    def get_peri(self):
        line_1 = sqrt(abs(self.p1.x - self.p2.x)**2 + abs(self.p1.y - self.p2.y)**2)
        line_2 = sqrt(abs(self.p1.x - self.p3.x)**2 + abs(self.p1.y - self.p3.y)**2)
        line_3 = sqrt(abs(self.p2.x - self.p3.x)**2 + abs(self.p2.y - self.p3.y)**2)
        return line_1 + line_2 + line_3

    def get_area(self):
        return abs(self.p1.x * self.p2.y + self.p2.x * self.p3.y + self.p3.x * self.p1.y -\
                   self.p1.y * self.p2.x - self.p2.y * self.p3.x - self.p3.y * self.p1.x)/2

