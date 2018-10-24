class Util(object):
    def __init__(self):
        self
    
    @classmethod
    def perimeter(shape, *args):
        pass

    @classmethod
    def area(shape, *args):
        pass

    @classmethod
    def volume(cls, *args):
        volume = 0
        volume = reduce(lambda x, y: x*y, args)
        return volume

    @classmethod
    def speed(arg1, arg2):
        pass

    @classmethod
    def distance(arg1, arg2):
        pass

    @classmethod
    def time(arg1, arg2):
        pass
