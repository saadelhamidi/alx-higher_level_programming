#!/usr/bin/python3
''' Module: 1-my_list
'''


class MyList(list):
    ''' Class: MyList
    inherits from list
    '''

    def print_sorted(self):
        ''' Method: print_sorted
        prints MyList in sorted order
        '''
        print(sorted(self))
