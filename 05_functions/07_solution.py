
# in place of *args, you can use any name you want
# the *args is just a convention
def sum_all(*args):
    print(args)
    for i in args:
        print(i * 2) 
        # here we have used print just to see
    return sum(args)
# sum is a built-in function in Python that adds all the numbers in an iterable (list, tuple, etc.) and returns the sum.

print(sum_all(1, 2, 3))
# print(sum_all(1, 2, 3, 4, 5))
# print(sum_all(1, 2, 3, 4, 5, 6, 7, 8))