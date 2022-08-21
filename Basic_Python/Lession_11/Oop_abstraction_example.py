from abc import ABC, abstractmethod
'''
class abstractClassName(ABC):
    [list of attributes]
    [list of methods]
    @abstrachmethod
    def methodName(self):
        pass
'''

class Polygon(ABC):
    @abstractmethod

    def draw(self):
        pass

    def get_area(self):
        pass

    def get_circle(self):
        pass

class Rectangle(Polygon):
    def __init__(self,width, height):
        self.width = width
        self.height = height

        def draw(self):
            print('Draw Rectangle')

        def get_width(self):
            return self.width

        def get_height(self):
            return self.height  
        
        def get_area(self):
            return self.width * self.height
        
        def perimeter(self):
            return 2*(self.width + self.height)

class Square(Polygon):
    def __init__(self,width):
        self.width = width

        def draw(self):
            print('Draw Spuare')

        def get_width(self):
            return self.width
        
        def get_area(self):
            return self.width * 2
        
        def perimeter(self):
            return 2*(self.width + self.width)

rect_obj = Rectangle(19,20)
print(f'fff:{rect_obj.draw()}')

sqr_obj = Square(22)
sqr_obj.draw()

poly_obj = Polygon()