#! usr/bin/python

import sys

def main():
    print 'Test case'
    args_fun('James','Eva',
            'Tressie',
            Movie = 'Gatsby',
            Hero = 'Leonardo Di Caprio')


def args_fun(name, *args, **kwargs):
    print 'I am really sorry',name
    print '\n'

    for arguements in args:
       print 'These are arguments:' ,arguements

    for kw in kwargs:
        print kw ,' : ', kwargs[kw]

if  __name__ == '__main__':
    main()

