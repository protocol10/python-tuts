#! usr/bin/env python

def f(x): return x % 2 != 0 and x % 3 != 0

def cube(x): return x * x * x

def add(x, y): return x+y

def main():
    a = [20, 21,  55, 80]

    print 'Before Inserting', a
    a.insert(1, 2)
    print 'After Inserting ',a

    a.append(21)
    print 'After Appending', a

    count = a.count(21)
    print 'Number of times 21 has occured', count

    a.remove(21)
    print 'Using Remove Command', a

    index =  a.index(55)
    print 'Index of 55 is ', index

    a.reverse()
    print 'Reverse elements', a

    a.sort()
    print 'Sorting Command' ,a

    filter_func1 = filter(f, a)
    print filter_func1

    print 'Using Filter function for range 1 - 20 ', filter(f, range(1, 20))

    print 'Using Filter function for range 1 - 20 ', map(cube, range(1, 20))

    sequence = range(1, 20)
    print 'Using Filter function for range 1 - 20 ', map(add, sequence, sequence)

    print "LIST COMPREHENSION"
    squares = [ x**2 for x in range(1,10)]
    print squares

    print "NESTED LIST COMPREHENSION"
    row = [(x**2, y**2) for x in [1, 4, 5] for y in [3, 5, 6] if x != y]
    print row

    vec = [1, 2, -1, -4, 5, -7, 7]
    print 'Vec list',vec

    print 'Elemenating Negative numbers'
    vec_list = [x for x in vec if x>=0]
    print vec_list
if __name__ == '__main__':
    main()
