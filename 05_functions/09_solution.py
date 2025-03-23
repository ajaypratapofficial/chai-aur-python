def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i
# range(start, stop, step)
# start: Starting number of the sequence.
# stop: Generate numbers up to, but not including this number.
# step: Difference between each number in the sequence.
#
# The range() function generates a sequence of numbers starting from 0 by default, and increments by 1 (by default), and stops before a specified number.


for num in even_generator(10):
    print(num)