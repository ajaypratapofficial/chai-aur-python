number = 3

for i in range(1, 11):
    if i == 5:
        continue
        # continue keyword will skip the current iteration and move to the next iteration
    print(number, 'x', i, '=', number * i)

