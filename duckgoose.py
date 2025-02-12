import sys
duck_goose = sys.argv[1:]
str_remove = 'goose'
while str_remove in duck_goose:
    duck_goose.remove(str_remove)
print(duck_goose)
