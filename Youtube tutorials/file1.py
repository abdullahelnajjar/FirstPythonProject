class Dog:

    def __init__(self, name='', height='0', weight='0'):
        self.name = name
        self.height = height
        self.weight = weight

    def run(self):
        print('{} the dog runs'.format(self.name))

    def eat(self):
        print('{} the dog eats'.format(self.name))

    def barks(self):
        print('{} the dog barks'.format(self.name))


class Square:

    def __init__(self, height='0', width='0'):
        self.height = height
        self.width = width

    @property
    def height(self):
        print('Retrieving the height')
        return self.__height

    @height.setter
    def height(self, value):
        if value.isdigit():
            self.__height = value
        else:
            print('Please enter a number')

    @property
    def width(self):
        print("Retrieving the width")
        return self.__width

    # This is the setter
    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print("Please only enter numbers for width")

    @width.deleter
    def width(self):
        print('Deleting value')
        del self.__width

def getArea(self):
        return int(self.__width) * int(self.__height)

def main():
    aSquare = Square()

    height = input('Enter height: ')
    width = input('ENter widht: ')

    aSquare.height=height
    aSquare.width=width

    print('Height :', aSquare.height)
    print('Width :', aSquare.width)
    print('Area: ',aSquare.getArea())

if __name__ == '__main__':
    main()

