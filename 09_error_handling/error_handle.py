file = open('youtube.txt', 'w')
# if not exist then create a file

try:
    file.write('chai aur code')
finally:
    file.close()

with open('youtube.txt', 'w') as file:
    file.write('chai aur python')