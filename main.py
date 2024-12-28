# Открытие файлов

from pprint import pprint


name = "semple.txt"
file = open(name, 'r')
pprint(file.read())
file.close()