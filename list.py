#! usr/bin/env/python

import sys

def main():
    squares=[1, 2, 3, 4, 5]
    print squares
    print('Slicing index with -3',squares[-3])

    # squares[-2:] will slice the entries 4,5 
    print('Slicing funtion',squares[-2:])

    #squares[2:5] will create a new list 3,4,5
    print('Slicing function', squares[2:5])

    #replacing the entries in the list
    squares[3]=20

    #appending the list with new entries
    squares.append(25)
    squares.append(210)
    squares.append(2 ** 4)

    #Replacing multiple values
    squares[2:5] = ['C','D','E']

    print('New List', squares)

    #remove the elements from specific elements
    squares[2:5]=[]
    print squares
    print('Length of The List is ',len(squares))
    
    #remove the complete list
    squares[:]=[]
    print squares

    #creating Nested List
    a = ['a', 'b', 'c']
    b = ['1 ','2 ','3 ']
    x = [a, b]
    
    print 'Nested List'
    print x

    print 'Nested List item'
    print x[0]

    print 'Nested multidimensional data'
    print x[0][2]

#boiler plate similar to the main function in java.
if __name__ == '__main__':
    main()

