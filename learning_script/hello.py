#code=utf-8
'''
    test
'''
print("hello")
DICTTEST = {'Michael':95, 'Bob':75}
print(DICTTEST['Michael'])


def my_abs(num):
    '''
    shishdiadsf
    '''
    if num >= 0:
        return num
    else:
        return -num

for i, v in enumerate([1, 2, 3, 4, 5]):
    print(i, ":", v)

print(my_abs(1221))

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

for i in fib(10):
    print(i)








