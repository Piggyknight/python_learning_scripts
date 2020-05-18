'''
   use map func to change input str to first word captial style
'''
from collections import Iterable

TEST_STR = ['adam', 'LISA', 'barT']

def custom_title(word):
    '''
        change first character to upper case
    '''
    word = word.title()
    return word


def test_func(strbuf):
    '''
        give string list, output first captial word, by
        using map/reduce func
    '''
    if not isinstance(strbuf, Iterable):
        print 'Input is not array!'
        return None
    return map(custom_title, strbuf)


print test_func(TEST_STR)







