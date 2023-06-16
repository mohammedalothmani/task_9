class Rectangle:
    def __init__(self,length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        perimeter1 = 2 * (self.width + self.length)
        return perimeter1


    def area(self):
        area1 = self.width * self.length
        return area1

    def display(self):
        print(f'the length is : {self.length}')
        print(f'the width is : {self.width}')
        print('the areas is :', self.area())
        print('the areas is :', self.perimeter())

class Parallelepipede(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volum(self):
        volm = self.length * self.width * self.height
        return volm

    def display(self):
        super().display()
        print('the height is:', self.height)
        print('the volume is:', self.volum())


length = int(input('inter the length = '))
width = int(input('inter the width = '))
height = int(input('inter the width = '))
rectangle = Rectangle(length, width)
parallelepiped = Parallelepipede(length,width,height)
parallelepiped.display()

