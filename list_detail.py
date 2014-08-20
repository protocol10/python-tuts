#! usr/bin/env python

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
if __name__ == '__main__':
    main()
