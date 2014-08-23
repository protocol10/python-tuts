#! usr/bin/env python

def f(x): return x % 2 != 0 and x % 3 != 0

def cube(x): return x * x * x
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


if __name__ == '__main__':
    main()
