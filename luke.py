import sys
def luke():
    relations = {'Darth Vader':'father', 'Leia':'sister', 'Han':'brother in law', 'R2D2':'droid', 'Rey':'Padawan', 'Tatooine':'homeworld'}
    x = relations[sys.argv[1]]
    if x == 'father':
        print("No, I am your father")
    else:
        print("Luke, I am your",x)
        
luke()