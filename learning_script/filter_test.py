'''
    remove prime number between 1~100
'''

def is_not_prime(num):
    '''
        check input num is prime or not
    '''
    result = False
    if num == 2 or num == 1:
        return True

    #loop from 2 to num -1, if mod is zero then is not prime
    for i in range(2, num, 1):
        if num % i == 0:
            result = True
            break
    return result

print '2 is:' + str(is_not_prime(2))
print '5 is:' + str(is_not_prime(5))
print '8 is:' + str(is_not_prime(8))
print '13 is:' + str(is_not_prime(13))

def get_unprime_num(min_val, max_val):
    '''
        return none prime num between minVal & max Val
    '''
    return filter(is_not_prime, range(min_val, max_val))


print get_unprime_num(1, 100)

