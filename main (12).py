import numpy
class Numpy():
    def __init__(self, shape):
        self.shape = shape
    
    def numpy_zeros(self):
        #The zeros tool returns a new array with a given shape and type filled with 0's.
        #Default type is float
        print(numpy.zeros(shape, dtype = numpy.int))#Type changes to int

    def numpy_ones(self):
        #The ones tool returns a new array with a given shape and type filled with 1's.
        print(numpy.ones(shape, dtype = numpy.int))

if __name__ == '__main__':
    #The 'zeros' and 'ones' tools take tuple as argument 
    shape = tuple(map(int, input().split()))
    my_object = Numpy(shape)
    my_object.numpy_zeros()
    my_object.numpy_ones()
